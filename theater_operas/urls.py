from django.urls import path
from .views import works_list, works_detail, part_detail, text_detail

app_name = 'theater_operas'

urlpatterns = [
  path('', works_list, name='works_list'),
  path('<slug>/', works_detail, name='works_detail'),
  path('<work_slug>/<part_number>', part_detail, name='part-detail'),
  path('<work_slug>/<part_number>/<text_number>/', text_detail, name='text_detail'),
  
]
