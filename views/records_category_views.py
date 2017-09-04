from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import RecordsCategory
from ..forms import RecordsCategoryForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class RecordsCategoryListView(ListView):
    model = RecordsCategory
    template_name = "sagenkarta_admin/records_category_list.html"
    paginate_by = 20
    context_object_name = "records_category_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RecordsCategoryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsCategoryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsCategoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RecordsCategoryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RecordsCategoryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RecordsCategoryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RecordsCategoryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RecordsCategoryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RecordsCategoryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RecordsCategoryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCategoryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCategoryListView, self).get_template_names()


class RecordsCategoryDetailView(DetailView):
    model = RecordsCategory
    template_name = "sagenkarta_admin/records_category_detail.html"
    context_object_name = "records_category"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RecordsCategoryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsCategoryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsCategoryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsCategoryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsCategoryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsCategoryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsCategoryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsCategoryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCategoryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCategoryDetailView, self).get_template_names()


class RecordsCategoryCreateView(CreateView):
    model = RecordsCategory
    form_class = RecordsCategoryForm
    # fields = ['record', 'category', 'level', 'type']
    template_name = "sagenkarta_admin/records_category_create.html"
    success_url = reverse_lazy("records_category_list")

    def __init__(self, **kwargs):
        return super(RecordsCategoryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RecordsCategoryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsCategoryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsCategoryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RecordsCategoryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsCategoryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsCategoryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsCategoryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsCategoryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsCategoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsCategoryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCategoryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCategoryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_category_detail", args=(self.object.pk,))


class RecordsCategoryUpdateView(UpdateView):
    model = RecordsCategory
    form_class = RecordsCategoryForm
    # fields = ['record', 'category', 'level', 'type']
    template_name = "sagenkarta_admin/records_category_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_category"

    def __init__(self, **kwargs):
        return super(RecordsCategoryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsCategoryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RecordsCategoryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RecordsCategoryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsCategoryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsCategoryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsCategoryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RecordsCategoryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RecordsCategoryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RecordsCategoryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RecordsCategoryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RecordsCategoryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RecordsCategoryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RecordsCategoryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsCategoryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCategoryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCategoryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_category_detail", args=(self.object.pk,))


class RecordsCategoryDeleteView(DeleteView):
    model = RecordsCategory
    template_name = "sagenkarta_admin/records_category_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "records_category"

    def __init__(self, **kwargs):
        return super(RecordsCategoryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RecordsCategoryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RecordsCategoryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RecordsCategoryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RecordsCategoryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RecordsCategoryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RecordsCategoryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RecordsCategoryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RecordsCategoryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RecordsCategoryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RecordsCategoryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("records_category_list")
