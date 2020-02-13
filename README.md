## Brightpearl API Python Client

Wrapper over the requests library for communicating with the Brightpearl  API.

Usage
-----

- Brightpearl Auth flow
```bash
from brightpearl.api import BrightPearlAPI

# To get authorization URL
auth_url = api.authorization_url(authorization_redirect_url="http://localhost/redirect_url")

# To get access token
api.oauth_fetch_token(code="XYZ", access_redirect_url="http://localhost/access_redirect_url")

# To refresh token
api.refresh_token(refresh_token="<referesh_token>")

```

- Access Resources
```bash
from brightpearl.api import BrightPearlAPI

api = BrightPearlAPI(
    'client_id', "client_secret", False, "account", "domain",
    "access_token", "appref", "devref"
)

# get all products from brightpearl
products = api.Products.all()

# get specific product
product = api.Products.get(1035)

# remove product
api.Products.remove(1035)

```
