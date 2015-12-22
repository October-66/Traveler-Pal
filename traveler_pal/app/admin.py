from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Scenery)
admin.site.register(Activity)
admin.site.register(ActivityScenery)
admin.site.register(Person)
admin.site.register(PersonActivity)
admin.site.register(PersonScenery)