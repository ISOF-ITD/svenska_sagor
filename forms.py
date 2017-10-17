from django import forms
from .models import CategoriesKlintberg, RecordsPlaces, Records, Media, RecordsCategory, Persons, RecordsPersons, PersonsPlaces, SockenV1, RecordsMedia, Socken, Categories, Harad


class CategoriesKlintbergForm(forms.ModelForm):

    class Meta:
        model = CategoriesKlintberg
        fields = ['name', 'name_en', 'level']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CategoriesKlintbergForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CategoriesKlintbergForm, self).is_valid()

    def full_clean(self):
        return super(CategoriesKlintbergForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_name_en(self):
        name_en = self.cleaned_data.get("name_en", None)
        return name_en

    def clean_level(self):
        level = self.cleaned_data.get("level", None)
        return level

    def clean(self):
        return super(CategoriesKlintbergForm, self).clean()

    def validate_unique(self):
        return super(CategoriesKlintbergForm, self).validate_unique()

    def save(self, commit=True):
        return super(CategoriesKlintbergForm, self).save(commit)


class RecordsPlacesForm(forms.ModelForm):

    class Meta:
        model = RecordsPlaces
        fields = ['record', 'place']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RecordsPlacesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RecordsPlacesForm, self).is_valid()

    def full_clean(self):
        return super(RecordsPlacesForm, self).full_clean()

    def clean_record(self):
        record = self.cleaned_data.get("record", None)
        return record

    def clean_place(self):
        place = self.cleaned_data.get("place", None)
        return place

    def clean(self):
        return super(RecordsPlacesForm, self).clean()

    def validate_unique(self):
        return super(RecordsPlacesForm, self).validate_unique()

    def save(self, commit=True):
        return super(RecordsPlacesForm, self).save(commit)


class RecordsForm(forms.ModelForm):

    class Meta:
        model = Records
        fields = ['title', 'text', 'year', 'category', 'archive', 'archive_id', 'type', 'archive_page', 'source', 'comment']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RecordsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RecordsForm, self).is_valid()

    def full_clean(self):
        return super(RecordsForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_text(self):
        text = self.cleaned_data.get("text", None)
        return text

    def clean_year(self):
        year = self.cleaned_data.get("year", None)
        return year

    def clean_category(self):
        category = self.cleaned_data.get("category", None)
        return category

    def clean_archive(self):
        archive = self.cleaned_data.get("archive", None)
        return archive

    def clean_archive_id(self):
        archive_id = self.cleaned_data.get("archive_id", None)
        return archive_id

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean_archive_page(self):
        archive_page = self.cleaned_data.get("archive_page", None)
        return archive_page

    def clean_source(self):
        source = self.cleaned_data.get("source", None)
        return source

    def clean_comment(self):
        comment = self.cleaned_data.get("comment", None)
        return comment

    def clean_changedate(self):
        changedate = self.cleaned_data.get("changedate", None)
        return changedate

    def clean(self):
        return super(RecordsForm, self).clean()

    def validate_unique(self):
        return super(RecordsForm, self).validate_unique()

    def save(self, commit=True):
        return super(RecordsForm, self).save(commit)


class MediaForm(forms.ModelForm):

    class Meta:
        model = Media
        fields = ['source', 'type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(MediaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(MediaForm, self).is_valid()

    def full_clean(self):
        return super(MediaForm, self).full_clean()

    def clean_source(self):
        source = self.cleaned_data.get("source", None)
        return source

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean(self):
        return super(MediaForm, self).clean()

    def validate_unique(self):
        return super(MediaForm, self).validate_unique()

    def save(self, commit=True):
        return super(MediaForm, self).save(commit)


class RecordsCategoryForm(forms.ModelForm):

    class Meta:
        model = RecordsCategory
        fields = ['record', 'category', 'level', 'type']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RecordsCategoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RecordsCategoryForm, self).is_valid()

    def full_clean(self):
        return super(RecordsCategoryForm, self).full_clean()

    def clean_record(self):
        record = self.cleaned_data.get("record", None)
        return record

    def clean_category(self):
        category = self.cleaned_data.get("category", None)
        return category

    def clean_level(self):
        level = self.cleaned_data.get("level", None)
        return level

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean(self):
        return super(RecordsCategoryForm, self).clean()

    def validate_unique(self):
        return super(RecordsCategoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(RecordsCategoryForm, self).save(commit)


class PersonsForm(forms.ModelForm):

    class Meta:
        model = Persons
        fields = ['name', 'gender', 'birth_year', 'address', 'biography', 'image', 'changedate']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PersonsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PersonsForm, self).is_valid()

    def full_clean(self):
        return super(PersonsForm, self).full_clean()

    def clean_firstname(self):
        firstname = self.cleaned_data.get("firstname", None)
        return firstname

    def clean_surname(self):
        surname = self.cleaned_data.get("surname", None)
        return surname

    def clean_gender(self):
        gender = self.cleaned_data.get("gender", None)
        return gender

    def clean_birth_year(self):
        birth_year = self.cleaned_data.get("birth_year", None)
        return birth_year

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_biography(self):
        biography = self.cleaned_data.get("biography", None)
        return biography

    def clean_image(self):
        image = self.cleaned_data.get("image", None)
        return image

    def clean_changedate(self):
        changedate = self.cleaned_data.get("changedate", None)
        return changedate

    def clean(self):
        return super(PersonsForm, self).clean()

    def validate_unique(self):
        return super(PersonsForm, self).validate_unique()

    def save(self, commit=True):
        return super(PersonsForm, self).save(commit)


class RecordsPersonsForm(forms.ModelForm):

    class Meta:
        model = RecordsPersons
        fields = ['record', 'person', 'relation']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RecordsPersonsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RecordsPersonsForm, self).is_valid()

    def full_clean(self):
        return super(RecordsPersonsForm, self).full_clean()

    def clean_record(self):
        record = self.cleaned_data.get("record", None)
        return record

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_relation(self):
        relation = self.cleaned_data.get("relation", None)
        return relation

    def clean(self):
        return super(RecordsPersonsForm, self).clean()

    def validate_unique(self):
        return super(RecordsPersonsForm, self).validate_unique()

    def save(self, commit=True):
        return super(RecordsPersonsForm, self).save(commit)


class PersonsPlacesForm(forms.ModelForm):

    class Meta:
        model = PersonsPlaces
        fields = ['person', 'place', 'relation']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PersonsPlacesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PersonsPlacesForm, self).is_valid()

    def full_clean(self):
        return super(PersonsPlacesForm, self).full_clean()

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean_place(self):
        place = self.cleaned_data.get("place", None)
        return place

    def clean_relation(self):
        relation = self.cleaned_data.get("relation", None)
        return relation

    def clean(self):
        return super(PersonsPlacesForm, self).clean()

    def validate_unique(self):
        return super(PersonsPlacesForm, self).validate_unique()

    def save(self, commit=True):
        return super(PersonsPlacesForm, self).save(commit)


class SockenV1Form(forms.ModelForm):

    class Meta:
        model = SockenV1
        fields = ['name', 'harad', 'lat', 'lng', 'changedate']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SockenV1Form, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SockenV1Form, self).is_valid()

    def full_clean(self):
        return super(SockenV1Form, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_harad(self):
        harad = self.cleaned_data.get("harad", None)
        return harad

    def clean_lat(self):
        lat = self.cleaned_data.get("lat", None)
        return lat

    def clean_lng(self):
        lng = self.cleaned_data.get("lng", None)
        return lng

    def clean_changedate(self):
        changedate = self.cleaned_data.get("changedate", None)
        return changedate

    def clean(self):
        return super(SockenV1Form, self).clean()

    def validate_unique(self):
        return super(SockenV1Form, self).validate_unique()

    def save(self, commit=True):
        return super(SockenV1Form, self).save(commit)


class RecordsMediaForm(forms.ModelForm):

    class Meta:
        model = RecordsMedia
        fields = ['record', 'media']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RecordsMediaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RecordsMediaForm, self).is_valid()

    def full_clean(self):
        return super(RecordsMediaForm, self).full_clean()

    def clean_record(self):
        record = self.cleaned_data.get("record", None)
        return record

    def clean_media(self):
        media = self.cleaned_data.get("media", None)
        return media

    def clean(self):
        return super(RecordsMediaForm, self).clean()

    def validate_unique(self):
        return super(RecordsMediaForm, self).validate_unique()

    def save(self, commit=True):
        return super(RecordsMediaForm, self).save(commit)


class SockenForm(forms.ModelForm):

    class Meta:
        model = Socken
        fields = ['name', 'harad', 'lat', 'lng']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(SockenForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(SockenForm, self).is_valid()

    def full_clean(self):
        return super(SockenForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_harad(self):
        harad = self.cleaned_data.get("harad", None)
        return harad

    def clean_lat(self):
        lat = self.cleaned_data.get("lat", None)
        return lat

    def clean_lng(self):
        lng = self.cleaned_data.get("lng", None)
        return lng

    def clean_changedate(self):
        changedate = self.cleaned_data.get("changedate", None)
        return changedate

    def clean(self):
        return super(SockenForm, self).clean()

    def validate_unique(self):
        return super(SockenForm, self).validate_unique()

    def save(self, commit=True):
        return super(SockenForm, self).save(commit)


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ['name', 'name_en']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CategoriesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CategoriesForm, self).is_valid()

    def full_clean(self):
        return super(CategoriesForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_name_en(self):
        name_en = self.cleaned_data.get("name_en", None)
        return name_en

    def clean(self):
        return super(CategoriesForm, self).clean()

    def validate_unique(self):
        return super(CategoriesForm, self).validate_unique()

    def save(self, commit=True):
        return super(CategoriesForm, self).save(commit)


class HaradForm(forms.ModelForm):

    class Meta:
        model = Harad
        fields = ['name', 'lan', 'landskap', 'country']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(HaradForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(HaradForm, self).is_valid()

    def full_clean(self):
        return super(HaradForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_lan(self):
        lan = self.cleaned_data.get("lan", None)
        return lan

    def clean_landskap(self):
        landskap = self.cleaned_data.get("landskap", None)
        return landskap

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean(self):
        return super(HaradForm, self).clean()

    def validate_unique(self):
        return super(HaradForm, self).validate_unique()

    def save(self, commit=True):
        return super(HaradForm, self).save(commit)

