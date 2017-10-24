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
from django.db.models.signals import post_save, m2m_changed
import requests, json
from django.db import models
from threading import Timer

import es_config

class Harad(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	lan = models.CharField(max_length=30, blank=True, null=True)
	landskap = models.CharField(max_length=14, blank=True, null=True)
	country = models.CharField(unique=True, max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name if self.name else ''

	class Meta:
		managed = False
		db_table = 'harad'
		verbose_name = 'Härad'
		verbose_name_plural = 'Härads'


class Socken(models.Model):
	name = models.CharField(max_length=200)
	harad = models.ForeignKey(Harad, models.DO_NOTHING, db_column='harad')
	lat = models.FloatField()
	lng = models.FloatField()
	#changedate = models.DateTimeField()

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
		managed = False
		db_table = 'socken'
		verbose_name = 'Socken'
		verbose_name_plural = 'Socknar'

class Categories(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=255)
	name_en = models.CharField(max_length=255, null=True, blank=True)
	type = models.CharField(max_length=255, choices=[('sägner', 'Sägner'), ('frågelista', 'Frågelista'), ('matkarta', 'Matkarta')])

	def __str__(self):
		return '('+self.id+') '+str(self.name)+' ['+self.type+']'

	class Meta:
		managed = False
		db_table = 'categories_v2'
		ordering = ['type']
		verbose_name = 'Kategori'
		verbose_name_plural = 'Kategorier'


class CategoriesKlintberg(models.Model):
	id = models.CharField(primary_key=True, max_length=10)
	name = models.CharField(max_length=255)
	name_en = models.CharField(max_length=255)
	level = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'categories_klintberg'


class Persons(models.Model):
	id = models.CharField(primary_key=True,max_length=255)
	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=2, choices=[('k', 'Kvinna'), ('m', 'Man')])
	birth_year = models.IntegerField(blank=True, null=True)
	address = models.CharField(max_length=255)
	biography = models.TextField()
	image = models.ImageField(verbose_name='Bildfil')
	changedate = models.DateTimeField()
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
		return mark_safe('<a href="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" target="_blank"><img src="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" style="max-width: 300px" /></a>' % (self.image, self.image))
	
	image_tag.short_description = 'Bild'
	image_tag.allow_tags = True

	def __str__(self):
		return self.name+' ('+str(self.birth_year)+')'

	class Meta:
		managed = False
		db_table = 'persons'
		verbose_name = 'Person'
		verbose_name_plural = 'Personer'


class PersonsPlaces(models.Model):
	person = models.ForeignKey(Persons, db_column='person')
	place = models.ForeignKey(Socken, db_column='place')
	relation = models.CharField(max_length=5, blank=True, null=True, choices=[('birth', 'birth'), ('home', 'home')])

	class Meta:
		managed = False
		db_table = 'persons_places'


class Media(models.Model):
	id = models.IntegerField(primary_key=True)
	source = models.ImageField(verbose_name='Bildfil')
	type = models.CharField(max_length=10, verbose_name='Mediatyp')

	def image_tag(self):
		return mark_safe('<a href="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" target="_blank"><img src="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" style="max-width: 300px" /></a>' % (self.source, self.source))
	
	image_tag.short_description = 'Bild'
	image_tag.allow_tags = True

	record_objects = models.ManyToManyField(
		'Records',
		through='RecordsMedia'
	)

	def __str__(self):
		return '['+self.type+'] '+str(self.source)

	class Meta:
		managed = False
		db_table = 'media'
		verbose_name = 'Mediafil'
		verbose_name_plural = 'Mediafiler'


class Records(models.Model):
	title = models.CharField(max_length=255, verbose_name='Titel')
	text = models.TextField()
	year = models.IntegerField(blank=True, null=True)
	category = models.ForeignKey(Categories, db_column='category')
	#category = models.CharField(max_length=20, blank=True, verbose_name='Kategori')
	archive = models.CharField(max_length=255, blank=True, verbose_name='Arkiv')
	archive_id = models.CharField(max_length=255, blank=True)
	type = models.CharField(max_length=20, verbose_name='Materialtyp', choices=[('arkiv', 'arkiv'), ('tryckt', 'tryckt'), ('register', 'register'), ('inspelning', 'inspelning'), ('matkarta', 'matkarta'), ('frågelista', 'frågelista')])
	archive_page = models.CharField(max_length=20, blank=True, null=True)
	source = models.TextField(blank=True, verbose_name='Källa')
	comment = models.TextField(blank=True)
	country = models.CharField(max_length=255, blank=False, null=False, default='sweden', choices=[('sweden', 'Sverige'), ('norway', 'Norge')])
	changedate = models.DateTimeField(auto_now_add=True, blank=True)
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
	media_objects = models.ManyToManyField(
		Media,
		through='RecordsMedia'
	)

	def __str__(self):
		return self.title

	class Meta:
		managed = False
		db_table = 'records'
		verbose_name = 'Sägen'
		verbose_name_plural = 'Sägner'
		permissions = (
			('view_records', 'Kan visa postar'),
		)


class RecordsMetadata(models.Model):
	record = models.ForeignKey(Records, db_column='record', related_name='metadata')
	type = models.CharField(max_length=30, blank=True, null=True, choices=[('sitevision_url', 'Sitevision url')])
	value = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.type+': '+self.value if self.type else ''

	class Meta:
		managed = False
		db_table = 'records_metadata'


class RecordsCategory(models.Model):
	record = models.IntegerField()
	category = models.CharField(max_length=20)
	level = models.IntegerField()
	type = models.CharField(max_length=50)

	class Meta:
		managed = False
		db_table = 'records_category'


class RecordsMedia(models.Model):
	record = models.ForeignKey(Records, db_column='record')
	media = models.ForeignKey(Media, db_column='media')

	class Meta:
		managed = False
		db_table = 'records_media'


class RecordsPersons(models.Model):
	record = models.ForeignKey(Records, db_column='record')
	person = models.ForeignKey(Persons, db_column='person')
	relation = models.CharField(max_length=5, blank=True, null=True, choices=[('i', 'Informant'), ('c', 'Uppteckare')])

	class Meta:
		managed = False
		db_table = 'records_persons'
		unique_together = (('record', 'person'),)

class RecordsPlaces(models.Model):
	record = models.ForeignKey(Records, db_column='record')
	place = models.ForeignKey(Socken, db_column='place')

	class Meta:
		managed = False
		db_table = 'records_places'


class SockenV1(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	harad = models.IntegerField()
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)
	changedate = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'socken_v1'


def model_m2m_changed(sender, **kwargs):
	print(kwargs['instance'].id)

	modelJson = requests.get(es_config.restApiRecordUrl+str(kwargs['instance'].id), verify=False)
	print(es_config.restApiRecordUrl+str(kwargs['instance'].id))
	print(modelJson.json())

def model_post_saved(sender, **kwargs):
	def save_es_model():
		modelId = kwargs['instance'].id
		print('model_post_saved')

		modelResponseData = requests.get(es_config.restApiRecordUrl+str(modelId), verify=False)
		modelResponseData.encoding = 'utf-8'
		modelJson = modelResponseData.json()

		document = {
			'doc': modelJson
		}

		esResponse = requests.post('https://'+es_config.user+':'+es_config.password+'@'+es_config.host+'/'+es_config.index_name+'/legend/'+str(modelId)+'/_update', data=json.dumps(document).encode('utf-8'), verify=False)

		print(esResponse.json())
		if 'status' in esResponse.json() and esResponse.json()['status'] == 404:
			esResponse = requests.put('https://'+es_config.user+':'+es_config.password+'@'+es_config.host+'/'+es_config.index_name+'/legend/'+str(modelId), data=json.dumps(modelJson).encode('utf-8'), verify=False)

		print(esResponse.json())

	t = Timer(5, save_es_model)
	t.start()


post_save.connect(model_post_saved, sender=Records)