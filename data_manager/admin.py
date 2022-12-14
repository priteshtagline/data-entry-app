from django.contrib import admin

# Register your models here.
from .models import Events, Countries
admin.site.register(Events)
admin.site.register(Countries)