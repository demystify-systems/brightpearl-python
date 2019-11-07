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
