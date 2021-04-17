import requests
from requests.exceptions import ConnectionError

class BaseClient:

    def _get_session(self, token):
        session = requests.Session()
        session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': token,
        })
        return session


    def _request_get(self, url, token):
        session = self._get_session(token)
        try:
            response = session.get(url)
        except ConnectionError:
            return False

        return response


    def _request_post(self, url, token, **kwargs):
        session = self._get_session(token)
        return session.post(url, data, **kwargs)

