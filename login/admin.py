from django.contrib import admin
from .models import Criminal, CriminalUpdate, Missing, PoliceDetail, Report, ReportUpdate
# Register your models here.

admin.site.register(Criminal)
admin.site.register(Missing)
admin.site.register(Report)
admin.site.register(ReportUpdate)
admin.site.register(CriminalUpdate)
admin.site.register(PoliceDetail)
