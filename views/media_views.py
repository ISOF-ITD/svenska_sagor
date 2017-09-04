from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Media
from ..forms import MediaForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class MediaListView(ListView):
    model = Media
    template_name = "sagenkarta_admin/media_list.html"
    paginate_by = 20
    context_object_name = "media_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(MediaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MediaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MediaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(MediaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(MediaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(MediaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(MediaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(MediaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(MediaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(MediaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(MediaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MediaListView, self).get_template_names()


class MediaDetailView(DetailView):
    model = Media
    template_name = "sagenkarta_admin/media_detail.html"
    context_object_name = "media"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(MediaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MediaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MediaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MediaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(MediaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(MediaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MediaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MediaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MediaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MediaDetailView, self).get_template_names()


class MediaCreateView(CreateView):
    model = Media
    form_class = MediaForm
    # fields = ['source', 'type']
    template_name = "sagenkarta_admin/media_create.html"
    success_url = reverse_lazy("media_list")

    def __init__(self, **kwargs):
        return super(MediaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(MediaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MediaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MediaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(MediaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MediaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MediaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MediaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(MediaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MediaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MediaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(MediaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MediaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("media_detail", args=(self.object.pk,))


class MediaUpdateView(UpdateView):
    model = Media
    form_class = MediaForm
    # fields = ['source', 'type']
    template_name = "sagenkarta_admin/media_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "media"

    def __init__(self, **kwargs):
        return super(MediaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MediaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MediaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MediaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MediaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(MediaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(MediaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(MediaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MediaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MediaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MediaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(MediaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MediaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MediaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MediaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MediaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MediaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("media_detail", args=(self.object.pk,))


class MediaDeleteView(DeleteView):
    model = Media
    template_name = "sagenkarta_admin/media_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "media"

    def __init__(self, **kwargs):
        return super(MediaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MediaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(MediaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(MediaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MediaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(MediaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(MediaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MediaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MediaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MediaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MediaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("media_list")
