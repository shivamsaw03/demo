from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Bookstore Admin"
admin.site.site_title = "Bookstore Admin Portal"
admin.site.index_title = "Welcome to Bookstore Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]