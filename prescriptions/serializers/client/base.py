import requests
from requests.exceptions import ConnectionError
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


DEFAULT_TIMEOUT = 5 # seconds

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class BaseClient:

    def _get_session(self, token):
        session = requests.Session()
        session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': token,
        })
        return session


    def _request_get(self, url, token, timeout = 5, retry = 7):
        session = self._get_session(token)

        adapter_time = TimeoutHTTPAdapter(timeout=timeout)
        adapter_retry = HTTPAdapter(max_retries=Retry(total=retry))

        session.mount("https://", adapter_retry)
        session.mount("https://", adapter_time)
       
        try:
            response = session.get(url)
            
        except ConnectionError:
            return False

        return response

    def _request_post(self, url, token, timeout = 5, retry = 5, **kwargs,):
        session = self._get_session(token)

        adapter_time = TimeoutHTTPAdapter(timeout=timeout)
        adapter_retry = HTTPAdapter(max_retries=Retry(total=retry))

        session.mount("https://", adapter_retry)
        session.mount("https://", adapter_time)
       
        try:
            response = session.post(url, **kwargs)
            
        except ConnectionError:
            return False

        return response


