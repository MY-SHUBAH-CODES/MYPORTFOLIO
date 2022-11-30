from django.contrib import admin
from app1.models import *

# Register your models here.
class MyCirtificatesAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyCirtificates,MyCirtificatesAdmin)


