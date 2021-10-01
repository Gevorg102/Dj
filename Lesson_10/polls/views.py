from django.shortcuts import render, redirect

from .forms import  StudentForm, UserForm
def home_view(request):

    context ={}
    context['form']= UserForm()
    return render(request, "home.html", context)


def student(request):
    error = ' '
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Your number is already used'

    form = StudentForm()
    context ={}
    context['students']= form
    context['error']= error
    return render(request, "home.html", context)