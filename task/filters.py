import django_filters
from .models import *

class SearchForm( django_filters.FilterSet):
    class Meta:
        model = Task
        fields  = "__all__" 