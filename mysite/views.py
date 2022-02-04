from django.views.generic import TemplateView

# -- templateView
class HomeView(TemplateView):
  template_name = 'home.html' # TemplateView를 상속 받아 사용하는경우 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해야함