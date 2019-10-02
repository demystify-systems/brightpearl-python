

class Category(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self):
        category_list = "brightpearl-category-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, category_list), "GET", {}
        )

    def get(self, category_id):
        category_get = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, category_get, category_id), "GET", {}
        )

    def create(self, category_info):
        category_create = "brightpearl-category"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, category_create), "POST", data=category_info
        )
