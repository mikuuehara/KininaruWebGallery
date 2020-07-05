from django import forms
from gallery.widgets import CustomCheckboxSelectMultiple
from gallery.models import Sitecategory, Sitecolor, Website

### 表示数の選択肢 ###
num_choicies = (
    (10, 10), 
    (20, 20),
    )
### 表示順の選択肢 ###
turn_choicies = (
    ('new', 'new'),
    ('random', 'random'),
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
        label="カテゴリ",
        queryset=Sitecategory.objects.all(), 
        required=False,
        widget=CustomCheckboxSelectMultiple
        #widget=forms.CheckboxSelectMultiple
        )
    
    color = forms.ModelMultipleChoiceField(
        label="色",
        queryset=Sitecolor.objects.all(),
        required=False,
        widget=CustomCheckboxSelectMultiple
        #widget=forms.CheckboxSelectMultiple
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


### 表示されたサイトを評価 ###
class EvalForm(forms.Form):
    eval = forms.ModelMultipleChoiceField(
        label='評価', 
        queryset=Website.objects.all(),
        widget=forms.CheckboxSelectMultiple
        )
    ### querysetを動的に変更 ###
    def __init__(self, queryset=None, *args, **kwargs):
        super(EvalForm, self).__init__(*args, **kwargs)
        if queryset:
            self.fields['eval'].queryset = queryset