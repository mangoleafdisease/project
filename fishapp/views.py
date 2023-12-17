from django.shortcuts import render, redirect
from .forms import FishForm
from .models import Fish
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import random

# Create your views here.


def index(request):
    fishs = Fish.objects.all()
    context = {'fishs': fishs}
    return render(request, 'fishapp/index.html', context=context)


def details(request, fish_id):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['price'] = request.POST['price']
        request.session['color'] = request.POST['color']
        request.session['size'] = request.POST['size']
        return redirect('order')
    fish = Fish.objects.get(pk=fish_id)
    sizes = fish.size.split(',')
    in_stock = random.randint(1, 50)
    context = {'fish': fish, 'sizes': sizes, 'in_stock': in_stock}
    return render(request, 'fishapp/details.html', context)


def add(request):
    form = FishForm()
    context = {'form': form}
    return render(request, 'fishapp/add.html', context)


def order(request):
    if request.method == 'POST':
        quantity_int = request.POST['quantity']
        quantity = int(quantity_int)
        request.session['quantity'] = quantity
        return redirect('order_placed')
    name = request.session.get('name')
    price = request.session.get('price')
    color = request.session.get('color')
    size = request.session.get('size')
    context = {'name': name, 'price': price, 'color': color, 'size': size}
    return render(request, 'fishapp/order.html', context)


def order_placed(request):
    price = request.session['price']
    price = int(price)
    quantity = request.session['quantity']
    total = price * quantity
    context = {'total': total}
    return render(request, 'fishapp/order_placed.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'fishapp/login.html')


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'fishapp/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
