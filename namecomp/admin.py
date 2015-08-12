from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
  list_display = ('name_proposal', 'name', 'email')
  search_fields = ('name', 'name_proposal', 'email', 'phone')
