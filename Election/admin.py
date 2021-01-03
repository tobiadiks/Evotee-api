from django.contrib import admin
from .models import Election,Contestant, Voter
from School.models import Electorate

class ContestantInline(admin.TabularInline):
    model = Contestant
    extra = 4

class ElectionAdmin(admin.ModelAdmin):
    inlines = [ContestantInline]

admin.site.register(Election, ElectionAdmin)

admin.site.register(Voter)

# Register your models here.
