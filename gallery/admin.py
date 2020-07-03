from django.contrib import admin
from .models import Website
from gallery.forms import SiteinfForm

# Register your models here.

class SiteinfFormAdmin(admin.ModelAdmin):
    readonly_fields=('img_pc','img_sm',)
    form = SiteinfForm