import requests
from urllib.parse import urlencode
import logging

log = logging.getLogger("brightpearl.api")


class BrightPearlAPI(object):
    def __init__(self, client_id, account, client_secret=None, redirect=None):
        """
            Method to initialise BrightPearlAPI Class
        :param client_id: (string) - Apps clientId on Brightpearl Portal
        :param account: (string) - Account Name which is installing app.
        :param client_secret: (string) - Apps client secret.
        :param redirect: (string) - Redirect Url
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.account = account
        self.redirect = redirect

    def oauth_fetch_token(self, code, redirect_uri):
        """
            Method to get access token from the Authorization Code.
        :param code: (string) - Authorization code returned by Brightpearl upon authorization.
        :param redirect_uri: (string)
        :return: Brightpearl response Object
        """
        request_param = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "redirect_uri": redirect_uri
        }
        url = "https://oauth.brightpearl.com/token/{}".format(self.account)
        log.debug("Calling " + url)
        return requests.post(url, data=request_param)
