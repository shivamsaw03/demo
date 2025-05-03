from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('profile/',views. myprofile.as_view(), name='profile'),
    path('form/',views. Form.as_view(), name='form'),
]