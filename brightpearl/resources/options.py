

class Options(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, stream=False):
        """
            Method to get all the options from the brightpearl platform.
        :param stream: (boolean) - True if the response has to be streamed.
        :return:
        """
        option_list = "option-search"
        return self.connection.make_request("/{}/{}".format(
            self.resource_parent, option_list), "GET", {}, stream
        )

    def get(self, option_id):
        option_get = "option"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, option_get, option_id), "GET", {}
        )

    def create(self, option_info):
        """
            Method to create the options on the brightpearl platform.
        :param option_info:
        :return:
        """
        option_create = "option"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, option_create), "POST", data=option_info
        )

    def update(self, option_info):
        """
            Method to update the options on the brightpearl.
        :param option_info: (dict)
        :return:
        """
        option_update = "option"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, option_update, option_info['id']), "PUT", data=option_info
        )

    def remove(self, option_id):
        """
            Method to delete the options from brightpearl
        :param option_id: (string) - Brightpeal option_id
        :return:
        """
        option_delete = "option"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, option_delete, option_id), "DELETE", {}
        )
