from brightpearl.utils import url_encode_params


class Category(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, stream=False):
        """
            Method to get all the category from the brightpearl.
         :param search_params: (dict) - search filter that is supposed to applied.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
        category_list = "brightpearl-category-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, category_list, url_encode_params(search_params)), "GET", {}, stream
        )

    def get(self, category_id):
        """
            Method to get the category information for the category_id.
        :param category_id: (string)
        :return:
        """
        category_get = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, category_get, category_id), "GET", {}
        )

    def create(self, category_info):
        category_create = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, category_create), "POST", data=category_info
        )
