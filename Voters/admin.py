from django.contrib import admin

from .models import Voter


class VoterAdmin(admin.ModelAdmin):
    
    list_display = ('firstName','lastName','idNumber','active','voted')
    list_display_links = ('firstName','idNumber')
    list_editable = ('active','voted')
    search_fields = ('firstName','lastName','idNumber')
    list_filter=('active','qualifiedElection')
    list_per_page = 10




admin.site.register(Voter,VoterAdmin)

# Register your models here.
