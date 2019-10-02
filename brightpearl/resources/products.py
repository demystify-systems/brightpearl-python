

class Products(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self):
        product_list = "product-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, product_list), "GET", {}
        )

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

    def update(self, product_info):
        product_update = "product"
        return self.connection.make_request(
           "{}/{}/{}".format(self.resource_parent, product_update, product_info['id']), "PUT", data=product_info
        )

    def remove(self, product_id):
        product_delete = "product"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, product_delete, product_id), "DELETE", {}, {}
        )

