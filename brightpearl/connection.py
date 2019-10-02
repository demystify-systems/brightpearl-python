import requests
import logging
import json


class OauthConnection(object):
    def __init__(self, client_id, client_secret):
        self.resource_base_path = "https://{region}.brightpearl.com/public-api/{account_id}/{resource}"
        self._session = requests.Session()
        self.client_id = client_id
        self.client_secret = client_secret
        self._session.headers = {
            "Accept": "application/json",
            "Content - Type": "application / x - www - form - urlencoded"
        }

    def make_request(self, url, method, data):
        response = self._session.request(method, url, data=data)
        return self.process_response(response)

    @staticmethod
    def process_response(response):
        result = dict()
        if response.status_code in [200, 201, 202]:
            result = response.json()
        elif response.status_code >= 500:
            pass
        elif response.status_code >= 400:
            pass
        elif response.status_code >= 300:
            pass
        return result


class Connection(object):
    def __init__(self, region, account_id, access_token, developer_ref, app_ref):
        self.resource_base_path = "https://{region}.brightpearl.com/public-api/{account_id}/{resource}"
        self.region = region
        self.account_id = account_id
        self._session = requests.Session()
        self._session.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(access_token),
            "brightpearl-dev-ref": developer_ref,
            "brightpearl-app-ref": app_ref
        }

    def get_full_path(self, endpoint):
        return self.resource_base_path.format(
            **{"region": self.region, "account_id": self.account_id, "resource": endpoint}
        )

    def make_request(self, url, method, data):
        response = self._session.request(
            method=method, url=self.get_full_path(url), data=json.dumps(data)
        )
        return self.process_response(response)

    @staticmethod
    def process_response(response):
        result = dict()
        if response.status_code in [200, 201, 202]:
            result = response.json()
        else:
            raise ValueError("Error while fetching product: {}".format(response.text))
        return result
