import requests


class BrightPearlAPI(object):
    def __init__(self, client_id , account, client_secret = None, redirect=None, ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.account = account
        self.redirect = redirect

    def oauth_fetch_token(self, code):
        request = {
            "grant_type" : "authorization_code",
            "code": code,
            "client_id": self.client_id,
        }
        url = "https://oauth.brightpearl.com/token/{}".format(self.account)
        return requests.post(url, request)