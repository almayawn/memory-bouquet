from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import FlowerForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Flower
from django.contrib import messages

def show_main(request):
    flowers = Flower.objects.all()

    total_entries = len(flowers)
    if (total_entries > 1):
        entry_messages = f'You have a total of {total_entries} entries'
    else:
        entry_messages = f'You have a total of {total_entries} entry'

    context = {
        'name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
        'flowers': flowers,
        'total_entry_message': entry_messages,
    }

    return render(request, "main.html", context)

def create_entry(request):
    form = FlowerForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        name = form.cleaned_data['name']
        messages.success(request, f'succesfully added a new entry "{name}"')
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_entry.html", context)

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