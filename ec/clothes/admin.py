from django.contrib import admin

from clothes.models import Brand, Clothes

# Register your models here.
admin.site.register(Brand)
admin.site.register(Clothes)