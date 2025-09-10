from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406496366',
        'name': 'Theo Samuel',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
