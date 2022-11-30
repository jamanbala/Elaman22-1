from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=3, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(min_length=3, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=3, widget=forms.PasswordInput)

