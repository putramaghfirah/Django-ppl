from django.contrib import admin
from .models import (
    Book,
    Cover
)
# Register your models here.

admin.site.register(Book)
admin.site.register(Cover)
