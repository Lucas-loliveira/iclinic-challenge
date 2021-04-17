import requests

from prescriptions.serializers.client.settings import *
from prescriptions.serializers.client.base import BaseClient

class Metrics(BaseClient):
    base_url = None

    def __init__(self):
        self.base_url = BASE_URL

    def post_metrics(self, data):
        url = f'{self.base_url}{METRICS_URL}'
        result =  self._request_post(url, METRICS_TOKEN, METRICS_TIMEOUT, METRICS_RETRY, data)
        return result