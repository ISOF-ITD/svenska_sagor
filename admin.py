from django.contrib import admin
from .models import CategoriesKlintberg, RecordsPlaces, Records, Media, RecordsCategory, Persons, RecordsPersons, PersonsPlaces, SockenV1, RecordsMedia, Socken, Categories, Harad, RecordsMetadata
from django_baker.admin import ExtendedModelAdminMixin
from .filters import DropdownFilter, RelatedDropdownFilter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

import sys

class CategoriesKlintbergAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class RecordsPlacesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}        


class RecordsPersonsInline(admin.TabularInline):
    model = Records.person_objects.through
    model._meta.verbose_name_plural = "Relaterade personer"


class RecordsPlacesInline(admin.TabularInline):
    model = Records.places.through
    model._meta.verbose_name_plural = "Platser"


class RecordsMediaInline(admin.TabularInline):
    model = Records.media_objects.through
    model._meta.verbose_name_plural = "Filer"


class RecordsMetadataInline(admin.TabularInline):
    model = RecordsMetadata


class RecordsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'archive', 'category', 'type', 'country']
    extra_list_display = []
#    list_filter = (('places', DropdownFilter),)
    extra_list_filter = ['type', ('archive', DropdownFilter), ('category', DropdownFilter), ('places', RelatedDropdownFilter), 'country']
    extra_search_fields = []
    list_editable = ['title', 'archive', 'category', 'type']
    raw_id_fields = ['media_objects', 'person_objects']
    inlines = [RecordsPersonsInline, RecordsPlacesInline, RecordsMetadataInline]
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']
    fields = ['title', ('category', 'type'), ('archive', 'year'), ('archive_page', 'archive_id'), 'text', 'source', 'comment','country']

    def get_model_perms(self, request):
        return {
            'add': self.has_add_permission(request),
            'change': self.has_change_permission(request),
            'delete': self.has_delete_permission(request),
        }

    def get_queryset(self, request):
        qs = super(RecordsAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='Norge').exists():
            return qs.filter(country='norway')
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super(RecordsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['text'].widget.attrs['style'] = 'height: 500px;'
        return form


class MediaRecordsInline(admin.TabularInline):
    model = Media.record_objects.through
    model._meta.verbose_name_plural = "Sägner"


class MediaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'source', 'type']
    extra_list_display = []
    extra_list_filter = ['type']
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id', 'image_tag']
    fields = ['source', 'type', 'image_tag']

    def get_queryset(self, request):
        qs = super(MediaAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='Norge').exists():
            inner_qs = Records.objects.filter(country='norway')
            return qs.filter(record_objects__in=inner_qs)
        return qs


class RecordsCategoryAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class PersonsPlacesInline(admin.TabularInline):
    model = Persons.places.through
    model._meta.verbose_name_plural = "Filer"


class PersonsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'birth_year']
    extra_list_display = []
    extra_list_filter = ['record_objects__country']
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = [PersonsPlacesInline]
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']
    readonly_fields = ['id', 'image_tag']
    fields = ['id', 'name', ('gender', 'birth_year'), 'address', 'biography', ('image', 'image_tag')]

    def lookup_allowed(self, lookup, value):
        if lookup == 'record_objects__country':
            return True
        return super(PersonsAdmin, self).lookup_allowed(lookup, value)

    def get_queryset(self, request):
        qs = super(PersonsAdmin, self).get_queryset(request)
        if request.user.groups.filter(name='Norge').exists():
            inner_qs = Records.objects.filter(country='norway')
            return qs.filter(record_objects__in=inner_qs)
        return qs


class RecordsPersonsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class PersonsPlacesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class SockenV1Admin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class RecordsMediaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']

    def get_model_perms(self, request):
        return {}


class SockenAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'harad']
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    fields = ['name', 'harad', 'lat', 'lng', 'map_tag', 'id']
    readonly_fields = ['id', 'map_tag']


class CategoriesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']


class HaradAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    extra_list_display = []
    extra_list_filter = []
    extra_search_fields = []
    list_editable = []
    raw_id_fields = []
    inlines = []
    filter_vertical = []
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']


class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        if request.user.groups.filter(name='Norge').exists():
            return User.objects.filter(id=request.user.id)
        return User.objects.all()


class CustomGroupAdmin(GroupAdmin):
    def get_queryset(self, request):
        if request.user.groups.filter(name='Norge').exists():
            return;
        return User.objects.all()


admin.site.register(CategoriesKlintberg, CategoriesKlintbergAdmin)
admin.site.register(RecordsPlaces, RecordsPlacesAdmin)
admin.site.register(Records, RecordsAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(RecordsCategory, RecordsCategoryAdmin)
admin.site.register(Persons, PersonsAdmin)
admin.site.register(RecordsPersons, RecordsPersonsAdmin)
admin.site.register(PersonsPlaces, PersonsPlacesAdmin)
admin.site.register(SockenV1, SockenV1Admin)
admin.site.register(RecordsMedia, RecordsMediaAdmin)
admin.site.register(Socken, SockenAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Harad, HaradAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)