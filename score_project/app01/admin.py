from django.contrib import admin
from app01 import models
# Register your models here.
#from app01 import account_admin


admin.site.register(models.BaseInfo)
admin.site.register(models.ServerInfo)
admin.site.register(models.ServerPlugin)
admin.site.register(models.DockerInfo)
