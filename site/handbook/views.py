from django.db.models import F
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import *
