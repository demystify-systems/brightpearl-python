

class Options(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, raw_response=False):
        option_list = "option-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, option_list), "GET", {}, raw_response
        )

    def get(self, option_id):
        option_get = "option"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, option_get, option_id), "GET", {}
        )

    def create(self, option_info):
        option_create = "option"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, option_create), "POST", data=option_info
        )

    def update(self, option_info):
        option_update = "option"
        return self.connection.make_request(
           "{}/{}/{}".format(self.resource_parent, option_update, option_info['id']), "PUT", data=option_info
        )

    def remove(self, option_id):
        option_delete = "option"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, option_delete, option_id), "DELETE", {}
        )

