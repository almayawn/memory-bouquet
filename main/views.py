import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import FlowerForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Flower
from django.contrib import messages

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {
        'form':form,
        'owner_name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
        }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {
        'owner_name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_main(request):
    flowers = Flower.objects.filter(user=request.user)

    total_entries = len(flowers)
    if (total_entries > 1):
        entry_messages = f'You have a total of {total_entries} entries'
    else:
        entry_messages = f'You have a total of {total_entries} entry'

    context = {
        'owner_name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
        'name': request.user.username,
        'flowers': flowers,
        'total_entry_message': entry_messages,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_entry(request):
    form = FlowerForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        name = form.cleaned_data['name']
        messages.success(request, f'succesfully added a new entry "{name}"')
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
        'owner_name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
    }
    return render(request, "create_entry.html", context)

def increment_flower_amount(request, pk_id):
    if request.method == 'POST':
        flower = Flower.objects.get(id=pk_id)
        flower.amount += 1
        flower.save()
    
    return redirect('main:show_main')

def decrement_flower_amount(request, pk_id):
    if request.method == 'POST':
        flower = Flower.objects.get(id=pk_id)
        if flower.amount > 0:
            flower.amount -= 1
            flower.save()
    
    return redirect('main:show_main')

def delete_flower(request, pk_id):
    if request.method == 'POST':
        flower = Flower.objects.get(id=pk_id)
        flower.delete()
    
    return redirect('main:show_main')

def show_xml(request):
    data = Flower.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Flower.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Flower.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Flower.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")