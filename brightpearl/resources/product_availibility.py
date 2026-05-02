from brightpearl.utils import url_encode_params
class ProductAvailibility(object):

    def __init__(self, connection):
        self.resource_parent = 'warehouse-service'
        self.connection = connection

    def get_product_availibility(self, product_id_set= None):
        """
            Method to get all the warehouse data from the brightpearl.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
        warehouse_get = "product-availability"
        data  = self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, warehouse_get, product_id_set), "GET", {}
        )
        return data

