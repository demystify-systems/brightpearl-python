import logging
import sys
from urllib.parse import urlencode
import requests


from brightpearl.connection import Connection, OauthConnection
from brightpearl.resources import (  # noqa F401
    Products, Brands, ProductType, Category, Options, Collection, Season, OptionValue, CustomField,  # noqa F401
    PriceList, ProductPrice  # noqa F401
)  # noqa F401


log = logging.getLogger("brightpearl.api")


class BrightPearlAPI(object):
    def __init__(
            self, client_id=None, client_secret=None, oauth=False, account_id=None, domain=None, access_token=None,
            developer_ref=None, app_ref=None, protocol="https", rate_limit_management=None
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.account = account_id
        self.access_token = access_token
        self.domain = domain
        self.developer_ref = developer_ref
        self.app_ref = app_ref
        self.oauth = oauth
        if oauth:
            self.connection = OauthConnection(self.client_id, self.client_secret, protocol=protocol)
        else:
            self.connection = Connection(
                domain, account_id, access_token, developer_ref, app_ref, protocol=protocol,
                rate_limit_management=rate_limit_management
            )

    def authorization_url(self, authorization_redirect_url):
        """
            Method to generate the Authorization url.
        :return: (string) - url to be called for getting authorization token.
        """
        query_params = dict({
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": authorization_redirect_url,
            "state": "random"
        })
        return "https://oauth.brightpearl.com/authorize/{}?{}".format(self.account, urlencode(query_params))

    def oauth_fetch_token(self, code, access_redirect_url):
        """
            Method to get access token from the Authorization Code.
        :param code: (string) - Authorization code returned by Brightpearl upon authorization.
        :param access_redirect_url: (string)
        :return: Brightpearl response Object
        """
        request_body = dict({
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "redirect_uri": access_redirect_url
        })
        response = requests.request(
            method="POST", url="https://oauth.brightpearl.com/token/{}".format(self.account),
            data=request_body)
        data = response.json()
        return data

    def refresh_token(self, refresh_token):
        if self.oauth:
            raise ValueError("Refresh token can't be triggered as connection initialized for oauth connection")
        request_body = dict({
            "grant_type": 'refresh_token',
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        })

        response = requests.request(
            method="POST", url="https://oauth.brightpearl.com/token/{}".format(self.account),
            data=request_body)
        data = response.json()
        if "access_token" not in data:
            raise ValueError("Expected 'access_token' in the response of refresh_token")
        self.access_token = data["access_token"]
        self.connection = Connection(self.domain, self.account, self.access_token, self.developer_ref, self.app_ref)
        return data

    def __getattr__(self, item):
        return ResourceWrapper(item, self.connection)


class ResourceWrapper(object):
    def __init__(self, resource_cls, conn_obj):
        self.conn_obj = conn_obj
        self.resource_class = self.str_to_class(resource_cls)

    def __getattr__(self, item):
        return lambda *args, **kwargs: (getattr(self.resource_class(self.conn_obj), item))(*args, **kwargs)

    @classmethod
    def str_to_class(cls, resource):
        return getattr(sys.modules[__name__], resource)
