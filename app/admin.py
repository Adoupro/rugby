from django.contrib import admin
from app.models import ODS_Club, ODS_Licence
from app.models import D_Federation, D_Geography

admin.site.register(ODS_Club)
admin.site.register(ODS_Licence)

admin.site.register(D_Geography)
admin.site.register(D_Federation)