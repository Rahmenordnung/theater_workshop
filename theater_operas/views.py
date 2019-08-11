from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Work, Part, Text

def works_list(request):
  # display all of the theater_work
  queryset = Work.objects.all()         
  context = {
    'queryset': queryset
  }
  return render(request, "works_list.html", context)

def works_detail(request, slug):
  # display some details of the work presented
  work = get_object_or_404(Work, slug=slug)
  context = {
    'work': work
  }
  return render(request, "work_detail.html", context)

def part_detail(request, work_slug, part_number):
  part_qs = Part.objects \
    .filter(work__slug=work_slug) \
    .filter(part_number=part_number)
  if part_qs.exists():
    context = {
      'part': part_qs[0] 
    }
    return render(request, "part_detail.html", context)
  return Http404

def text_detail(request, work_slug, part_number, text_number):
  text_qs = Text.objects \
    .filter(part__work__slug=work_slug) \
    .filter(part__part_number=part_number) \
    .filter(text_number = text_number)
  if text_qs.exists():
    context = {
      'text': text_qs[0] 
    }
    return render(request, "text_detail.html", context)
  return Http404    
  
  
        