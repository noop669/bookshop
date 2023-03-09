from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from .models import *


class Cart(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_city'].empty_label = "Город не выбран"
        self.fields['books'].empty_label = 'Книга не выбрана'

    class Meta:
        model = Chek
        fields = ['books', 'count', 'delivery_city']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class SupportForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class RePassword(PasswordChangeView):

    class Meta:
        model = User


class ResetPassword(PasswordChangeDoneView):

    class Meta:
        model = User


class ShowProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=255)

    class Meta:
        model = User
        fields = ('first_name',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
