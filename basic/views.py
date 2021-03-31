from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Belajar Bersama bersama sama'
        context['nama'] = "Aqil Fiqran Dzi'Ul Haq"
        return context
