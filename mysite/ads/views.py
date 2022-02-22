from django.shortcuts import render
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Create your views here.
class AdListView(OwnerListView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad