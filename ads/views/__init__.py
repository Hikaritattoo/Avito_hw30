from ads.views.ad import AdListView, AdDetailView, AdUpdateView, AdImageView, AdDeleteView, AdCreateView
from ads.views.category import CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateView
from ads.views.location import LocationViewSet
from ads.views.selection import SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, SelectionDeleteView
from ads.views.index import index


__all__ = [
    'AdListView',
    'AdDetailView',
    'AdUpdateView',
    'AdImageView',
    'AdDeleteView',
    'AdCreateView',
    'CategoryListView',
    'CategoryDetailView',
    'CategoryUpdateView',
    'CategoryDeleteView',
    'CategoryCreateView',
    'LocationViewSet',
    'SelectionListView',
    'SelectionDetailView',
    'SelectionCreateView',
    'SelectionUpdateView',
    'SelectionDeleteView',
    'index',
]


