# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from string import Template
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.utils.functional import lazy
import requests, json
from django.db import models
from threading import Timer

from django.contrib.auth.models import User

import es_config

class Harad(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	lan = models.CharField(max_length=30, blank=True, null=True)
	landskap = models.CharField(max_length=14, blank=True, null=True)
	country = models.CharField(unique=True, max_length=100, blank=True, null=True)
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	def __str__(self):
		return self.name if self.name else ''

	class Meta:
		managed = True
		db_table = 'harad'
		verbose_name = 'Härad'
		verbose_name_plural = 'Härads'


class ImportBatch(models.Model):
	batch_id = models.AutoField(primary_key=True, null=False)
	source_file_name = models.CharField(max_length=255, null=False)
	records_count = models.IntegerField(blank=True, null=True)
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")


	class Meta:
		managed = True
		db_table = 'import_batch'


class Socken(models.Model):
	name = models.CharField(max_length=200)
	harad = models.ForeignKey(Harad, models.DO_NOTHING, null=True, blank=True, db_column='harad')
	fylke = models.CharField(max_length=50, blank=True, null=True)
	lat = models.FloatField()
	lng = models.FloatField()
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	def map_tag(self):
		values = {
			'lat': str(self.lat),
			'lng': str(self.lng)
		}
		map_template = """
			<link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css" />
			<script src="https://unpkg.com/leaflet@1.2.0/dist/leaflet.js"></script>
			<div id="socken_map" style="width: 100%; height: 400px;"></div>
			<script type="text/javascript">
				var map = L.map("socken_map").setView([${lat}, ${lng}], 8); // Skapar en karta
				L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {attribution: "&copy; <a href='http://osm.org/copyright'>OpenStreetMap</a> contributors"}).addTo(map);
				var marker = L.marker([${lat}, ${lng}]); // Lägger till en L.marker
				marker.addTo(map);

				map.on('click', function(e) { // Map click handler
					marker.setLatLng(e.latlng); // Uppdaterar punkten på kartan

					django.jQuery('#id_lat').val(e.latlng.lat.toFixed(6)); // Skriver e.latlng.lat från punkter var man klickade på kartan till "lat" fältet
					django.jQuery('#id_lng').val(e.latlng.lng.toFixed(6)); // Skriver e.latlng.lng från punkter var man klickade på kartan till "lng" fältet
				});
			</script>
		"""

		template = Template(map_template)

		map_html = template.substitute(values)

		return mark_safe(map_html);

	map_tag.short_description = 'Karta'
	map_tag.allow_tags = True

	def __str__(self):
		return self.name+' ('+str(self.id)+') '

	class Meta:
		managed = True
		db_table = 'socken'
		verbose_name = 'Socken'
		verbose_name_plural = 'Socknar'


class Categories(models.Model):
	type_choices = [
		('folkminnen', 'Folkminnen'),
		('sägner', 'Sägner'),
		('frågelista', 'Frågelista'),
		('webbfrågelista', 'Webbfrågelista'),
		('matkarta', 'Matkarta'),
		('digitalt-kulturarv', 'Digitalt kulturarv'),
		('tradark', 'TradArk'),
	]

	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=255)
	name_en = models.CharField(max_length=255, null=True, blank=True)
	type = models.CharField(max_length=255, choices=type_choices)
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	def __str__(self):
		return str(self.name)+' ('+self.id+') ['+self.type+']'

	class Meta:
		managed = True
		db_table = 'categories_v2'
		ordering = ['type']
		verbose_name = 'Kategori'
		verbose_name_plural = 'Kategorier'


class CategoriesKlintberg(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=255)
	name_en = models.CharField(max_length=255)
	level = models.IntegerField()
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'categories_klintberg'


class Persons(models.Model):
	id = models.CharField(primary_key=True, max_length=50)
	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=8, choices=[('female', 'Kvinna'), ('male', 'Man'), ('unknown', 'Okänd')])
	birth_year = models.IntegerField(blank=True, null=True)
	address = models.CharField(blank=True, null=True, max_length=255)
	birthplace = models.CharField(blank=True, null=True, max_length=255, verbose_name='Födelseort')
	biography = models.TextField(blank=True, null=True)
	image = models.ImageField(blank=True, null=True, verbose_name='Bildfil', upload_to='personer')
	transcriptioncomment = models.CharField(max_length=255, verbose_name='Kommentarer', default='')
	#changedate = models.DateTimeField()
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")
	places = models.ManyToManyField(
		Socken,
		through='PersonsPlaces',
		through_fields = ('person', 'place')
	)

	record_objects = models.ManyToManyField(
		'Records',
		through='RecordsPersons',
		verbose_name = 'Sägner'
	)

	def image_tag(self):
		return mark_safe('<a href="/media/%s" target="_blank"><img src="/media/%s" style="max-width: 300px" /></a>' % (self.image, self.image))

	image_tag.short_description = 'Bild'
	image_tag.allow_tags = True

	def __str__(self):
		return self.name+' ['+self.id+'] ('+str(self.birth_year)+')'

	class Meta:
		managed = True
		db_table = 'persons'
		verbose_name = 'Person'
		verbose_name_plural = 'Personer'


class PersonsPlaces(models.Model):
	person = models.ForeignKey(Persons, db_column='person')
	place = models.ForeignKey(Socken, db_column='place')
	relation = models.CharField(max_length=5, blank=True, null=True, choices=[('birth', 'birth'), ('home', 'home')])

	class Meta:
		managed = True
		db_table = 'persons_places'


class CrowdSourceUsers(models.Model):
	userid = models.CharField(primary_key=True, max_length=150)
	name = models.CharField(max_length=255)
	email = models.EmailField()

	class Meta:
		managed = True
		db_table = 'crowdsource_users'


class ImportBatch(models.Model):
	batch_id = models.AutoField(primary_key=True, null=False)
	source_file_name = models.CharField(max_length=255, null=False)
	records_count = models.IntegerField(blank=True, null=True)
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'import_batch'


class Records(models.Model):
	type_choices = [
		('arkiv', 'Arkiv'),
		('tryckt', 'Tryckt'),
		('register', 'Register'),
		('inspelning', 'Inspelning'),
		('matkarta', 'Matkarta'),
		('frågelista', 'Frågelista'),
		('accessionsregister', 'Accessionsregister'),
		('webbfrågelista', 'Webbfrågelista'),
		('brev', 'Brev'),
		('folkmusik', 'Folkmusik'),
	]

	country_choices = [
		('sweden', 'Sverige'),
		('norway', 'Norge'),
		('none', 'Inget')
	]

	language_choices = [
		('swedish', 'Svenska'),
		('norwegian', 'Norska')
	]

	transcription_statuses = [
		('untranscribed', 'Ej transkriberad'),
		('transcribed', 'Transkriberad'),
		('reviewing', 'Under granskning'),
		('approved', 'Godkänd'),
		('published', 'Publicerad')
	]

	id = models.CharField(primary_key=True, max_length=150)
	title = models.CharField(max_length=255, verbose_name='Titel')
	text = models.TextField(blank=True, null=True)
	year = models.DateField(blank=True, null=True)
	#category = models.ForeignKey(Categories, db_column='category')
	#category = models.CharField(max_length=20, blank=True, verbose_name='Kategori')
	archive = models.CharField(max_length=255, blank=True, verbose_name='Arkiv')
	archive_id = models.CharField(max_length=1000, blank=True)
	type = models.CharField(max_length=20, verbose_name='Materialtyp', choices=type_choices)
	archive_page = models.CharField(max_length=20, blank=True, null=True)
	total_pages = models.IntegerField(default=1, blank=False, null=False)
	source = models.TextField(blank=True, verbose_name='Källa')
	comment = models.TextField(blank=True)
	country = models.CharField(max_length=20, blank=False, null=False, default='sweden', choices=country_choices)
	language = models.CharField(max_length=20, blank=False, null=False, default='swedish', choices=language_choices)
	import_batch = models.ForeignKey(ImportBatch, db_column="import_batch", null=True)
	import_row_id = models.IntegerField(default=0, blank=False, null=False)
	transcriptiondate = models.DateTimeField(blank=True, verbose_name="Transkriptionsdatum")
	transcribedby = models.ForeignKey(CrowdSourceUsers, db_column='transcribedby', null=True, blank=True)
	transcriptionstatus = models.CharField(max_length=20, blank=False, null=False, default='new', choices=transcription_statuses)
	approvedby = models.ForeignKey(User, db_column='approvedby', null=True, blank=True, editable=False, verbose_name='Godkänd av')
	approvedate = models.DateTimeField(blank=True, verbose_name="Godkänd datum")
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', related_name='records_created',null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	person_objects = models.ManyToManyField(
		Persons,
		through='RecordsPersons',
	#    through_fields = ('record', 'person'),
		verbose_name = 'Personer'
	)
	places = models.ManyToManyField(
		Socken,
		through = 'RecordsPlaces',
	#    through_fields = ('record', 'place'),
		verbose_name = 'Socken'
	)
	categories = models.ManyToManyField(
		Categories,
		through = 'RecordsCategory',
	#    through_fields = ('record', 'place'),
		verbose_name = 'Kategorier'
	)

	def __str__(self):
		return self.title

	class Meta:
		managed = True
		db_table = 'records'
		verbose_name = 'Uppteckning/inspelning'
		verbose_name_plural = 'Uppteckningar och inspelningar'
		permissions = (
			('view_records', 'Kan visa postar'),
		)


class MetadataTypes(models.Model):
	type = models.CharField(max_length=255, blank=False, null=False)
	label = models.CharField(max_length=500, blank=False, null=False)
	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'metadata_types'
		verbose_name = 'Metadata typ'
		verbose_name_plural = 'Metadata typer'


def get_records_metadata_types():
	metadataTypes = MetadataTypes.objects.order_by('label').all()

	def itemFormat(item):
		return (item.type, item.label)

	types = list(map(itemFormat, metadataTypes))

	print('get_records_metadata_types')

	return types


class RecordsMetadata(models.Model):
	record = models.ForeignKey(Records, db_column='record', related_name='metadata')
	type = models.CharField(max_length=30, blank=True, null=True, choices=get_records_metadata_types())
	value = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.type+': '+self.value if self.type and self.value else ''

	class Meta:
		managed = True
		db_table = 'records_metadata'


class RecordsMedia(models.Model):
	record = models.ForeignKey(Records, db_column='record', related_name='media')
	type = models.CharField(max_length=30, blank=True, null=True, choices=[('image', 'Bildfil'), ('pdf', 'Pdf'), ('audio', 'Ljudfil')])
	source = models.CharField(max_length=255, blank=True, null=True)
	title = models.TextField(blank=True, null=True)

	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'records_media'


class CrowdSourceRecords(models.Model):
	transcription_statuses = [
		('untranscribed', 'Ej transkriberad'),
		('transcribed', 'Transkriberad'),
		('reviewing', 'Under granskning'),
		('approved', 'Godkänd'),
		('published', 'Publicerad')
	]
	id = models.CharField(primary_key=True, max_length=150)
	title = models.CharField(max_length=255, verbose_name='Titel')
	text = models.TextField(blank=True, null=True)
	transcriptiondate = models.DateTimeField(blank=True, verbose_name="Transkriptionsdatum")
	transcribedby = models.ForeignKey(CrowdSourceUsers, db_column='transcribedby', null=True, blank=True)
	transcriptionstatus = models.CharField(max_length=20, blank=False, null=False, default='new', choices=transcription_statuses, verbose_name='transcription status')
	approvedby = models.ForeignKey(User, db_column='approvedby', null=True, blank=True, editable=False, verbose_name='Godkänd av')
	approvedate = models.DateTimeField(blank=True, verbose_name="Godkänd datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")

	def to_be_transcribed(self):
		if (self.text == 'Ej transkriberad.'):
			return self.text
		return self.transcriptionstatus

	to_be_transcribed.short_description = 'Transcription status'

	class Meta:
		managed = False			# Skall ej vara kopplad till automatiska migreringar, det sker via Records!
		db_table = 'records'


class CrowdSourceMedia(models.Model):
	record = models.ForeignKey(CrowdSourceRecords, db_column='record', related_name='media')
	type = models.CharField(max_length=30, blank=True, null=True, choices=[('image', 'Bildfil'), ('pdf', 'Pdf'), ('audio', 'Ljudfil')])
	source = models.CharField(max_length=255, blank=True, null=True)
	title = models.TextField(blank=True, null=True)

	class Meta:
		managed = False			# Skall ej vara kopplad till automatiska migreringar, det sker via RecordsMedia!
		db_table = 'records_media'

	def image_tag(self):
		return mark_safe('<a href="https://www4.isof.se/Folkminnen/Svenska_sagor_filer/%s" target="_blank">'
						 '  <img src="https://www4.isof.se/Folkminnen/Svenska_sagor_filer/%s" width="200" height="150" />'
						 '</a>' % (self.source, self.source)
						 )

	image_tag.short_description = 'Original'


class RecordsPersons(models.Model):
	record = models.ForeignKey(Records, db_column='record')
	person = models.ForeignKey(Persons, db_column='person')
	relation = models.CharField(max_length=20, blank=True, null=True, choices=[('i', 'Informant'), ('c', 'Uppteckare'), ('sender', 'Avsändare'), ('receiver', 'Mottagare'), ('recorder', 'Intervjuare')])

	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'records_persons'
		unique_together = (('record', 'person'),)


class RecordsPlaces(models.Model):
	relation_type_choices = [
		('place_collected', 'Insamlingsort'), 
		('place_mentioned', 'Nämns i texten'), 
		('related_person_place', 'Födelseort/hemort'), 
		('dispatch_place', 'Avsändningsort'), 
		('destination_place', 'Destination')
	]

	record = models.ForeignKey(Records, db_column='record')
	place = models.ForeignKey(Socken, db_column='place')
	type = models.CharField(max_length=20, blank=True, null=True, default='place_collected', choices=relation_type_choices)

	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'records_places'


class RecordsCategory(models.Model):
	record = models.ForeignKey(Records, db_column='record')
	category = models.ForeignKey(Categories, db_column='category')

	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'records_category'


class SockenV1(models.Model):
	id = models.IntegerField(primary_key=True, default=0)
	name = models.CharField(max_length=255)
	harad = models.IntegerField()
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
# 	changedate = models.DateTimeField()

	createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
	changedate = models.DateTimeField(auto_now=True, blank=True, verbose_name="Ändrad datum")
	createdby = models.ForeignKey(User, db_column='createdby', null=True, blank=True, editable=False,
							 verbose_name="Excerperad av")
	editedby = models.ForeignKey(User, db_column='editedby', null=True, blank=True, editable=False,
								 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

	class Meta:
		managed = True
		db_table = 'socken_v1'


class ImportRecords(models.Model):
    # id = models.CharField(primary_key=True, max_length=150)
    id = models.IntegerField(primary_key=True)
    batchid = models.IntegerField()
    title = models.CharField(max_length=255, verbose_name='Titel')
    text = models.TextField(blank=True, null=True)
    year = models.DateField(blank=True, null=True)

    #Categories. Comma separated if more than one
    category = models.CharField(max_length=20, blank=True, verbose_name='Kategori')
    #Data on each batchid:
    #archive = models.CharField(max_length=255, blank=True, verbose_name='Arkiv')

    #Accessionsid
    archive_sub_id = models.IntegerField()
    #Accessionsnummer
    archive_id = models.CharField(max_length=1000, blank=True)
    #type = models.CharField(max_length=20, verbose_name='Materialtyp', choices=type_choices)

    #start_page = models.IntegerField()
    #end_page = models.IntegerField()
    #Start page
    archive_page = models.CharField(max_length=20, blank=True, null=True)
    #endpage = archive_page + total_pages
    total_pages = models.IntegerField(default=1, blank=False, null=False)

    source = models.TextField(blank=True, verbose_name='Källa')
    comment = models.TextField(blank=True)

    #Data on each batchid:
    #country = models.CharField(max_length=20, blank=False, null=False, default='sweden', choices=country_choices)
    #language = models.CharField(max_length=20, blank=False, null=False, default='swedish', choices=language_choices)

    #Change
    createdate = models.DateTimeField(auto_now_add=True, verbose_name="Skapad datum")
    changedate = models.DateTimeField(auto_now=True, verbose_name="Ändringsdatum")
    createuser = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Excerperad av")
    changeuser = models.ForeignKey(User, null=True, blank=True, editable=False,
                                 related_name='Uppdaterad av+', verbose_name="Uppdaterad av")

    def __str__(self):
        name = ""
        if self.title != None:
            name = self.title
        if self.category != None:
            name = name + ' - ' + self.category
        return name

    class Meta:
        managed = True
        db_table = 'import_records'

def model_m2m_changed(sender, **kwargs):
	print(kwargs['instance'].id)

	modelJson = requests.get(es_config.restApiRecordUrl+str(kwargs['instance'].id), verify=False)
	print(es_config.restApiRecordUrl+str(kwargs['instance'].id))
	print(modelJson.json())


# Spara/uppdatera modell JSON i Elasticsearch
def records_post_saved(sender, **kwargs):
	def save_es_model():
		modelId = kwargs['instance'].id
		print('records_post_saved')

		modelResponseData = requests.get(es_config.restApiRecordUrl+str(modelId), verify=False)
		modelResponseData.encoding = 'utf-8'
		modelJson = modelResponseData.json()

		document = {
			'doc': modelJson
		}

		esResponse = requests.post(es_config.protocol+(es_config.user+':'+es_config.password+'@' if hasattr(es_config, 'user') else '')+es_config.host+'/'+es_config.index_name+'/legend/'+str(modelId)+'/_update', data=json.dumps(document).encode('utf-8'), verify=False)

		if 'status' in esResponse.json() and esResponse.json()['status'] == 404:
			esResponse = requests.put(es_config.protocol+(es_config.user+':'+es_config.password+'@' if hasattr(es_config, 'user') else '')+es_config.host+'/'+es_config.index_name+'/legend/'+str(modelId), data=json.dumps(modelJson).encode('utf-8'), verify=False)

	t = Timer(5, save_es_model)
	t.start()


# Radera model JSON från Elasticsearch
def model_post_delete(sender, **kwargs):
	modelId = kwargs['instance'].id

	try:
		esResponse = requests.delete(es_config.protocol+(es_config.user+':'+es_config.password+'@' if hasattr(es_config, 'user') else '')+es_config.host+'/'+es_config.index_name+'/legend/'+str(modelId), verify=False)
	except TypeError:
		pass


# Spara/uppdatera modell JSON i Elasticsearch
def person_post_saved(sender, **kwargs):
	def save_es_model():
		modelId = kwargs['instance'].id

		print('person_post_saved')
		print(modelId)

	t = Timer(5, save_es_model)
	t.start()


post_save.connect(records_post_saved, sender=Records)
m2m_changed.connect(records_post_saved, sender=Records)
post_delete.connect(model_post_delete, sender=Records)

post_save.connect(person_post_saved, sender=Persons)
