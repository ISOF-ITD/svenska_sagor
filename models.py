# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.safestring import mark_safe

from django.db import models


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
        return mark_safe('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.2.0/dist/leaflet.css" /><script src="https://unpkg.com/leaflet@1.2.0/dist/leaflet.js"></script><div id="socken_map" style="width: 100%; height: 400px;"><script type="text/javascript">var map = L.map("socken_map").setView(['+str(self.lat)+', '+str(self.lng)+'], 8); L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {attribution: "&copy; <a href=\'http://osm.org/copyright\'>OpenStreetMap</a> contributors"}).addTo(map);L.marker(['+str(self.lat)+', '+str(self.lng)+']).addTo(map);</script></div>');
    
    map_tag.short_description = 'Karta'
    map_tag.allow_tags = True

    def __str__(self):
        return self.name+' ('+str(self.id)+')'

    class Meta:
        managed = False
        db_table = 'socken'
        verbose_name = 'Socken'
        verbose_name_plural = 'Socknar'

class Categories(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categories'
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


class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.ImageField(verbose_name='Bildfil')
    type = models.CharField(max_length=10, verbose_name='Mediatyp')

    def image_tag(self):
        return mark_safe('<a href="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" target="_blank"><img src="http://www4.sprakochfolkminnen.se/Folkminnen/Svenska_sagor_filer/%s" style="max-width: 300px" /></a>' % (self.source, self.source))
    
    image_tag.short_description = 'Bild'
    image_tag.allow_tags = True

    def __str__(self):
        return '['+self.type+'] '+str(self.source)

    class Meta:
        managed = False
        db_table = 'media'
        verbose_name = 'Mediafil'
        verbose_name_plural = 'Mediafiler'


class Persons(models.Model):
    id = models.IntegerField(primary_key=True)
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


class Records(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titel')
    text = models.TextField()
    year = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, verbose_name='Kategori')
    archive = models.CharField(max_length=255, blank=True)
    archive_id = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=20, verbose_name='Materialtyp', choices=[('arkiv', 'arkiv'), ('tryckt', 'tryckt'), ('register', 'register'), ('inspelning', 'inspelning')])
    archive_page = models.CharField(max_length=20, blank=True, null=True)
    source = models.TextField(blank=True, verbose_name='Källa')
    comment = models.TextField(blank=True)
    changedate = models.DateTimeField()
    persons = models.ManyToManyField(
        Persons, 
        through='RecordsPersons', 
        through_fields = ('record', 'person')
    )
    places = models.ManyToManyField(
        Socken, 
        through='RecordsPlaces', 
        through_fields = ('record', 'place')
    )
    media = models.ManyToManyField(
        Media,
        through='RecordsMedia',
        through_fields=('record', 'media')
    )
    #persons = models.ForeignKey(RecordsPersons)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'records'
        verbose_name = 'Sägen'
        verbose_name_plural = 'Sägner'


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
    relation = models.CharField(max_length=5, blank=True, null=True, choices=[('i', 'Inormant'), ('c', 'Uppteckare')])

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

