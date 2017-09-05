from django.contrib import admin
from .models import CategoriesKlintberg, RecordsPlaces, Records, Media, RecordsCategory, Persons, RecordsPersons, PersonsPlaces, SockenV1, RecordsMedia, Socken, Categories, Harad
from django_baker.admin import ExtendedModelAdminMixin


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
    model = Records.persons.through
    model._meta.verbose_name_plural = "Relaterade personer"


class RecordsPlacesInline(admin.TabularInline):
    model = Records.places.through
    model._meta.verbose_name_plural = "Platser"


class RecordsMediaInline(admin.TabularInline):
    model = Records.media.through
    model._meta.verbose_name_plural = "Filer"


class RecordsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'archive', 'category', 'type']
    extra_list_display = []
    extra_list_filter = ['type', 'category']
    extra_search_fields = []
    list_editable = ['title', 'archive', 'category', 'type']
    raw_id_fields = ['media', 'persons']
    inlines = [RecordsPersonsInline, RecordsPlacesInline]
    filter_vertical = ['persons']
    filter_horizontal = []
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ['id']
    fields = ['title', ('category', 'type'), ('archive', 'year'), ('archive_page', 'archive_id'), 'text', 'source', 'comment']

    def get_form(self, request, obj=None, **kwargs):
        form = super(RecordsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['text'].widget.attrs['style'] = 'height: 500px;'
        return form


class MediaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
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
    extra_list_filter = []
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
