from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165515',
        'name': 'Eva Yunia Aliyanshah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
