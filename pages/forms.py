from django import forms
from django.contrib.auth.models import User
from pages.models import Region


class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the region name.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please describe the region.")

    class Meta:
        model = Region
        fields = ('name',)
        exclude = ('description',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
