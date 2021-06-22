from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home-no-profile.html')

def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    pass


def delete_expense(request, pk):
    pass


def profile(request):
    return render(request, 'profile.html')


def profile_edit(request):
    pass

def profile_delete(requet):
    pass