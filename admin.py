from django.contrib import admin
from .models import CategoriesKlintberg, RecordsPlaces, Records, MetadataTypes, RecordsCategory, Persons, CrowdSourceMedia, RecordsPersons, PersonsPlaces, SockenV1, RecordsMedia, Socken, Categories, Harad, RecordsMetadata, CrowdSourceRecords, CrowdSourceUsers
from django_baker.admin import ExtendedModelAdminMixin
from .filters import DropdownFilter, RelatedDropdownFilter
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin

import sys
import time

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
	extra_search_fields = ['id']
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
	raw_id_fields = ['person']
	model._meta.verbose_name_plural = "Relaterade personer"


class RecordsPlacesInline(admin.TabularInline):
	model = Records.places.through
	raw_id_fields = ['place']
	model._meta.verbose_name_plural = "Platser"


class RecordsMediaInline(admin.TabularInline):
	model = RecordsMedia
	model._meta.verbose_name_plural = "Filer"


class CrowdSourceMediaInline(admin.TabularInline):
	model = CrowdSourceMedia
	model._meta.verbose_name_plural = "Källfiler"
	fields = ['image_tag']
	readonly_fields = ['image_tag']

class RecordsCategoriesInline(admin.TabularInline):
	model = RecordsCategory
	raw_id_fields = ['category']
	model._meta.verbose_name_plural = "Kategorier"


class RecordsMetadataInline(admin.TabularInline):
	model = RecordsMetadata


def force_update(modeladmin, request, queryset):
	for model in queryset:
		model.changedate = time.strftime('%Y-%m-%d %H:%M:%S')
		model.save()
		time.sleep(0.5)

force_update.short_description = 'Force update'

class MetadataTypesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'type', 'label']
	extra_list_display = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	fields = ['type', 'label']

	def save_model(self, request, obj, form, change):
		if change == True:										# Was the post changed?
			obj.editedby = request.user							#	Get the current user and log it as the editor
		else:   												# The post might be new
			if getattr(obj, 'createdby', None) is None:			#	check if the creator is defined
				obj.createdby = request.user					#		If not, set the current user as the creator
		obj.save()												# Save the post.


class RecordsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'title', 'archive', 'type', 'country']
	extra_list_display = []
	extra_list_filter = ['type', ('archive', DropdownFilter), ('categories', RelatedDropdownFilter), ('places', RelatedDropdownFilter), ('places__harad__landskap', DropdownFilter), 'country', 'language']
	extra_search_fields = []
	list_editable = ['title', 'archive', 'type']
	raw_id_fields = ['person_objects']
	inlines = [RecordsCategoriesInline, RecordsPersonsInline, RecordsPlacesInline, RecordsMetadataInline, RecordsMediaInline]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = ['transcriptionstatus', 'transcribedby', 'approvedby', 'approvedate']
	actions = [force_update]
	fields = [('title', 'id'), ('type'), ('archive', 'year'), ('archive_page', 'total_pages', 'archive_id'), 'text', 'source', 'comment', ('country', 'language'), ('transcriptionstatus', 'transcribedby'), ('approvedby', 'approvedate')]

	def lookup_allowed(self, lookup, value):
		if lookup == 'places__harad__landskap':
			return True
		return super(RecordsAdmin, self).lookup_allowed(lookup, value)

	def save_model(self, request, obj, form, change):
		if request.user.groups.filter(name='Norge').exists():
			obj.country = 'norway'
		if getattr(obj, 'createdby', None) is None:
			# if change == False:
			obj.createdby = request.user
		else:
			obj.changedby = request.user
		obj.save()

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


class CrowdSourceReview(ExtendedModelAdminMixin, admin.ModelAdmin):
	save_on_top = True
	list_display = ['id', 'title', 'to_be_transcribed', 'transcribedby', 'transcriptiondate']
	extra_list_display = []
	list_filter = ['transcriptionstatus', 'transcribedby', 'transcriptiondate']
	#extra_list_filter = ['transcriptionstatus']
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = [CrowdSourceMediaInline]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {
		#models.CharField: {'widget': TextInput(attrs={'size': '20'})},
		#models.TextField: {'widget': TextInput(attrs={'size': '20'})},
	}
	readonly_fields = ['id', 'title', 'transcriptiondate', 'approvedby']
	actions = [force_update, 'remove_transcription']

	fields = [('id', 'title'), 'text', 'comment', ('transcribedby', 'transcriptiondate'), ('transcriptionstatus', 'approvedby')]
	search_fields = ['id','title']

	def save_model(self, request, obj, form, change):
		if change == True:
			obj.approvedby = request.user
		obj.save()

	# Set active placename in session as session attribute
	def remove_transcription(self, request, queryset):
		# active_placename = queryset.first()
		if queryset.count() == 1:
			active_record = queryset[0]
			#Find crowdsource informant by id
			crid = 'crwd' + active_record.id
			person = Persons.objects.filter(pk=crid)
			person_arr = []
			person_arr += person
			if len(person_arr) == 1:
				records_person = RecordsPersons.objects.filter(person=person_arr[0])
				records_person_arr = []
				records_person_arr += records_person
				#Only one relation to this person
				if len(records_person_arr) == 1:
					#Remove person
					person[0].delete()
				#Remove person
				#Persons.objects.filter(pk=records_person_arr[0].person).delete()
				#rRemove relation
				#records_person_arr[0].delete()

			records_person = CrowdSourceUsers.objects.filter(pk=active_record.transcribedby.userid)
			records_person_arr = []
			records_person_arr += records_person
			if len(records_person_arr) == 1:
				crowdsourceuser = records_person_arr[0]
				try:

					crowdsourceuser.delete()
				except Exception as e:
					print(e)
			#Set record data to not transcribed
			active_record.text = 'Ej transkriberad.'
			active_record.transcriptionstatus = 'untranscribed'
			active_record.transcribedby = ''
			active_record.save()

			message = "Transkribering borttagen för '" + str(active_record) + "'."
			self.message_user(request, message)

	remove_transcription.short_description = "UNDER DEVELOPMENT: Ta bort transkribering (OBS: Välj bara en)"


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
	readonly_fields = ['image_tag', 'createdby', 'createdate', 'editedby', 'changedate']
	fields = ['id', 'name', ('gender', 'birth_year'), 'address', 'biography', ('image', 'image_tag'), ('createdby', 'createdate', 'editedby', 'changedate')]

	def lookup_allowed(self, lookup, value):
		if lookup == 'record_objects__country__exact':
			return True
		return super(PersonsAdmin, self).lookup_allowed(lookup, value)

	def get_queryset(self, request):
		qs = super(PersonsAdmin, self).get_queryset(request)
		if request.user.groups.filter(name='Norge').exists():
			inner_qs = Records.objects.filter(country='norway')
			return qs.filter(record_objects__in=inner_qs).distinct()
		return qs

	def save_model(self, request, obj, form, change):
		if change == True:										# Was the post changed?
			obj.editedby = request.user							#	Get the current user and log it as the editor
		else:   												# The post might be new
			if getattr(obj, 'createdby', None) is None:			#	check if the creator is defined
				obj.createdby = request.user					#		If not, set the current user as the creator
		obj.save()												# Save the post.


class RecordsPersonsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = ['id']
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
	fields = ['name', 'harad', 'fylke', 'lat', 'lng', 'map_tag', 'id']
	readonly_fields = ['id', 'map_tag']


class CategoriesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = ['type']
	extra_search_fields = []
	list_display = ['id', 'name', 'type']
	list_editable = ['name', 'type']
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []

	def save_model(self, request, obj, form, change):
		if change == True:										# Was the post changed?
			obj.editedby = request.user							#	Get the current user and log it as the editor
		else:   												# The post might be new
			if getattr(obj, 'createdby', None) is None:			#	check if the creator is defined
				obj.createdby = request.user					#		If not, set the current user as the creator
		obj.save()												# Save the post.


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

	def save_model(self, request, obj, form, change):
		if change == True:										# Was the post changed?
			obj.editedby = request.user							#	Get the current user and log it as the editor
		else:   												# The post might be new
			if getattr(obj, 'createdby', None) is None:			#	check if the creator is defined
				obj.createdby = request.user					#		If not, set the current user as the creator
		obj.save()												# Save the post.


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

class CrowdSourceUsersAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['userid', 'name', 'email']
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
	fields = []
	readonly_fields = []


admin.site.register(CategoriesKlintberg, CategoriesKlintbergAdmin)
admin.site.register(RecordsPlaces, RecordsPlacesAdmin)
admin.site.register(Records, RecordsAdmin)
admin.site.register(CrowdSourceRecords, CrowdSourceReview)
admin.site.register(RecordsCategory, RecordsCategoryAdmin)
admin.site.register(Persons, PersonsAdmin)
admin.site.register(RecordsPersons, RecordsPersonsAdmin)
admin.site.register(PersonsPlaces, PersonsPlacesAdmin)
admin.site.register(SockenV1, SockenV1Admin)
admin.site.register(RecordsMedia, RecordsMediaAdmin)
admin.site.register(Socken, SockenAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Harad, HaradAdmin)
admin.site.register(CrowdSourceUsers, CrowdSourceUsersAdmin)
admin.site.register(MetadataTypes, MetadataTypesAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
#admin.site.unregister(Group)
#admin.site.register(Group, CustomGroupAdmin)
