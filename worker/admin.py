from django.contrib import admin
from . models import Worker, Unit, Visit


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',  'created_at')
    search_fields = ['name']
	

class UnitAdmin(admin.ModelAdmin):
    search_fields = ['name']
	

class VisitAdmin(admin.ModelAdmin):
    search_fields = ['unit__name', 'unit__worker__name']
	
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Visit, VisitAdmin)