from django.shortcuts import render

def show_main(request):
    context = {
        'flower_t1': 'Red Spider Lily',
        'amount_t1': '4',
        'desc_t1': 'Known as the flower of farewell, it symbolize abandonment, loss, death, and separation.',
        'flower_t2': 'Blue Rose',
        'amount_t2': '1',
        'desc_t2': 'A depiction of unrequited love. Others say it means to attain the impossible. Perhaps both can coexist.',
        'flower_t3': 'Sunflower',
        'amount_t3': '2',
        'desc_t3': 'Full of warmth and happiness. Such happiness might be the goal of many.',
        
    }

    return render(request, "main.html", context)