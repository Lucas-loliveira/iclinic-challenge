import pytest
from requests.models import Response
from prescriptions.serializers.validators import Validators


def test_connection_validators():
    validator = Validators()
    response_physician = validator.validate_physician('1')
    response_clinics = validator.validate_clinic('1')
    response_patients = validator.validate_patient('1')

    assert isinstance(response_physician, Response)
    assert isinstance(response_clinics, Response)
    assert isinstance(response_patients, Response)
