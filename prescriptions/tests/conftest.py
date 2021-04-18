import pytest 
import requests_mock
import requests_cache
from prescriptions.serializers.client.settings import *


@pytest.fixture(autouse=True)
def clear_cache():
    session = requests_cache.CachedSession('client_cache')
    session.cache.clear()


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def request_physician_success(requests_mock):
    url = f'{BASE_URL}{PHYSICIANS_URL}1'
    return requests_mock.get(url,
        json={
            "id": "1",
            "name": "Alysha Dibbert",
            "crm": "55efe166-8e8e-4969-a5b7-f07ca99e78a8"
        }
    )

@pytest.fixture
def request_clinic_success(requests_mock):
    url = f'{BASE_URL}{CLINICS_URL}1'
    return requests_mock.get(url,
        json={
            "id": "1",
            "name": "Lenny Farrell"
        }
    )

@pytest.fixture
def request_patient_success(requests_mock):
    url = f'{BASE_URL}{PATIENTS_URL}1'
    return requests_mock.get(url,
        json={
            "id": "1",
            "name": "Dr. Berry Howe",
            "email": "Janick92@hotmail.com",
            "phone": "580-544-7692 x90775"
        }
    )

@pytest.fixture
def request_metrics_success(requests_mock):
    url = f'{BASE_URL}{METRICS_URL}'
    return requests_mock.post(url,
        json={
            "patient_id": "1",
            "patient_name": "Dr. Berry Howe",
            "patient_email": "Janick92@hotmail.com",
            "patient_phone": "580-544-7692 x90775",
            "clinic_id": "1",
            "clinic_name": "Lenny Farrell",
            "physician_id": "1",
            "physician_name": "Alysha Dibbert",
            "physician_crm": "55efe166-8e8e-4969-a5b7-f07ca99e78a8"

        }
    )


@pytest.fixture
def request_patient_fail(requests_mock):
    url = f'{BASE_URL}{PATIENTS_URL}1'
    return requests_mock.get(url,
        status_code=404
    )

@pytest.fixture
def request_physician_fail(requests_mock):
    url = f'{BASE_URL}{PHYSICIANS_URL}1'
    return requests_mock.get(url,
        status_code=404
    )

@pytest.fixture
def request_metrics_fail(requests_mock):
    url = f'{BASE_URL}{METRICS_URL}'
    return requests_mock.post(url,
        status_code=500
    )

@pytest.fixture
def request_patient_status_500(requests_mock):
    url = f'{BASE_URL}{PATIENTS_URL}1'
    return requests_mock.get(url,
        status_code=500
    )

@pytest.fixture
def request_physician_status_500(requests_mock):
    url = f'{BASE_URL}{PHYSICIANS_URL}1'
    return requests_mock.get(url,
        status_code=500
    )
