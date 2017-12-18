from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import PersonsPlaces
from ..forms import PersonsPlacesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PersonsPlacesListView(ListView):
    model = PersonsPlaces
    template_name = "Sagenkarta-Admin/persons_places_list.html"
    paginate_by = 20
    context_object_name = "persons_places_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PersonsPlacesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsPlacesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsPlacesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PersonsPlacesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PersonsPlacesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PersonsPlacesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PersonsPlacesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PersonsPlacesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PersonsPlacesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PersonsPlacesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsPlacesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsPlacesListView, self).get_template_names()


class PersonsPlacesDetailView(DetailView):
    model = PersonsPlaces
    template_name = "Sagenkarta-Admin/persons_places_detail.html"
    context_object_name = "persons_places"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PersonsPlacesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsPlacesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsPlacesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsPlacesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsPlacesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsPlacesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonsPlacesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsPlacesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsPlacesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsPlacesDetailView, self).get_template_names()


class PersonsPlacesCreateView(CreateView):
    model = PersonsPlaces
    form_class = PersonsPlacesForm
    # fields = ['person', 'place', 'relation']
    template_name = "Sagenkarta-Admin/persons_places_create.html"
    success_url = reverse_lazy("persons_places_list")

    def __init__(self, **kwargs):
        return super(PersonsPlacesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PersonsPlacesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsPlacesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonsPlacesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PersonsPlacesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PersonsPlacesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonsPlacesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonsPlacesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonsPlacesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonsPlacesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonsPlacesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsPlacesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsPlacesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_places_detail", args=(self.object.pk,))


class PersonsPlacesUpdateView(UpdateView):
    model = PersonsPlaces
    form_class = PersonsPlacesForm
    # fields = ['person', 'place', 'relation']
    template_name = "Sagenkarta-Admin/persons_places_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "persons_places"

    def __init__(self, **kwargs):
        return super(PersonsPlacesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsPlacesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsPlacesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonsPlacesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsPlacesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsPlacesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsPlacesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PersonsPlacesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PersonsPlacesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonsPlacesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonsPlacesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonsPlacesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonsPlacesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonsPlacesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsPlacesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsPlacesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsPlacesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_places_detail", args=(self.object.pk,))


class PersonsPlacesDeleteView(DeleteView):
    model = PersonsPlaces
    template_name = "Sagenkarta-Admin/persons_places_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "persons_places"

    def __init__(self, **kwargs):
        return super(PersonsPlacesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsPlacesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PersonsPlacesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PersonsPlacesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsPlacesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsPlacesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsPlacesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonsPlacesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsPlacesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsPlacesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsPlacesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_places_list")
