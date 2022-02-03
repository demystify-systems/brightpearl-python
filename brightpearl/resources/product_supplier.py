from brightpearl.utils import url_encode_params

class ProductSupplier(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def get(self, product_set_id):
        """
            Method to get the product_price information.
        :param product_set_id: (string)
        :param price_list_id: (string)
        :return:
        """
        supplier_get = "supplier"

        if product_set_id:
            url = "{}/{}/{}/{}".format(self.resource_parent, "product", product_set_id, supplier_get)
        return self.connection.make_request(url, "GET", {})



    def update(self, product_id, supplier_list):
        supplier_update = "supplier"
        return self.connection.make_request(
            "{}/{}/{}/{}".format(self.resource_parent, "product", product_id, supplier_update), "POST", data=supplier_list
        )


