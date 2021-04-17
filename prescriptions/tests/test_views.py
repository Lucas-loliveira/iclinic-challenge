import pytest
import json
from django.urls import reverse
from rest_framework import status


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db(transaction=True)
def test_prescription(api_client):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patient': {
            'id': 3
        },
        'text': 'Dipirona 1x ao dia'
    }

    response = api_client.post('/prescriptions/',content_type='application/json', data=json.dumps(data))
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db(transaction=True)
def test_prescription_miss_required_field(api_client):
    data = {
        'clinic': {
            'id': 1
        },
        'physician': {
            'id': 1
        },
        'patien1t': {
            'id': 3
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

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    