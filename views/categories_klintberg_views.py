from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CategoriesKlintberg
from ..forms import CategoriesKlintbergForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class CategoriesKlintbergListView(ListView):
    model = CategoriesKlintberg
    template_name = "sagenkarta_admin/categories_klintberg_list.html"
    paginate_by = 20
    context_object_name = "categories_klintberg_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CategoriesKlintbergListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesKlintbergListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesKlintbergListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CategoriesKlintbergListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CategoriesKlintbergListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CategoriesKlintbergListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CategoriesKlintbergListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CategoriesKlintbergListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CategoriesKlintbergListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CategoriesKlintbergListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesKlintbergListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesKlintbergListView, self).get_template_names()


class CategoriesKlintbergDetailView(DetailView):
    model = CategoriesKlintberg
    template_name = "sagenkarta_admin/categories_klintberg_detail.html"
    context_object_name = "categories_klintberg"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CategoriesKlintbergDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesKlintbergDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesKlintbergDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesKlintbergDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesKlintbergDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesKlintbergDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoriesKlintbergDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesKlintbergDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesKlintbergDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesKlintbergDetailView, self).get_template_names()


class CategoriesKlintbergCreateView(CreateView):
    model = CategoriesKlintberg
    form_class = CategoriesKlintbergForm
    # fields = ['name', 'name_en', 'level']
    template_name = "sagenkarta_admin/categories_klintberg_create.html"
    success_url = reverse_lazy("categories_klintberg_list")

    def __init__(self, **kwargs):
        return super(CategoriesKlintbergCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesKlintbergCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesKlintbergCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoriesKlintbergCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CategoriesKlintbergCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CategoriesKlintbergCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoriesKlintbergCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoriesKlintbergCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoriesKlintbergCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoriesKlintbergCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoriesKlintbergCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesKlintbergCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesKlintbergCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_klintberg_detail", args=(self.object.pk,))


class CategoriesKlintbergUpdateView(UpdateView):
    model = CategoriesKlintberg
    form_class = CategoriesKlintbergForm
    # fields = ['name', 'name_en', 'level']
    template_name = "sagenkarta_admin/categories_klintberg_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "categories_klintberg"

    def __init__(self, **kwargs):
        return super(CategoriesKlintbergUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesKlintbergUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CategoriesKlintbergUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CategoriesKlintbergUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesKlintbergUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesKlintbergUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesKlintbergUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CategoriesKlintbergUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CategoriesKlintbergUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CategoriesKlintbergUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CategoriesKlintbergUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CategoriesKlintbergUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CategoriesKlintbergUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CategoriesKlintbergUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesKlintbergUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesKlintbergUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesKlintbergUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_klintberg_detail", args=(self.object.pk,))


class CategoriesKlintbergDeleteView(DeleteView):
    model = CategoriesKlintberg
    template_name = "sagenkarta_admin/categories_klintberg_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "categories_klintberg"

    def __init__(self, **kwargs):
        return super(CategoriesKlintbergDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CategoriesKlintbergDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CategoriesKlintbergDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CategoriesKlintbergDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CategoriesKlintbergDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CategoriesKlintbergDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CategoriesKlintbergDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CategoriesKlintbergDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CategoriesKlintbergDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CategoriesKlintbergDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CategoriesKlintbergDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("categories_klintberg_list")
