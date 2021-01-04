from django.contrib import admin
from .models import Electorate

class ElectorateAdmin(admin.ModelAdmin):
    
    list_display = ('electorateName','electorateEmail','electorateId','electorateApproved')
    list_display_links = ('electorateName','electorateEmail')
    list_editable = ('electorateApproved',)
    search_fields = ('electorateName','electorateEmail','electorateId')
    list_per_page = 10





admin.site.register(Electorate , ElectorateAdmin)
# Register your models here.
