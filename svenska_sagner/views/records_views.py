from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Records
from ..forms import RecordsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RecordsListView(ListView):
    model = Records
    template_name = "svenska_sagner/records_list.html"
    paginate_by = 20
    context_object_name = "records_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RecordsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RecordsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RecordsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RecordsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RecordsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RecordsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RecordsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RecordsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsListView, self).get_template_names()


class RecordsDetailView(DetailView):
    model = Records
    template_name = "svenska_sagner/records_detail.html"
    context_object_name = "records"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RecordsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsDetailView, self).get_template_names()


class RecordsCreateView(CreateView):
    model = Records
    form_class = RecordsForm
    # fields = ['title', 'text', 'year', 'category', 'archive', 'archive_id', 'type', 'archive_page', 'source', 'comment', 'informant_name', 'changedate']
    template_name = "svenska_sagner/records_create.html"
    success_url = reverse_lazy("records_list")

    def __init__(self, **kwargs):
        return super(RecordsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RecordsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RecordsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_detail", args=(self.object.pk,))


class RecordsUpdateView(UpdateView):
    model = Records
    form_class = RecordsForm
    # fields = ['title', 'text', 'year', 'category', 'archive', 'archive_id', 'type', 'archive_page', 'source', 'comment', 'informant_name', 'changedate']
    template_name = "svenska_sagner/records_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records"

    def __init__(self, **kwargs):
        return super(RecordsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RecordsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_detail", args=(self.object.pk,))


class RecordsDeleteView(DeleteView):
    model = Records
    template_name = "svenska_sagner/records_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records"

    def __init__(self, **kwargs):
        return super(RecordsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RecordsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RecordsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_list")
