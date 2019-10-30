from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    confirmation_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    birthdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'type': 'date'
            }
        )
    )

    def clean(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['confirmation_password']
        if pass1 != pass2:
            raise forms.ValidationError('Passwords do not match')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        login_email = User.objects.filter(email=email)
        if login_email.exists():
            raise forms.ValidationError('email already exists')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        login_username = User.objects.filter(username=username)
        if not login_username.exists():
            raise forms.ValidationError('this email does not exist Please sign up')
        return username