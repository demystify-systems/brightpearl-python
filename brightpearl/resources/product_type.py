from brightpearl.utils import url_encode_params


class ProductType(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, stream=False):
        product_type__list = "product-type-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, product_type__list, url_encode_params(search_params)), "GET", {}, stream
        )

    def get(self, product_type_id):
        product_type_get = "product-type"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_type_get, product_type_id), "GET", {}
        )

    def create(self, product_type_info):
        product_type_create = "product-type"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, product_type_create), "POST", data=product_type_info
        )
