from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=255, label=_('Full Name'))
    email = forms.EmailField(required=True, label=_('Email'))
    phone_number = forms.CharField(required=True, max_length=20, label=_('Phone Number'))
    user_type = forms.ChoiceField(choices=User.USER_CHOICES, label=_('User Type'))

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'phone_number', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.user_type = self.cleaned_data['user_type']
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=255, label=_('Full Name'))
    email = forms.EmailField(required=True, label=_('Email'))
    phone_number = forms.CharField(required=True, max_length=20, label=_('Phone Number'))
    user_type = forms.ChoiceField(choices=User.USER_CHOICES, label=_('User Type'))
    profile_photo = forms.ImageField(required=False)
    website1 = forms.URLField(required=False)
    website2 = forms.URLField(required=False)
    age = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'phone_number', 'user_type', 'profile_photo', 'website1', 'website2', 'age', 'location')