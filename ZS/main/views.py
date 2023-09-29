from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.core.paginator import Paginator


from .forms import CatsModelForm
from .models import Cats

# @login_required
def index(request):
    cats = Cats.objects.all()
    my_queryset = Cats.objects.all()
    paginator = Paginator(my_queryset, 2)  # показывать 25 объектов на странице
    page = request.GET.get('page')  # получить текущую страницу из параметров URL
    my_objects = paginator.get_page(page)
    return render(request, 'index.html', {"cats":cats,'my_objects': my_objects})


def post_proc(request):
    form = CatsModelForm()
    return render(request, 'index.html', {'form': form})


class CatsDetailView(DetailView):
    model = Cats
    template_name = 'cats.html'
    context_object_name = 'cats'

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ['admin.html']
        else:
            return ['cats.html']


class CatsListView(ListView):
    model = Cats
    template_name = 'index.html'
    context_object_name = 'cats'
    paginate_by = 1
# Create your views here.

from django.views.generic.detail import SingleObjectMixin,SingleObjectTemplateResponseMixin
from django.shortcuts import get_object_or_404
from .models import Cats  # Импортируйте вашу модель Cats

class MyDetailView(SingleObjectMixin,SingleObjectTemplateResponseMixin, TemplateView):
    model = Cats
    template_name = 'admin.html'
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        object = get_object_or_404(Cats, pk=pk)
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        context['cats'] = Cats.objects.all()
        return context

    def get_template_names(self):
        if self.request.user.is_superuser:
            return ['admin.html']
        else:
            return ['cats.html']

