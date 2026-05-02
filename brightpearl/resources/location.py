from brightpearl.utils import url_encode_params
class Location(object):
    def __init__(self, connection):
        self.resource_parent = 'warehouse-service'
        self.connection = connection

    def get(self, warehouse_id):
        warehouse_get = "warehouse"
        return self.connection.make_request(
            "{}/{}/{}/{}".format(self.resource_parent, warehouse_get, str(warehouse_id), "location"), "GET"
        )
