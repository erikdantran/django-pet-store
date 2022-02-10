from django import forms
from django.forms import ModelForm
from .models import Pet, Customer

class PetForm(ModelForm):
  class Meta:
    model = Pet
    fields = ('name', 'breed', 'age', 'color', 'category', 'description', 'imageUrl')

class CustomerForm(ModelForm):
  class Meta:
    model = Customer
    fields = ('name', 'email', 'phone', 'card')