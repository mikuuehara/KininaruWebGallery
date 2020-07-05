from django.shortcuts import render, redirect
from django import forms
from gallery.models import Sitecategory, Sitecolor, Website
from gallery.forms import ColorForm, CategoryForm, SiteinfForm, SelectForm, EvalForm
from django.views.generic import TemplateView
from gallery.widgets import CustomCheckboxSelectMultiple, CustomCheckboxSelectMultiple2



### top page ###
class top(TemplateView):
    select_form_class = SelectForm
    eval_form_class = EvalForm
    template_name ='gallery/top.html'
    print("頑張れー！")

    def get(self, request):
        context = {
                'select_form': self.select_form_class(),
                }
        return render(request, 'gallery/top.html', context)

    def post(self, request):
        ### 未選択のオブジェクトが取得できそうに無かったのでformを変えてみる ###
        if 'select' in self.request.POST: 
            ### 選ばれた色をリストとして取り出す ###
            selected_color_id_list = self.request.POST.getlist("color")

            ### 選ばれたカテゴリをリストとして取り出す ###
            selected_category_id_list = self.request.POST.getlist("category")

            ### Websiteオブジェクトにフィルターかける ###
            if selected_color_id_list == []:
                if selected_category_id_list == []:
                    filter1 = Website.objects.all()
                else:
                    filter1 = Website.objects.filter(category__in = selected_category_id_list)
            else:
                if selected_category_id_list == []:
                    filter1 = Website.objects.filter(color__in = selected_color_id_list)
                else:
                    filter1 = Website.objects.filter(color__in = selected_color_id_list, category__in = selected_category_id_list)

            selected_site_list = filter1.values_list('name', flat=True)
            ### formにフィールドを追加 ###
            good_bad = (
                ('good', 'good'),
                ('bad', 'bad')
            )
            eval_form = forms.Form()
            for selected_site_name in list(selected_site_list): 
                eval_form.fields[selected_site_name] = forms.ChoiceField(
                    choices = good_bad,
                    required=True,
                    widget=CustomCheckboxSelectMultiple2
                )

            context = {
                'eval_form' : eval_form,
                'siteinfs' : filter1,
            }
            return render(request, 'gallery/evaluation.html', context)
        
        ### posted evalform ###
        if 'eval' in self.request.POST:
            ### なぜかリストの最後に '' が入っているからそれを除く ###
            #eval_list = []
            #for a in (self.request.POST.getlist("eval")):
            #    if a != '':
            #        eval_list.append(a)
            #eval_result = Website.objects.filter(id__in = eval_list)
            #context = {
            #    'selected_siteinfs' : eval_result
            #}

            print(self.request.POST)
            return render(request, 'gallery/result.html')  




class evaluation(TemplateView):
    template_name = 'gallery/evaluation.html'
    
    def post(self, request):
        print("いまevaluationページです")
        print(self.request.POST.getlist("eval"))
        context = {
            'siteinfs' : self.request.POST.getlist("eval")
        }
        return render(request, 'gallery/result.html', context)  


class result(TemplateView):
    template_name = 'gallery/result.html'

    def get(self, request):
        return render(request, 'gallery/result.html')


### management page ###
class register(TemplateView):
    color_form_class = ColorForm
    category_form_class = CategoryForm
    siteinf_form_class = SiteinfForm
    template_name = 'gallery/management.html'


    ### when fitst acsessed ###
    def get(self, request):
        # return empty fields #
        print(self.siteinf_form_class())
        context = {
                'siteinf_form': self.siteinf_form_class(),
                'color_form': self.color_form_class(),
                'category_form': self.category_form_class(),
                }
        return render(self.request, 'gallery/management.html', context)

    ### when posted ###
    def post(self, request):
        color_form = self.color_form_class(request.POST)
        category_form = self.category_form_class(request.POST)
        siteinf_form = self.siteinf_form_class(request.POST, request.FILES or None)
        context = self.get_context_data(color_form=color_form,
                                        category_form=category_form,
                                        siteinf_form=siteinf_form)

        ### posted website information ###
        if 'siteinf' in self.request.POST:
            if siteinf_form.is_valid():
                self.form_save(siteinf_form)
                # return empty fields & message #
                context = {
                    'siteinf_form': self.siteinf_form_class(),
                    'color_form': self.color_form_class(),
                    'category_form': self.category_form_class(),
                    'message_siteinf': "サイト情報を登録しました",
                    }
                return render(self.request, 'gallery/management.html', context)

        ### posted color ###
        elif 'color' in self.request.POST:
            if color_form.is_valid():
                self.form_save(color_form)
                # return empty fields & message #
                context = {
                    'siteinf_form': self.siteinf_form_class(),
                    'color_form': self.color_form_class(),
                    'category_form': self.category_form_class(),
                    'message_color': "色を登録しました",
                    }
                return render(self.request, 'gallery/management.html', context)

        ### posted category ###
        elif 'category' in self.request.POST:
            if category_form.is_valid():
                self.form_save(category_form)
                # return empty fields & message #
                context = {
                    'siteinf_form': self.siteinf_form_class(),
                    'color_form': self.color_form_class(),
                    'category_form': self.category_form_class(),
                    'message_category': "カテゴリを登録しました",
                    }
                return render(self.request, 'gallery/management.html', context)
        

           
        return render(self.request, 'gallery/management.html', context)

    ### save the form information ###
    def form_save(self, form):
        obj = form.save()
        return obj

