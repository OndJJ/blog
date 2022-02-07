from django.views.generic import TemplateView


from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# -- HomepageView
class HomeView(TemplateView):
  template_name = 'home.html' # TemplateView를 상속 받아 사용하는경우 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해야함

#-- User Creation
class UserCreateView(CreateView):
  template_name = 'registration/register.html' 
  form_class = UserCreationForm
  success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
  template_name = 'registration/register_done.html'