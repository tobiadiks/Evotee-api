from django.contrib import admin
from .models import Election,Contestant
from School.models import Electorate

class ContestantInline(admin.TabularInline):
    model = Contestant
    extra = 5

class ElectionAdmin(admin.ModelAdmin):
    inlines = [ContestantInline]
    list_display = ('electionName','electionId','organizer','is_active')
    list_display_links = ('electionName','organizer')
    list_editable = ('is_active',)
    search_fields = ('electionName','organizer','electionId')
    list_per_page = 10

admin.site.register(Election, ElectionAdmin)



# Register your models here.
