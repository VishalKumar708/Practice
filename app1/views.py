from django.shortcuts import render
from .forms import StudentForm, ContactForm
# from .forms import *


def register_user_form(request):

    if request.method == 'POST':
        text_data = request.POST
        file_data = request.FILES
        form = StudentForm(text_data, file_data)

        if form.is_valid():
            form.save()
            return render(request, 'register_user.html', context={'form': StudentForm()})
        else:
            return render(request, 'register_user.html', context={'form': form})

    form = StudentForm(initial={'gender': 'male', 'name': 'Shruti'})
    form.order_fields(field_order=('photo', 'gender', 'name', 'email'))
    return render(request, 'register_user.html', context={'form': form})
# Create your views here.


def get_contact_form(request):
    form = ContactForm(auto_id="%s")
    return render(request, 'contact_form.html', context={'form': form})


def get_details(request):
    data = request.POST
    form = ContactForm(request.POST)
    print("is valid=> ", form.is_valid())
    print('data=> ', data)
    return render(request, template_name='contact_form.html', context={'form': form})