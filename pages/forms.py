from django import forms
from django.contrib.auth.models import User
from pages.models import Region, Place


class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the region name.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please describe the region.")

    class Meta:
        model = Region
        fields = ('name',)
        exclude = ('description',)


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Name:")
    population = forms.IntegerField(initial=0, help_text='Population:')
    description = forms.CharField(widget=forms.Textarea, help_text='Description:')
    economy = forms.CharField(widget=forms.Textarea, help_text='Economy:')
    special_features = forms.CharField(widget=forms.Textarea, help_text='Special Features:')

    class Meta:
        model = Place
        fields = ('name', 'population', 'description', 'economy', 'special_features')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
