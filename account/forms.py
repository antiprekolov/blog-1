from django import forms
from django.contrib.auth.models import User
from .


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают')
        return cd['password2']


class UserForm()


    class Form(forms.ModelForm):
        class Meta:
            model = User
            fields = ['first_name', 'last_name', 'email']

    class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['date_of_birth', 'about_me']


