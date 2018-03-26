from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Categories
from ..forms import CategoriesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CategoriesListView(ListView):
    model = Categories
    template_name = "Sagenkarta-Admin/categories_list.html"
    paginate_by = 20
    context_object_name = "categories_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CategoriesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CategoriesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CategoriesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CategoriesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CategoriesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CategoriesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CategoriesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CategoriesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesListView, self).get_template_names()


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = "Sagenkarta-Admin/categories_detail.html"
    context_object_name = "categories"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CategoriesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoriesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesDetailView, self).get_template_names()


class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    # fields = ['name', 'name_en']
    template_name = "Sagenkarta-Admin/categories_create.html"
    success_url = reverse_lazy("categories_list")

    def __init__(self, **kwargs):
        return super(CategoriesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoriesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CategoriesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CategoriesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoriesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoriesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoriesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoriesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoriesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_detail", args=(self.object.pk,))


class CategoriesUpdateView(UpdateView):
    model = Categories
    form_class = CategoriesForm
    # fields = ['name', 'name_en']
    template_name = "Sagenkarta-Admin/categories_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "categories"

    def __init__(self, **kwargs):
        return super(CategoriesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoriesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CategoriesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CategoriesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoriesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoriesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoriesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoriesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoriesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_detail", args=(self.object.pk,))


class CategoriesDeleteView(DeleteView):
    model = Categories
    template_name = "Sagenkarta-Admin/categories_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "categories"

    def __init__(self, **kwargs):
        return super(CategoriesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CategoriesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CategoriesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoriesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_list")
