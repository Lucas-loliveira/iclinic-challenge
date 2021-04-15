from rest_framework import serializers
from prescriptions.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields =  '__all__'
