
class PriceList(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def get(self, price_list_ids=None):
        """
            Method to get the pricelist information for the price_list_ids.
        :param price_list_ids: (string)
        :return:
        """
        if not price_list_ids:
            price_list_ids = ""
        price_list_get = "price-list"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, price_list_get, price_list_ids), "GET", {}
        )
