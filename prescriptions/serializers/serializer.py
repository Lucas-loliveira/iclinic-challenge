from requests.models import Response
from rest_framework import serializers
from prescriptions.models import Prescription
from prescriptions.serializers.validators import Validators
from prescriptions.serializers.metrics import Metrics
from django.db import transaction


class PrescriptionSerializer(serializers.ModelSerializer):
    metrics_data = {}
    validator = Validators()

    class Meta:
        model = Prescription
        fields =  '__all__'

    def validate(self, data):
        response_physician = self.validator.validate_physician(data['id_physician'])

        if isinstance(response_physician, Response):
            if response_physician.ok:
                for key, value in response_physician.json().items():
                    self.metrics_data[f'physician_{key}'] = value
            else:
                raise serializers.ValidationError({'error': {'message': "physician not found", 'code': "02"}})
        else:
            raise serializers.ValidationError({'error': {'message': "physicians service not available", 'code': "05"}})

        response_patient = self.validator.validate_patient(data['id_patient'])

        if isinstance(response_patient, Response):
            if response_patient.ok:
                for key, value in response_patient.json().items():
                    self.metrics_data[f'patient_{key}'] = value
            else:
                raise serializers.ValidationError({'error': {'message': "patient not found", 'code': "03"}})
        else:
            raise serializers.ValidationError({'error': {'message': "patients service not available", 'code': "06"}})

        response_clinic = self.validator.validate_clinic(data['id_clinic'])

        if isinstance(response_clinic, Response):
            if response_clinic.ok:
                for key, value in response_clinic.json().items():
                    self.metrics_data[f'clinic_{key}'] = value

        return data

    @transaction.atomic
    def create(self, validated_data):
        metrics_service = Metrics() 

        sid = transaction.savepoint()
        Prescription.objects.create(**validated_data)

        if metrics_service.post_metrics(self.metrics_data):  
            transaction.savepoint_commit(sid)
        else:
            transaction.savepoint_rollback(sid)
            raise serializers.ValidationError({'error': {'message': "metrics service not available", 'code': "04"}})

        return validated_data

