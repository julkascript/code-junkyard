from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (e, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
            if e == 'password2':
                field.widget.attrs['placeholder'] = 'Repeat password'
                field.widget.attrs['id'] = 'pass2'
            elif e == 'password1':
                field.widget.attrs['placeholder'] = 'Password'
                field.widget.attrs['id'] = 'pass1'
            else:
                field.widget.attrs['placeholder'] = e.capitalize()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'about_me', 'github_link', 'linkedin_link')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'
