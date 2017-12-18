from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RecordsPlaces
from ..forms import RecordsPlacesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RecordsPlacesListView(ListView):
    model = RecordsPlaces
    template_name = "Sagenkarta-Admin/records_places_list.html"
    paginate_by = 20
    context_object_name = "records_places_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RecordsPlacesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPlacesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPlacesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RecordsPlacesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RecordsPlacesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RecordsPlacesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RecordsPlacesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RecordsPlacesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RecordsPlacesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RecordsPlacesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPlacesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPlacesListView, self).get_template_names()


class RecordsPlacesDetailView(DetailView):
    model = RecordsPlaces
    template_name = "Sagenkarta-Admin/records_places_detail.html"
    context_object_name = "records_places"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RecordsPlacesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPlacesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPlacesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPlacesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPlacesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPlacesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsPlacesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPlacesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPlacesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPlacesDetailView, self).get_template_names()


class RecordsPlacesCreateView(CreateView):
    model = RecordsPlaces
    form_class = RecordsPlacesForm
    # fields = ['record', 'place']
    template_name = "Sagenkarta-Admin/records_places_create.html"
    success_url = reverse_lazy("records_places_list")

    def __init__(self, **kwargs):
        return super(RecordsPlacesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RecordsPlacesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPlacesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsPlacesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RecordsPlacesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsPlacesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsPlacesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsPlacesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsPlacesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsPlacesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsPlacesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPlacesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPlacesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_places_detail", args=(self.object.pk,))


class RecordsPlacesUpdateView(UpdateView):
    model = RecordsPlaces
    form_class = RecordsPlacesForm
    # fields = ['record', 'place']
    template_name = "Sagenkarta-Admin/records_places_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_places"

    def __init__(self, **kwargs):
        return super(RecordsPlacesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPlacesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPlacesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsPlacesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPlacesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPlacesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPlacesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RecordsPlacesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsPlacesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsPlacesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsPlacesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsPlacesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsPlacesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsPlacesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPlacesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPlacesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPlacesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_places_detail", args=(self.object.pk,))


class RecordsPlacesDeleteView(DeleteView):
    model = RecordsPlaces
    template_name = "Sagenkarta-Admin/records_places_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_places"

    def __init__(self, **kwargs):
        return super(RecordsPlacesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPlacesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RecordsPlacesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RecordsPlacesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPlacesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPlacesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPlacesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsPlacesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPlacesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPlacesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPlacesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_places_list")
