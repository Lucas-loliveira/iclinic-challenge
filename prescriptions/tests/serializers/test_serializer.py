import pytest
from django.test import TestCase
from mixer.backend.django import mixer
from prescriptions.models import Prescription
from prescriptions.serializers.serializer import PrescriptionSerializer

class PrescriptionSerializerTestCase(TestCase):

    def setUp(self):
        self.prescriptions = mixer.blend('prescriptions.Prescription')
        self.serializer = PrescriptionSerializer(instance=self.prescriptions)

    def test_serialized_data(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','id_clinic', 'id_physician', 'id_patient', 'text'] ))

