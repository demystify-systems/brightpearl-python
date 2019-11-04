

class OptionValue(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, stream=False):
        option_value_list = "option-value-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, option_value_list), "GET", {}, stream
        )

    def get(self, option_id):
        option_value_get = "option"
        return self.connection.make_request(
            "{}/{}/{}/value".format(self.resource_parent, option_value_get, option_id), "GET", {}
        )

    def create(self, option_id, option_values):
        option_value_create = "option"
        return self.connection.make_request(
            "{}/{}/{}/values".format(self.resource_parent, option_value_create, option_id), "POST", data=option_values
        )
