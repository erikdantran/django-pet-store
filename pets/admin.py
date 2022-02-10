from django.contrib import admin
from .models import Pet, Customer

# Register your models here.
admin.site.register(Pet)
admin.site.register(Customer)