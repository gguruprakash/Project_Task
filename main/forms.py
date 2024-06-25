from django import forms
from .models import UserProfile, Task

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'mobile_number', 'password', 'address']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date', 'time', 'assigned_to', 'status']




       

    
   