from django.contrib import admin
from .models import Mimodelo
 

class ModeloPosts(admin.ModelAdmin):
    list_display = ('campo1', 'campo2')
    search_fields = ['campo1']
    list_filter = ('campo1', 'campo2')
      
admin.site.register(Mimodelo, ModeloPosts)