from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.detail, name='book_detail'), 
    path('create/', views.create, name='create'),
    path('<int:book_id>/edit/', views.update_book, name='update_book'),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
