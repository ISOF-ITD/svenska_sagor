from django.contrib.admin.filters import RelatedFieldListFilter, AllValuesFieldListFilter 

class DropdownFilter(AllValuesFieldListFilter ):
    template = 'Sagenkarta-Admin/dropdown_filter.html'

class RelatedDropdownFilter(RelatedFieldListFilter ):
    template = 'Sagenkarta-Admin/dropdown_filter.html'