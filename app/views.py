# from django.shortcuts import render
# import requests

# # Create your views here.

# def index(request):
#     url = "https://api.freeapi.app/api/v1/public/meals"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         meals_data = data.get('data', {}).get('data', [])
    
#     # For filtering required columns
#     filtered_data = []
#     for meal in meals_data:
#         filtered_data.append({
#             'name': meal['strMeal'],
#             'thumbnail': meal.get('strMealThumb'),
#             'category': meal['strCategory'],
#             'area': meal['strArea'],
#             # 'strInstructions': meal['strInstructions']
#         })

#     return render(request, 'pages/index.html', {'meals': filtered_data})

from django.shortcuts import redirect, render, get_object_or_404
import requests
from .models import Meal

def index(request):
    url = "https://api.freeapi.app/api/v1/public/meals"
    response = requests.get(url)
    meals = response.json()['data']['data']
    
    if request.method == "POST":
        meal_name = request.POST.get("meal_name")
        meal_category = request.POST.get("meal_category")
        meal_area = request.POST.get("meal_area")
        meal_id = request.POST.get("meal_id")
        bill_total = request.POST.get("bill_total")

        # Ensure that the meal is not duplicated
        meal, created = Meal.objects.get_or_create(
            id=meal_id,
            defaults={
                'name': meal_name,
                'category': meal_category,
                'area': meal_area,
                'bill_total': bill_total
            }
        )
        if not created:
            meal.bill_total = bill_total
            meal.save()
        
        return redirect('index-page')

    context = {
        'meals': meals
    }
    return render(request, 'pages/index.html', context)


def transactions(request):
    transactions = Meal.objects.exclude(bill_total__isnull=True)
    context = {
        'transactions': transactions
    }
    return render(request, 'pages/transactions.html', context)

def edit_transaction(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    context = {
        'meal': meal
    }
    return render(request, 'pages/edit_transaction.html', context)

def delete_transaction(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    meal.delete()
    return redirect('transactions-page')

def print_bill_page(request, meal_id):
    bill = get_object_or_404(Meal, id=meal_id)
    context = {
        'bill': bill
    }
    return render(request, 'pages/print_bill_page.html', context)
