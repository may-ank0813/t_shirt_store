from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello(request):
    return JsonResponse({'info': 'T-Shirt Store APP', 'name': "Mayank Saini"})

def home(request):
    return JsonResponse({'info': 'T-Shirt Store APP', 'name': "Mayank Saini"})
