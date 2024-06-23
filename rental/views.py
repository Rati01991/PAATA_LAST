from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import AddCarForm, SearchForm

def home(request):
    cars = Car.objects.filter(available=True)
    context = {
        'cars': cars
    }
    return render(request, 'rental/home.html', context)

def car_details(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car': car
    }
    return render(request, 'rental/car_details.html', context)

def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful form submission
    else:
        form = AddCarForm()
    return render(request, 'rental/add_car.html', {'form': form})

def search_cars(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            make = form.cleaned_data.get('make')
            model = form.cleaned_data.get('model')
            min_year = form.cleaned_data.get('min_year')
            max_price = form.cleaned_data.get('max_price')

            # Implement your filtering logic here based on form data
            # Example:
            # cars = Car.objects.filter(make=make, model=model, year__gte=min_year, price_per_day__lte=max_price)

            # For simplicity, returning an empty list
            cars = []
        else:
            cars = []
    else:
        form = SearchForm()
        cars = []

    return render(request, 'rental/search.html', {'form': form, 'cars': cars})

from django.shortcuts import render, redirect
from .forms import UserCarSubmissionForm

def submit_car(request):
    if request.method == 'POST':
        form = UserCarSubmissionForm(request.POST, request.FILES)  # Include request.FILES for handling file uploads
        if form.is_valid():
            # Create a new instance of UserSubmittedCar and link it to the current user
            new_car = form.save(commit=False)
            new_car.owner = request.user  # Assign the current user as the owner
            new_car.save()
            return redirect('home')  # Redirect to the home page after successful submission
    else:
        form = UserCarSubmissionForm()
    
    return render(request, 'rental/submit_car.html', {'form': form})

from django.shortcuts import render
from .models import Car, UserSubmittedCar

def home(request):
    # Query available cars from main Car model
    cars = Car.objects.filter(available=True)

    # Query user-submitted cars from UserSubmittedCar model
    user_submitted_cars = UserSubmittedCar.objects.all()

    context = {
        'cars': cars,
        'user_submitted_cars': user_submitted_cars,
    }
    return render(request, 'rental/home.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import UserSubmittedCar
from .forms import UserCarSubmissionForm

def update_car(request, car_id):
    car = get_object_or_404(UserSubmittedCar, pk=car_id)

    if request.method == 'POST':
        form = UserCarSubmissionForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after update
    else:
        form = UserCarSubmissionForm(instance=car)
    
    return render(request, 'rental/update_car.html', {'form': form})

def delete_car(request, car_id):
    car = get_object_or_404(UserSubmittedCar, pk=car_id)

    if request.method == 'POST':
        car.delete()
        return redirect('home')  # Redirect to home page after deletion
    
    return render(request, 'rental/delete_car.html', {'car': car})