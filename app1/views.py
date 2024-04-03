from django.shortcuts import render
from .forms import StudentForm
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
