from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import SockenV1
from ..forms import SockenV1Form
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class SockenV1ListView(ListView):
    model = SockenV1
    template_name = "Sagenkarta-Admin/socken_v1_list.html"
    paginate_by = 20
    context_object_name = "socken_v1_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SockenV1ListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenV1ListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenV1ListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SockenV1ListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SockenV1ListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SockenV1ListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SockenV1ListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SockenV1ListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SockenV1ListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SockenV1ListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenV1ListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenV1ListView, self).get_template_names()


class SockenV1DetailView(DetailView):
    model = SockenV1
    template_name = "Sagenkarta-Admin/socken_v1_detail.html"
    context_object_name = "socken_v1"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SockenV1DetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenV1DetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenV1DetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenV1DetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenV1DetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenV1DetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SockenV1DetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenV1DetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenV1DetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenV1DetailView, self).get_template_names()


class SockenV1CreateView(CreateView):
    model = SockenV1
    form_class = SockenV1Form
    # fields = ['name', 'harad', 'lat', 'lng', 'changedate']
    template_name = "Sagenkarta-Admin/socken_v1_create.html"
    success_url = reverse_lazy("socken_v1_list")

    def __init__(self, **kwargs):
        return super(SockenV1CreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SockenV1CreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenV1CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SockenV1CreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SockenV1CreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SockenV1CreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SockenV1CreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SockenV1CreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SockenV1CreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SockenV1CreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SockenV1CreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SockenV1CreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenV1CreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_v1_detail", args=(self.object.pk,))


class SockenV1UpdateView(UpdateView):
    model = SockenV1
    form_class = SockenV1Form
    # fields = ['name', 'harad', 'lat', 'lng', 'changedate']
    template_name = "Sagenkarta-Admin/socken_v1_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "socken_v1"

    def __init__(self, **kwargs):
        return super(SockenV1UpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenV1UpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenV1UpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SockenV1UpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenV1UpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenV1UpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenV1UpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SockenV1UpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SockenV1UpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SockenV1UpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SockenV1UpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SockenV1UpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SockenV1UpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SockenV1UpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenV1UpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenV1UpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenV1UpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_v1_detail", args=(self.object.pk,))


class SockenV1DeleteView(DeleteView):
    model = SockenV1
    template_name = "Sagenkarta-Admin/socken_v1_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "socken_v1"

    def __init__(self, **kwargs):
        return super(SockenV1DeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenV1DeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SockenV1DeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SockenV1DeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenV1DeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenV1DeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenV1DeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SockenV1DeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenV1DeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenV1DeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenV1DeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_v1_list")
