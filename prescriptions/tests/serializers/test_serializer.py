import pytest
from rest_framework import serializers
from prescriptions.serializers.serializer import PrescriptionSerializer


def test_serializer_physician_not_found(request_physician_fail, request_clinic_success, request_patient_success):
    serializer = PrescriptionSerializer()
    
    with pytest.raises(serializers.ValidationError):
        serializer.validate({'id_clinic':1,'id_physician':1, 'id_patient':1, 'text': 'test'})


def test_serializer_physician_service_not_avalible(request_physician_status_500, request_clinic_success, request_patient_success):
    serializer = PrescriptionSerializer()
    
    with pytest.raises(serializers.ValidationError):
        serializer.validate({'id_clinic':1,'id_physician':1, 'id_patient':1, 'text': 'test'})


def test_serializer_patient_service_not_avalible(request_physician_success, request_clinic_success, request_patient_status_500):
    serializer = PrescriptionSerializer()
    
    with pytest.raises(serializers.ValidationError):
        serializer.validate({'id_clinic':1,'id_physician':1, 'id_patient':1, 'text': 'test'})