from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RecordsPersons
from ..forms import RecordsPersonsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RecordsPersonsListView(ListView):
    model = RecordsPersons
    template_name = "sagenkarta_admin/records_persons_list.html"
    paginate_by = 20
    context_object_name = "records_persons_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RecordsPersonsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPersonsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPersonsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RecordsPersonsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RecordsPersonsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RecordsPersonsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RecordsPersonsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RecordsPersonsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RecordsPersonsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RecordsPersonsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPersonsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPersonsListView, self).get_template_names()


class RecordsPersonsDetailView(DetailView):
    model = RecordsPersons
    template_name = "sagenkarta_admin/records_persons_detail.html"
    context_object_name = "records_persons"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RecordsPersonsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPersonsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPersonsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPersonsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPersonsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPersonsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsPersonsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPersonsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPersonsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPersonsDetailView, self).get_template_names()


class RecordsPersonsCreateView(CreateView):
    model = RecordsPersons
    form_class = RecordsPersonsForm
    # fields = ['record', 'person', 'relation']
    template_name = "sagenkarta_admin/records_persons_create.html"
    success_url = reverse_lazy("records_persons_list")

    def __init__(self, **kwargs):
        return super(RecordsPersonsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RecordsPersonsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPersonsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsPersonsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RecordsPersonsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsPersonsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsPersonsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsPersonsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsPersonsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsPersonsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsPersonsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPersonsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPersonsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_persons_detail", args=(self.object.pk,))


class RecordsPersonsUpdateView(UpdateView):
    model = RecordsPersons
    form_class = RecordsPersonsForm
    # fields = ['record', 'person', 'relation']
    template_name = "sagenkarta_admin/records_persons_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_persons"

    def __init__(self, **kwargs):
        return super(RecordsPersonsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPersonsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsPersonsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsPersonsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPersonsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPersonsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPersonsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RecordsPersonsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsPersonsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsPersonsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsPersonsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsPersonsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsPersonsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsPersonsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPersonsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPersonsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPersonsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_persons_detail", args=(self.object.pk,))


class RecordsPersonsDeleteView(DeleteView):
    model = RecordsPersons
    template_name = "sagenkarta_admin/records_persons_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_persons"

    def __init__(self, **kwargs):
        return super(RecordsPersonsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsPersonsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RecordsPersonsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RecordsPersonsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsPersonsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsPersonsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsPersonsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsPersonsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsPersonsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsPersonsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsPersonsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_persons_list")
