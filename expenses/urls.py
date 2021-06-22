from django.urls import path

from tracker.expenses.views import create_expense, edit_expense, delete_expense, profile, profile_edit, profile_delete, \
    home

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_expense, name='create_expense'),
    path('edit/<int:pk>', edit_expense, name='edit_expense'),
    path('delete/<int:pk>', delete_expense, name='delete_expense'),
    path('profile/',profile, name='profile'),
    path('profile/edit', profile_edit, name='profile_edit'),
    path('profile/delete', profile_delete, name='profile_delete'),


]
