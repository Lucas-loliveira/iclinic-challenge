import requests

from prescriptions.serializers.client.settings import *
from prescriptions.serializers.client.base import BaseClient


class Validators(BaseClient):
    base_url = None

    def __init__(self):
        self.base_url = BASE_URL
    
    def validate_physician(self, id_physician):
        url = f'{self.base_url}{PHYSICIANS_URL}{id_physician}'
        result =  self._request_get(url, PHYSICIANS_TOKEN, PHYSICIANS_TIMEOUT, PHYSICIANS_RETRY, PHYSICIANS_TTL)
        return result


    def validate_clinic(self, id_clinic):
        url = f'{self.base_url}{CLINICS_URL}{id_clinic}'
        return self._request_get(url, CLINICS_TOKEN, CLINICS_TIMEOUT, CLINICS_RETRY, CLINICS_TTL)


    def validate_patient(self, id_patient):
        url = f'{self.base_url}{PATIENTS_URL}{id_patient}'
        return self._request_get(url, PATIENTS_TOKEN, PATIENTS_TIMEOUT, PATIENTS_RETRY, PATIENTS_TTL)