from pyexpat import model
from django.contrib import admin 
from health import models
import nested_admin
from .models import Blog , Comment , Clinic_info
from health.models import Clinic, Day,Doctor, Hours


class hours(nested_admin.NestedStackedInline):
    model=Hours
    extra = 1
    


class DayInline(nested_admin.NestedStackedInline):
    model=Day
    inlines=[hours]
    extra = 1
    

class ClinicAdmin(nested_admin.NestedModelAdmin):
    inlines=[DayInline]  




# Register your models here.
admin.site.register(Clinic,ClinicAdmin)
admin.site.register(Doctor)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Clinic_info)