from brightpearl.api import BrightPearlAPI

api = BrightPearlAPI(
    'client_id', "client_secret", False
)

# To get authorization URL
auth_url = api.authorization_url(authorization_redirect_url="http://localhost/redirect_url")

# To get access token
api.oauth_fetch_token(code="XYZ", access_redirect_url="http://localhost/access_redirect_url")

# To refresh token
api.refresh_token(refresh_token="<referesh_token>")
