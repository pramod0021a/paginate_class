from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile

# Create your views here.
class ProfileListView(ListView):
   template_name = 'core/index.html'
   paginate_by =3
   ordering = ['id']
   queryset = Profile.objects.all()
