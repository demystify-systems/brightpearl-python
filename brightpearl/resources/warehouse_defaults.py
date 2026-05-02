from brightpearl.utils import url_encode_params
class WarehouseDefaults(object):

    def __init__(self, connection):
        self.resource_parent = 'warehouse-service'
        self.connection = connection

    def put(self, warehouse_id, bp_id,reqObj):
        warehouse_get = "warehouse"
        return self.connection.make_request(
            "{}/{}/{}/{}/{}".format(self.resource_parent, warehouse_get, str(warehouse_id), "product", bp_id), "PUT",
            data=reqObj
        )

    def get_default_location(self, warehouse_id=None):
        warehouse_get = "warehouse"
        return self.connection.make_request(
            "{}/{}/{}/{}/{}".format(self.resource_parent, warehouse_get, warehouse_id,"location","default"), "GET", {}
        )
