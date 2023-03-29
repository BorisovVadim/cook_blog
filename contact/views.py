from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import ContactForm
from .models import ContactLink


class ContactView(View):

    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'
