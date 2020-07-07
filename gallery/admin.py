from django.contrib import admin
from gallery.models import Sitecategory, Sitecolor, Website
from gallery.forms import ColorForm, CategoryForm, SiteinfForm, SelectForm

# Register your models here.
admin.site.register(Website)
admin.site.register(Sitecategory)
admin.site.register(Sitecolor)

class SiteinfFormAdmin(admin.ModelAdmin):
    readonly_fields=('img_pc','img_sm',)
    form = SiteinfForm