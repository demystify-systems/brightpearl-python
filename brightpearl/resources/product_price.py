
class ProductPrice(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def get(self, product_set_id, price_list_id=None):
        """
            Method to get the product_price information.
        :param product_set_id: (string)
        :param price_list_id: (string)
        :return:
        """
        product_price_list_get = "product-price"
        url = "{}/{}/{}".format(self.resource_parent, product_price_list_get, product_set_id)
        if price_list_id:
            url = "{}/price-list/{}".format(url, price_list_id)
        return self.connection.make_request(url, "GET", {})

    def update(self, product_id, price_list):
        product_price_update = "product-price"
        return self.connection.make_request(
            "{}/{}/{}/price-list".format(self.resource_parent, product_price_update, product_id), "PUT", data=price_list
        )

