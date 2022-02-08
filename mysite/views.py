from django.views.generic import TemplateView


from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin #--> 뷰 처리 진입 단계에서 적절한 권한을 소유했는지 판별할 때 사용 하는 믹스인 클래스

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

class OwnerOnlyMixin(AccessMixin):
  raise_exception = True
  permission_denied_messgae = "Owner Only can update/delete the object"

  def dispatch(self, request, *args, **kwargs):
    obj = self.get_object()
    if request.user != obj.owner:
      return self.handle_no_permission
    return super().dispatch(request, *args, **kwargs)