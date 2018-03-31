from django.views.generic import ListView, DetailView
from .models import City


class CityListView1(ListView):
    template_name = "list1.html"
    model = City
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CityListView2(ListView):
    template_name = "list2.html"
    model = City
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CityDetailView(DetailView):
    template_name = "detail.html"
    model = City

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context