from django.contrib import admin
from .models import Services
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    fields = ["service_title", "service_content", "service_published"]


admin.site.register(Services, ServiceAdmin)