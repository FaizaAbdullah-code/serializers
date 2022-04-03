from django.contrib import admin

from .models import Heros, bioData
admin.site.register(Heros)
# Register your models here.
admin.site.register(bioData)