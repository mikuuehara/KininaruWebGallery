from django import forms
#from . import models
from gallery.models import Sitecategory, Sitecolor, Website

class ColorForm(forms.ModelForm):
    class Meta:
        model = Sitecolor
        fields = ('name',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Sitecategory
        fields = ('name',)

class SiteinfForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name','url','img_pc','img_sm','color','category','add_date',)

class SelectForm(forms.Form):
    forms.ModelChoiceField(
        label='カテゴリ',
        queryset=Sitecategory.objects.all(), 
        required=False)
        #widget=forms.widgets.Select