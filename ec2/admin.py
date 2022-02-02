from django.contrib import admin
from .models import Instance
# Register your models here.

@admin.register(Instance)

class InstanceAdmin(admin.ModelAdmin):
    readonly_fields = ("instance_id", "instance_state", )
    pass
    
#admin.site.register(Instance, InstanceAdmin)

