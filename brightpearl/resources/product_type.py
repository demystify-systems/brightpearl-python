from brightpearl.utils import url_encode_params


class ProductType(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, stream=False):
        """
            Method to get all product type from the brightpearl platform.
        :param search_params: (dict) - search filter that is supposed to applied.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
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
        """
            Method to create the product type on the brightpearl
        :param product_type_info: (dict) - Dict of the product type that has to be updated.
        :return:
        """
        product_type_create = "product-type"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, product_type_create), "POST", data=product_type_info
        )
