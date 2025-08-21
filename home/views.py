from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact  # Ensure the model name is capitalized

# Create your views here.
def index(request):
    flavor_data = [
        {"flavor": "Orange", "img": "orangef", "price": 100},
        {"flavor": "Coal", "img": "coalf", "price": 110},
        {"flavor": "Lemon", "img": "lemonf", "price": 105},
        {"flavor": "Mango", "img": "mangof", "price": 120},
        {"flavor": "Raspberry", "img": "rasberryf", "price": 115},
        {"flavor": "Bubblegum", "img": "buublegumf", "price": 110},
        {"flavor": "All Flavors Pack", "img": "allf", "price": 120},
        {"flavor": "Combo Pack", "img": "combo", "price": 120},
        {"flavor": "Icepops", "img": "icepops", "price": 100},
    ]

    context = {
        'variable': "harshitha",
        'flavors': flavor_data
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        # Save the contact data to the database
        c = Contact(email=email, phone=phone, message=message)
        c.save()  # Ensure the data is saved to the database

        # Render the thank-you page
        return render(request, 'submit.html')

    return render(request, 'contact.html')
