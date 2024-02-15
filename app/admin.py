from django.contrib import admin
from app.models import ODS_Club, ODS_Licence
from app.models import D_Sexe, D_Federation, D_Geography, D_Age_Group, D_Club_Type, D_Date
from app.models import F_Club, F_Licence

admin.site.register(ODS_Club)
admin.site.register(ODS_Licence)

admin.site.register(D_Geography)
admin.site.register(D_Sexe)
admin.site.register(D_Federation)
admin.site.register(D_Age_Group)
admin.site.register(D_Club_Type)
admin.site.register(D_Date)

admin.site.register(F_Club)
admin.site.register(F_Licence)