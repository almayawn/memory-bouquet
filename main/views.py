from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alma Laras Bestari',
        'npm': '2206082303',
        'class': 'PBP E',
        'application': 'Memory Bouquet',
    }

    return render(request, "main.html", context)