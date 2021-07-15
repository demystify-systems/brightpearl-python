from brightpearl.utils import url_encode_params


class Products(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, stream=False):
        """
            Method to get all the Products from the Brightpearl.
         :param search_params: (dict) - search filter that is supposed to applied.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
        product_list = "product-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, product_list, url_encode_params(search_params)), "GET", {}, stream
        )

    
    def fetch_all_urls(self):
        """
        Method to get all the Products from the Brightpearl.
        https://api-docs.brightpearl.com/product/product/options.html
        :return:
        """
        product_list = "product"


        return self.connection.make_request("/product-service/product/", "OPTIONS", {})

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

    def update(self, product_info, product_version=None):
        product_update = "product"
        update_header = None
        if product_version:
            update_header = {
                "if-match": product_version
            }
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_update, product_info['id']), "PUT", data=product_info,
            headers=update_header
        )

    def remove(self, product_id):
        product_delete = "product"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_delete, product_id), "DELETE", {}, {}
        )
