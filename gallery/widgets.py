from django import forms

### top.html用 ###
class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'gallery/widgets/custom_checkbox.html'
    option_template_name = 'gallery/widgets/custom_checkbox_option.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += 'custom-checkbox'
        else:
            self.attrs['class'] = 'custom-checkbox'


### evaluation.html用 ###
class CustomCheckboxSelectMultiple2(forms.CheckboxSelectMultiple):
    template_name = 'gallery/widgets/custom_checkbox_2.html'
    option_template_name = 'gallery/widgets/custom_checkbox_option_2.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += 'custom-checkbox'
        else:
            self.attrs['class'] = 'custom-checkbox'