from brightpearl.utils import url_encode_params
class StockCorrection(object):
    def __init__(self, connection):
        self.resource_parent = 'warehouse-service'
        self.connection = connection

    def update(self, warehouse_id, req_obj):
        warehouse_get = "warehouse"
        return self.connection.make_request(
            "{}/{}/{}/{}".format(self.resource_parent, warehouse_get, str(warehouse_id), "stock-correction"), "POST", data = req_obj
        )
