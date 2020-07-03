from django import forms
#from . import models
from gallery.models import Sitecategory, Sitecolor, Website

num_choicies = (
    (10, 10), 
    (20, 20),
    )

turn_choicies = (
    ('new', 'new'),
    ('random', 'random'),
)

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
    category = forms.ModelMultipleChoiceField(
        label="カテゴリ",
        queryset=Sitecategory.objects.all(), 
        required=False,
        widget=forms.CheckboxSelectMultiple
        )
    
    color = forms.ModelMultipleChoiceField(
        label="色",
        queryset=Sitecolor.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    
    num = forms.ChoiceField(
        label='表示数',
        choices=num_choicies,
        required=True
    )

    turn = forms.ChoiceField(
        label='表示順',
        choices=turn_choicies,
        required=True
    )