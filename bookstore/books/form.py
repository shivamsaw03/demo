from django import forms
from .models import Profile

class profileform(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields =['Name', 'Email', 'Address', 'About', 'Mobile']