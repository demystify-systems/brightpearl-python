from brightpearl.utils import url_encode_params


class Brands(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, raw_response=False):
        brand_list = "brand-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, brand_list, url_encode_params(search_params)), "GET", {}, raw_response
        )

    def get(self, brand_id):
        brand_get = "brand"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, brand_get, brand_id), "GET", {}
        )

    def create(self, brand_info):
        brand_create = "brand"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, brand_create), "POST", data=brand_info
        )

    def update(self, brand_info):
        brand_update = "brand"
        return self.connection.make_request(
           "{}/{}/{}".format(self.resource_parent, brand_update, brand_info['id']), "PUT", data=brand_info
        )

    def remove(self, brand_id):
        brand_delete = "brand"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, brand_delete, brand_id), "DELETE", {}
        )

