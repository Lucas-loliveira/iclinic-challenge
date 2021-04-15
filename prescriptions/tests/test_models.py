from mixer.backend.django import mixer
from prescriptions.models import Prescription
import pytest 


@pytest.mark.django_db
class TestModels:

    def test_prescriptions(self):
        prescription = mixer.blend('prescriptions.Prescription')
        assert isinstance(prescription, Prescription)
        