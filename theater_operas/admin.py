from django.contrib import admin
from .models import Maestro, Work, Text, Part, Mention

admin.site.register(Maestro)
admin.site.register(Work)
admin.site.register(Text)
admin.site.register(Part)
admin.site.register(Mention)