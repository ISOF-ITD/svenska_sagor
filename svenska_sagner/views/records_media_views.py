from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RecordsMedia
from ..forms import RecordsMediaForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RecordsMediaListView(ListView):
    model = RecordsMedia
    template_name = "svenska_sagner/records_media_list.html"
    paginate_by = 20
    context_object_name = "records_media_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RecordsMediaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsMediaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsMediaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RecordsMediaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RecordsMediaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RecordsMediaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RecordsMediaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RecordsMediaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RecordsMediaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RecordsMediaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsMediaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsMediaListView, self).get_template_names()


class RecordsMediaDetailView(DetailView):
    model = RecordsMedia
    template_name = "svenska_sagner/records_media_detail.html"
    context_object_name = "records_media"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RecordsMediaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsMediaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsMediaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsMediaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsMediaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsMediaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsMediaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsMediaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsMediaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsMediaDetailView, self).get_template_names()


class RecordsMediaCreateView(CreateView):
    model = RecordsMedia
    form_class = RecordsMediaForm
    # fields = ['record', 'media']
    template_name = "svenska_sagner/records_media_create.html"
    success_url = reverse_lazy("records_media_list")

    def __init__(self, **kwargs):
        return super(RecordsMediaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RecordsMediaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsMediaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsMediaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RecordsMediaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsMediaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsMediaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsMediaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsMediaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsMediaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsMediaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsMediaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsMediaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_media_detail", args=(self.object.pk,))


class RecordsMediaUpdateView(UpdateView):
    model = RecordsMedia
    form_class = RecordsMediaForm
    # fields = ['record', 'media']
    template_name = "svenska_sagner/records_media_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_media"

    def __init__(self, **kwargs):
        return super(RecordsMediaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsMediaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsMediaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsMediaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsMediaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsMediaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsMediaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RecordsMediaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsMediaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsMediaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsMediaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsMediaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsMediaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsMediaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsMediaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsMediaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsMediaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_media_detail", args=(self.object.pk,))


class RecordsMediaDeleteView(DeleteView):
    model = RecordsMedia
    template_name = "svenska_sagner/records_media_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_media"

    def __init__(self, **kwargs):
        return super(RecordsMediaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsMediaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RecordsMediaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RecordsMediaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsMediaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsMediaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsMediaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsMediaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsMediaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsMediaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsMediaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_media_list")
