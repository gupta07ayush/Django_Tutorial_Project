from django.contrib import admin

# import your model here
from service.models import Block


# list all fields of you models which you want to show in admin panel
class BlockAdmin(admin.ModelAdmin):
    display = ('block_icon', 'block_title', 'block_des')


# Register your models here.
admin.site.register(Block, BlockAdmin)
