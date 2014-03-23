# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

#from polls.models import Poll, Choice

@login_required(login_url='/login/')
def index(request):
    return render(request, 'time/index.html')
