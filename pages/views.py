from django.shortcuts import render
from .models import ContactPage

# Create your views here.


def contactPageView(request):
    if request.method=="POST":
            contact = ContactPage()
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('subject')
            contact.name=name
            contact.email=email
            contact.message=message
            contact.image = request.FILES['image']
            contact.save()
            return HttpResponse("<h2> Hey, Thanks for Contact with us, Please Go Back privous Page! </h2>")
    return render(request, 'contact.html')
