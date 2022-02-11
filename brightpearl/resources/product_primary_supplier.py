from brightpearl.utils import url_encode_params

class ProductPrimarySupplier(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection


    def put(self, supplier_id, products_list):
        supplier_update = "product"
        supplier_id= supplier_id[0] if (isinstance(supplier_id, list) and len(supplier_id)>0) else supplier_id
        return self.connection.make_request(
            "{}/{}/{}/{}".format(self.resource_parent, "primary-supplier", supplier_id, supplier_update), "PUT", data=products_list
        )
