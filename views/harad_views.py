from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Harad
from ..forms import HaradForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class HaradListView(ListView):
    model = Harad
    template_name = "Sagenkarta-Admin/harad_list.html"
    paginate_by = 20
    context_object_name = "harad_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HaradListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HaradListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HaradListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HaradListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HaradListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HaradListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HaradListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HaradListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HaradListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HaradListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HaradListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HaradListView, self).get_template_names()


class HaradDetailView(DetailView):
    model = Harad
    template_name = "Sagenkarta-Admin/harad_detail.html"
    context_object_name = "harad"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(HaradDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HaradDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HaradDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HaradDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(HaradDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(HaradDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HaradDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HaradDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HaradDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HaradDetailView, self).get_template_names()


class HaradCreateView(CreateView):
    model = Harad
    form_class = HaradForm
    # fields = ['name', 'lan', 'landskap', 'country']
    template_name = "Sagenkarta-Admin/harad_create.html"
    success_url = reverse_lazy("harad_list")

    def __init__(self, **kwargs):
        return super(HaradCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(HaradCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HaradCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HaradCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(HaradCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HaradCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HaradCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HaradCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(HaradCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HaradCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HaradCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(HaradCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HaradCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("harad_detail", args=(self.object.pk,))


class HaradUpdateView(UpdateView):
    model = Harad
    form_class = HaradForm
    # fields = ['name', 'lan', 'landskap', 'country']
    template_name = "Sagenkarta-Admin/harad_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "harad"

    def __init__(self, **kwargs):
        return super(HaradUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HaradUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HaradUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HaradUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HaradUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(HaradUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(HaradUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(HaradUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(HaradUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(HaradUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(HaradUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(HaradUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HaradUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HaradUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HaradUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HaradUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HaradUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("harad_detail", args=(self.object.pk,))


class HaradDeleteView(DeleteView):
    model = Harad
    template_name = "Sagenkarta-Admin/harad_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "harad"

    def __init__(self, **kwargs):
        return super(HaradDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HaradDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HaradDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HaradDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(HaradDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(HaradDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(HaradDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(HaradDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(HaradDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(HaradDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HaradDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("harad_list")
