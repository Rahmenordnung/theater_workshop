from django.db import models
from django.shortcuts import redirect, reverse

# Maestro 
#     Opera
#       Part     
#         Text       
#           Mention1            
#           Mention2           
  
  
class Maestro(models.Model):
  complete_name = models.CharField(max_length=50)
  country_maestro = models.CharField(max_length=50)
  slug = models.SlugField()
  
  def __str__(self):
    return f"{self.complete_name} {self.country_maestro}"
  
class Work(models.Model):
  maestros = models.ManyToManyField(Maestro)
  title = models.CharField(max_length=50)
  publication_date = models.DateTimeField()
  gendre = models.CharField(max_length=30)
  slug = models.SlugField()
  cover = models.ImageField()
  price = models.FloatField()
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("theater_operas:works_detail", kwargs={'slug': self.slug })
  
class Part(models.Model):
  work = models.ForeignKey(Work, on_delete=models.CASCADE)
  part_number = models.IntegerField()
  title = models.CharField(max_length=50)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("theater_operas:part-detail", kwargs={'work_slug': self.work.slug, 'part_number': self.part_number }) 

class Text(models.Model):
  part = models.ForeignKey(Part, on_delete=models.CASCADE)
  text_number = models.IntegerField()
  text_page_number = models.IntegerField()
  title = models.CharField(max_length=50)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse("theater_operas:text_detail", kwargs={'work_slug': self.part.work.slug, 'part_number': self.part.part_number, 'text_number': self.text_number })
class Mention(models.Model):
  text = models.ForeignKey(Text, on_delete = models.CASCADE)
  image = models.ImageField()
  
  def __str__(self):
    return f"{self.text.title}-{self.pk}"   
            