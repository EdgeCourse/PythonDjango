"""
from django.shortcuts import render
from .models import Band

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'bands/band_list.html', {'bands': bands})
"""
from django.shortcuts import render
from .models import Band

def band_list(request):
    bands = Band.objects.all().prefetch_related('members')  # Prefetch members
    return render(request, 'bands/band_list.html', {'bands': bands})    