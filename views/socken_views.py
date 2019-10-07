from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Socken
from ..forms import SockenForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class SockenListView(ListView):
    model = Socken
    template_name = "Sagenkarta-Admin/socken_list.html"
    paginate_by = 20
    context_object_name = "socken_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(SockenListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(SockenListView, self).get_queryset()

    def get_allow_empty(self):
        return super(SockenListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(SockenListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(SockenListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(SockenListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(SockenListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(SockenListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenListView, self).get_template_names()


class SockenDetailView(DetailView):
    model = Socken
    template_name = "Sagenkarta-Admin/socken_detail.html"
    context_object_name = "socken"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(SockenDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SockenDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenDetailView, self).get_template_names()


class SockenCreateView(CreateView):
    model = Socken
    form_class = SockenForm
    # fields = ['name', 'harad', 'lat', 'lng', 'sweref99_n', 'sweref99_e', 'changedate']
    template_name = "Sagenkarta-Admin/socken_create.html"
    success_url = reverse_lazy("socken_list")

    def __init__(self, **kwargs):
        return super(SockenCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(SockenCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SockenCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(SockenCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SockenCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SockenCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SockenCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(SockenCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SockenCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SockenCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(SockenCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_detail", args=(self.object.pk,))


class SockenUpdateView(UpdateView):
    model = Socken
    form_class = SockenForm
    # fields = ['name', 'harad', 'lat', 'lng', 'sweref99_n', 'sweref99_e', 'changedate']
    template_name = "Sagenkarta-Admin/socken_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "socken"

    def __init__(self, **kwargs):
        return super(SockenUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(SockenUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SockenUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(SockenUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(SockenUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(SockenUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(SockenUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(SockenUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(SockenUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SockenUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_detail", args=(self.object.pk,))


class SockenDeleteView(DeleteView):
    model = Socken
    template_name = "Sagenkarta-Admin/socken_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "socken"

    def __init__(self, **kwargs):
        return super(SockenDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(SockenDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(SockenDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(SockenDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(SockenDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(SockenDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(SockenDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(SockenDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(SockenDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(SockenDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(SockenDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("socken_list")
