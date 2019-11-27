import requests
import json

from time import sleep

from brightpearl.exceptions import TokenExpiredException, RateLimitException


class OauthConnection(object):
    def __init__(self, client_id, client_secret, protocol="https"):
        self.resource_base_path = protocol + "://{domain}/public-api/{account_id}/{resource}"
        self._session = requests.Session()
        self.client_id = client_id
        self.client_secret = client_secret
        self._session.headers = {
            "Accept": "application/json",
            "Content - Type": "application/x-www-form-urlencoded"
        }

    def make_request(self, url, method, data=None):
        if not data:
            data = dict()
        response = self._session.request(method, url, data=data)
        return self.process_response(response)

    @staticmethod
    def process_response(response):
        result = dict()
        if response.status_code in [200, 201, 202]:
            result = response.json()
        else:
            raise ValueError("Error while making api request: {}".format(response.text))
        return result


class Connection(object):
    def __init__(
            self, domain, account_id, access_token, developer_ref, app_ref, protocol="https", rate_limit_management=None
    ):
        self.resource_base_path = protocol + "://{domain}/public-api/{account_id}/{resource}"
        self.domain = domain
        self.account_id = account_id
        self._session = requests.Session()
        self.rate_limit_management = rate_limit_management
        self._session.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(access_token),
            "brightpearl-dev-ref": developer_ref,
            "brightpearl-app-ref": app_ref
        }

    def get_full_path(self, endpoint):
        """
            Method to prepare the full URL for which connection object has to send the request
        :param endpoint: (string) -
        :return:
        """
        return self.resource_base_path.format(
            **{"domain": self.domain, "account_id": self.account_id, "resource": endpoint}
        )

    def make_request(self, url, method, data=None, stream=False):
        if not data:
            data = dict()
        response = self._session.request(
            method=method, url=self.get_full_path(url), data=json.dumps(data), stream=stream
        )
        return self.process_response(response, stream)

    def rate_limiting(self, headers):
        """
            Method to manage rate limiting
        :param headers: (dict) - Response headers.
        :return:
        """
        if 'brightpearl-requests-remaining' in headers:
            # check if the min_requests_remaining are lesser than requests_remaining
            if self.rate_limit_management['min_requests_remaining'] <= self.rate_limit_management['requests_remaining']:
                if self.rate_limit_management['wait']:
                    sleep(headers['brightpearl-next-throttle-period'] / 1000)
                if self.rate_limit_management.get('callback_function'):
                    callback = self.rate_limit_management['callback_function']
                    args_dict = self.rate_limit_management.get('callback_args')
                    if args_dict:
                        callback(args_dict)
                    else:
                        callback()

    def process_response(self, response, stream):
        """
            Method to process the responses from the brightpearl.
        :param response: (object)
        :param stream: (boolean)
        :return:
        """
        result = dict()
        if response.status_code in [200, 201, 202]:
            self.rate_limiting(response.headers)
            if not stream:
                result = response.json()
            else:
                return response
        elif response.status_code == 401:
            raise TokenExpiredException("Token expired")
        elif response.status_code == 429:
            raise RateLimitException("Rate limit :{}".format(response.text))
        else:
            raise ValueError("Error while fetching : {}".format(response.text))
        return result
