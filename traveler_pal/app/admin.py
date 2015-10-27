from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Scenery)
admin.site.register(Activity)
admin.site.register(ActivityScenery)
admin.site.register(Person)
admin.site.register(UserActivity)
admin.site.register(UserScenery)
admin.site.register(Comment)
admin.site.register(Journal)