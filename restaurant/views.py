
from django.shortcuts import render
from .models import FoodItem, StaffMember


def home(request):
    return render(request, 'restaurant/home.html')


def menu(request):
    foods = FoodItem.objects.all()
    return render(request, 'restaurant/menu.html', {'foods': foods})


def administration(request):
    staff = StaffMember.objects.all()
    return render(request, 'restaurant/administration.html', {'staff': staff})


def contact(request):
    return render(request, 'restaurant/contact.html')
