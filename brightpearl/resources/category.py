from brightpearl.utils import url_encode_params


class Category(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, raw_response=False):
        category_list = "brightpearl-category-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, category_list, url_encode_params(search_params)), "GET", {}, raw_response
        )

    def get(self, category_id):
        category_get = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, category_get, category_id), "GET", {}
        )

    def create(self, category_info):
        category_create = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, category_create), "POST", data=category_info
        )
