from brightpearl.utils import url_encode_params


class Brands(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params=None, stream=False):
        """
            Method to get all the Brands from the brightpearl.
        :param search_params: (dict) - search filter that is supposed to applied.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
        brand_list = "brand-search"

        if not search_params:
            search_params = dict()

        return self.connection.make_request("/{}/{}?{}".format(
            self.resource_parent, brand_list, url_encode_params(search_params)), "GET", {}, stream
        )

    def get(self, brand_id):
        """
            Method to get the brand information for a brand with <brand_id>
        :param brand_id: (string) - Brand id for which information is needed.
        :return:
        """
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
        """
            Method to update the brand information
        :param brand_info: (dict) - Brand information dictionary.
        :return:
        """
        brand_update = "brand"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, brand_update, brand_info['id']), "PUT", data=brand_info
        )

    def remove(self, brand_id):
        """
            Method to delete the brand from the brightpearl
        :param brand_id: (String) - Brand Id which is supposed to be deleted.
        :return:
        """
        brand_delete = "brand"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, brand_delete, brand_id), "DELETE", {}
        )
