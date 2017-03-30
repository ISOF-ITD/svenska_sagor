from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Persons
from ..forms import PersonsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class PersonsListView(ListView):
    model = Persons
    template_name = "svenska_sagner/persons_list.html"
    paginate_by = 20
    context_object_name = "persons_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PersonsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PersonsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PersonsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PersonsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PersonsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PersonsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PersonsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PersonsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsListView, self).get_template_names()


class PersonsDetailView(DetailView):
    model = Persons
    template_name = "svenska_sagner/persons_detail.html"
    context_object_name = "persons"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PersonsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsDetailView, self).get_template_names()


class PersonsCreateView(CreateView):
    model = Persons
    form_class = PersonsForm
    # fields = ['firstname', 'surname', 'gender', 'birth_year', 'address', 'biography', 'image', 'changedate']
    template_name = "svenska_sagner/persons_create.html"
    success_url = reverse_lazy("persons_list")

    def __init__(self, **kwargs):
        return super(PersonsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PersonsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PersonsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PersonsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_detail", args=(self.object.pk,))


class PersonsUpdateView(UpdateView):
    model = Persons
    form_class = PersonsForm
    # fields = ['firstname', 'surname', 'gender', 'birth_year', 'address', 'biography', 'image', 'changedate']
    template_name = "svenska_sagner/persons_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "persons"

    def __init__(self, **kwargs):
        return super(PersonsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PersonsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PersonsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PersonsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PersonsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PersonsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PersonsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PersonsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PersonsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PersonsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_detail", args=(self.object.pk,))


class PersonsDeleteView(DeleteView):
    model = Persons
    template_name = "svenska_sagner/persons_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "persons"

    def __init__(self, **kwargs):
        return super(PersonsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PersonsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PersonsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PersonsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PersonsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PersonsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PersonsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PersonsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PersonsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PersonsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PersonsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("persons_list")
