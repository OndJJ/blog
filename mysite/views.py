from django.views.generic import TemplateView

# -- templateView
class HomeView(TemplateView):
  template_name = 'home.html'