from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Task)
admin.site.register(models.GenLink)
admin.site.register(models.Notification)
admin.site.register(models.Section)
admin.site.register(models.Address)
admin.site.register(models.Position)
