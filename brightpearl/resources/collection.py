

class Collection(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self):
        collection_list = "collection-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, collection_list), "GET", {}
        )
