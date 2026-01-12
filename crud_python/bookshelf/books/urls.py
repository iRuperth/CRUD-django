from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view(), name='books-list'),
    path('books/<int:pk>/', views.BooksDetail.as_view(), name='books-detail'),
]