# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoriesKlintberg(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories_klintberg'


class Harad(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    lan = models.CharField(max_length=30, blank=True, null=True)
    landskap = models.CharField(max_length=14, blank=True, null=True)
    country = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harad'


class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=255)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'media'


class Persons(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=2)
    birth_year = models.IntegerField()
    address = models.CharField(max_length=255)
    biography = models.TextField()
    image = models.CharField(max_length=255)
    changedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'persons'


class PersonsPlaces(models.Model):
    person = models.IntegerField()
    place = models.IntegerField()
    relation = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons_places'


class Records(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    year = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=20)
    archive = models.CharField(max_length=255)
    archive_id = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    archive_page = models.CharField(max_length=20, blank=True, null=True)
    source = models.TextField()
    comment = models.TextField()
    informant_name = models.CharField(max_length=255)
    changedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'records'


class RecordsCategory(models.Model):
    record = models.IntegerField()
    category = models.CharField(max_length=20)
    level = models.IntegerField()
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'records_category'


class RecordsMedia(models.Model):
    record = models.IntegerField()
    media = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'records_media'


class RecordsPersons(models.Model):
    record = models.IntegerField()
    person = models.IntegerField()
    relation = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'records_persons'


class RecordsPlaces(models.Model):
    record = models.IntegerField()
    place = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'records_places'


class Socken(models.Model):
    name = models.CharField(max_length=200)
    harad = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    sweref99_n = models.FloatField(db_column='sweref99_N')  # Field name made lowercase.
    sweref99_e = models.FloatField(db_column='sweref99_E')  # Field name made lowercase.
    changedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'socken'


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

