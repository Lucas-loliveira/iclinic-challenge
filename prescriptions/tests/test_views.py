import pytest
import json
from django.urls import reverse
from rest_framework import status
import requests_mock
from prescriptions.serializers.client.settings import *

@pytest.mark.django_db(transaction=True)
def test_prescription(api_client, requests_mock, request_physician_success, request_clinic_success, request_patient_success, request_metrics_success):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patient': {
            'id': 1
        },
        'text': 'Dipirona 1x ao dia'
    }
    
    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))
    assert response.status_code == status.HTTP_201_CREATED



@pytest.mark.django_db(transaction=True)
def test_prescription_missing_required_field(api_client):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'text': 'Dipirona 1x ao dia'
    }

    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))

    data_response = response.data.get('error',{})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert data_response.get('message') == "malformed request"
    assert data_response.get('code') == "01"


@pytest.mark.django_db(transaction=True)
def test_prescription_wrong_type(api_client):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patient': {
            'id': 'wrong_type'
        },
        'text': 'Dipirona 1x ao dia'
    }
    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

@pytest.mark.django_db(transaction=True)
def test_prescription_patient_not_found(api_client, request_physician_success, request_clinic_success, request_patient_fail, request_metrics_success):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patient': {
            'id': 1
        },
        'text': 'Dipirona 1x ao dia'
    }
    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    
@pytest.mark.django_db(transaction=True)
def test_prescription_metrics_not_available(api_client, request_physician_success, request_clinic_success, request_patient_success, request_metrics_fail):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patient': {
            'id': 1
        },
        'text': 'Dipirona 1x ao dia'
    }
    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))

    assert response.status_code == status.HTTP_400_BAD_REQUEST