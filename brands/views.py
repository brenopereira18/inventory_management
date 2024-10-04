from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from . import models


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name_icontains=name)
        
        return queryset