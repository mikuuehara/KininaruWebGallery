from django import forms
from gallery.widgets import CustomCheckboxSelectMultiple
from gallery.models import Sitecategory, Sitecolor, Website

### 表示数の選択肢 ###
num_choicies = (
    (5, 5),
    (10, 10), 
    (20, 20),
    )
### 表示順の選択肢 ###
turn_choicies = (
    ('new', '新着順'),
    ('old', '古い順'),
    ('random', 'ランダム'),
)


### 色の登録 ###
class ColorForm(forms.ModelForm):
    class Meta:
        model = Sitecolor
        fields = ('name',)

    
### カテゴリの登録 ###
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Sitecategory
        fields = ('name',)


### サイト情報の登録 ###
class SiteinfForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name','url','img_pc','img_sm','color','category','add_date',)


### 表示するサイトを選択 ###
class SelectForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        label="",
        queryset=Sitecategory.objects.all(), 
        required=False,
        widget=CustomCheckboxSelectMultiple,
        #widget=forms.CheckboxSelectMultiple
        )
    
    color = forms.ModelMultipleChoiceField(
        label="",
        queryset=Sitecolor.objects.all(),
        required=False,
        widget=CustomCheckboxSelectMultiple
        #widget=forms.CheckboxSelectMultiple
    )
    
    num = forms.ChoiceField(
        label='',
        choices=num_choicies,
        required=True
    )

    turn = forms.ChoiceField(
        label='',
        choices=turn_choicies,
        required=True
    )
