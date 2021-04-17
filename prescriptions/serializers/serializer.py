from requests.models import Response
from rest_framework import serializers
from prescriptions.models import Prescription
from prescriptions.serializers.validators import Validators


class PrescriptionSerializer(serializers.ModelSerializer):
    metrics_data = {}
    validator = Validators()

    class Meta:
        model = Prescription
        fields =  '__all__'

    def validate_id_physician(self, id_physician):
        response_physician = self.validator.validate_physician(id_physician)

        if isinstance(response_physician, Response):
            if response_physician.ok:
                for key, value in response_physician.json().items():
                    self.metrics_data[f'physician_{key}'] = value
            else:
                raise serializers.ValidationError({'error': {'message': "physician not found", 'code': "02"}})
        else:
            raise serializers.ValidationError({'error': {'message': "physicians service not available", 'code': "05"}})

        return id_physician


    def validate_id_patient(self, id_patient):
        response_patient = self.validator.validate_patient(id_patient)

        if isinstance(response_patient, Response):
            if response_patient.ok:
                for key, value in response_patient.json().items():
                    self.metrics_data[f'patient_{key}'] = value
            else:
                raise serializers.ValidationError({'error': {'message': "patient not found", 'code': "03"}})
        else:
            raise serializers.ValidationError({'error': {'message': "patients service not available", 'code': "06"}})
        
        return id_patient

    def validate_id_clinic(self, id_clinic):
        response_clinic = self.validator.validate_clinic(id_clinic)

        if isinstance(response_clinic, Response):
            if response_clinic.ok:
                for key, value in response_clinic.json().items():
                    self.metrics_data[f'clinic_{key}'] = value
        return id_clinic
