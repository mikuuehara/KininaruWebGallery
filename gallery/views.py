from django.shortcuts import render, redirect
from gallery.models import Sitecategory, Sitecolor, Website
from gallery.forms import ColorForm, CategoryForm, SiteinfForm, SelectForm, EvalForm
from django.views.generic import TemplateView


### top page ###
class top(TemplateView):
    select_form_class = SelectForm
    eval_form_class = EvalForm
    template_name ='gallery/top.html'
    print("頑張れー！")

    def get(self, request):
        context = {
                'selecte_form': self.select_form_class(),
                }
        return render(request, 'gallery/top.html', context)

    def post(self, request):
        #だめだ～
        #selected_color = self.request.POST.getlist("color")
        #for a in selected_color:
        #    color_id = int(a)
        #print(color_id)
        self.eval_form_class().fields['eval'].queryset = Website.objects.filter(id=2)
        context = {
            'eval_form' : self.eval_form_class(),
            'siteinf' : Website.objects.all(),
        }
        #全然フィルターかかってないなんで～
        return render(request, 'gallery/evaluation.html', context)


#def top(request):
#    if request.method == "POST":
#        context = {
#            'color' : request.POST.getlist("color"),
#        }
#        return render(request, 'gallery/evaluation.html', context)
#
#    else:
#        context = {
#                'selecte_form': SelectForm(),
#                }
#        return render(request, 'gallery/top.html', context)




class evaluation(TemplateView):
    template_name = 'gallery/evaluation.html'

    def get(self, request):
        print("いまここですよ")
        context = {
            'siteinfs' : Website.objects.all(),
        }
        return render(request, 'gallery/evaluation.html', context)  


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

