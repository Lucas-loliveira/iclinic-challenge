from django.contrib import admin
from prescriptions.models import Prescription

class Prescriptions(admin.ModelAdmin):
    list_display = ('id','id_physician')
    list_display_links = ('id', 'id_physician')

admin.site.register(Prescription, Prescriptions)
