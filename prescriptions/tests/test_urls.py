from django.urls import reverse, resolve


class TestUrls:
    def test_prescriptions_url(self):
        
        path = reverse('prescriptions-list')
        assert resolve(path).view_name == 'prescriptions-list'

