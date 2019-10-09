from brightpearl.utils import url_encode_params


class Collection(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params):
        collection_list = "collection-search"

        product_list = "product-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, collection_list, url_encode_params(search_params)), "GET", {}
        )
