from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Customer, CustomerStatus

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role', 'assigned_checker')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter to show only checkers in the assigned_checker dropdown
        self.fields['assigned_checker'].queryset = User.objects.filter(role='checker')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'photo', 'resume']

class CustomerStatusForm(forms.ModelForm):
    class Meta:
        model = CustomerStatus
        fields = ['status']
