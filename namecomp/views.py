# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import SubmissionForm

def index(request):
  message = ''
  if request.POST:
    form = SubmissionForm(request.POST)
    if form.is_valid():
      result = form.save()
      message = u"Ditt forslag er lagt inn, møt opp 2. september for å se om du vinner!"
    else:
      print form.errors
  else:
    form = SubmissionForm()
  return render(request, 'index.html', {'form': form, 'message': message})
