from django.views.generic import View, TemplateView, RedirectView, DetailView, ListView, FormView


#-- 최상위 View를 상속 받아 직접 로직을 작성해 사용 할 수 있다.
class TestView(View):

  def get(self, request, *args, **kwargs):
    return HttpResponse('Hello, World!')


#-- 단순히 템플릿을 보여주는 template view
class HomeView(TemplateView):
  template_name = 'home.html'


#-- 주어진 URL로 리다이렉트 시켜주는 제너릭 뷰 URL 속성 필수
class TestRedirectView(RedirectView):
  url = '/blog/post/'
#url 대신 패턴 명을 지정해도 된다.  
#pattern_name ='blog:post_list'

#-- 특정 객체 하나에 대한 정보를 보여주는 DetailView
class PostDV(DetailView):
  model = Post


#-- 여러 객체의 리스트를 보여주는 ListView
class PostLV(ListView):
  model = Post



#-- 폼을 보여주기 위한 제네릭 뷰 FormView, form_class와 폼을 렌더링하는 template_name, success_url 속성 등
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context) # No Redirection



