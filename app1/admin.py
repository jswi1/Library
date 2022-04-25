from typing import Tuple

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    pass

@admin.register(Kitob)
class app1:KitobAdmin(ModelAdmin)
    list_display = ("nom", "sahifa", "janr")
    search_fields = ("id", "nom")
    list_filter = ("janr",)
    autocomplate_fields = ("muallif",)

@admin.register(Muallif)
class MuallifAdmin(ModelsAdmin):
    search_fields = ("id", "ism", "tirik")

admin.site.register(Muallif)
admin.site.register(Kitob)
admin.site.register(Student)
admin.site.register(Record)
