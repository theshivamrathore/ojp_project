from django.contrib import admin
from .models import *
# Register your models here.

class Govjob_detail_admin(admin.ModelAdmin):
    list_display = ['company','post_name','education','total_post','location','last_date']

admin.site.register(Govtjob_detail_model,Govjob_detail_admin)
