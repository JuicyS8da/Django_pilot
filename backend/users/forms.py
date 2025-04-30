from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(widget=forms.EmailInput, required=True)

    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя пользователя'})
    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
    password1.widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})
    password2.widget.attrs.update({'class': 'form-control', 'placeholder': 'Подтвердить пароль'})

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    username.widget.attrs.update({'placeholder': 'Имя пользователя'})
    password.widget.attrs.update({'placeholder': 'Введите пароль'})

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']