
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_visible = models.BooleanField(default=True)

    def _str_(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} - {self.email}"
    
class Profile(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=150,default= "gfdr")
    About = models.TextField(max_length=150,default= "gfdr")
    Mobile=models.CharField(max_length=150,default= "gfdr")
    Address=models.CharField(max_length=150,default= "gfdr")
    def _str_(self):
        return f"{self.Name}"
    def _str_(self):
        return self.Email  
    