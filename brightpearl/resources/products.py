from brightpearl.utils import url_encode_params


class Products(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, raw_response=False):
        product_list = "product-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?".format(
            self.resource_parent, product_list, url_encode_params(search_params)), "GET", {}, raw_response
        )

    def get(self, product_id):
        product_get = "product"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_get, product_id), "GET", {}
        )

    def create(self, product_info):
        product_create = "product"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, product_create), "POST", data=product_info
        )

    def update(self, product_info):
        product_update = "product"
        return self.connection.make_request(
           "{}/{}/{}".format(self.resource_parent, product_update, product_info['id']), "PUT", data=product_info
        )

    def remove(self, product_id):
        product_delete = "product"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_delete, product_id), "DELETE", {}, {}
        )

