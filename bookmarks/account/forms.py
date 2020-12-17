from django import forms
from django.contrib.auth.models import User
from .models import Profile


# форма авторизации
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# регистрация пользователей
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


# возможность пользователя редактировать профили через сайт
# позволит пользователям менять имя, фамилию, e-mail (поля встроенной в 
# Django модели)
class UserEditFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# позволит модифицировать дополнительные сведения, которые мы сохраняем в 
# модели Profile (дату рождения и аватар)
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

