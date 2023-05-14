from django.contrib import admin

# import your Services model here
from service.models import Services

# list all fields of your Services models which you want to show in admin panel


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_title', 'service_des')


# Register your models here.
admin.site.register(Services, ServiceAdmin)
