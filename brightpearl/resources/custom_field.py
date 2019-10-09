

class CustomField(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def get(self, product_id):
        custom_field_get = "product/{}/custom-field".format(product_id)
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, custom_field_get), "GET", {}
        )

    def patch(self, product_id, customer_fields):
        custom_field_get = "product/{}/custom-field".format(product_id)
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, custom_field_get), "PATCH", customer_fields
        )
