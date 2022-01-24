from brightpearl.utils import url_encode_params

class OptionValue(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params= None, stream=False):
        """
            Method to get option_values from the brightpearl.
        :param stream: (boolean) - True if the data are to be streamed.
        :return:
        """
        option_value_list = "option-value-search"
        if not search_params:
            search_params = dict()
        return self.connection.make_request("/{}/{}/{}".format(
            self.resource_parent, option_value_list, url_encode_params(search_params)), "GET", {}, stream
        )

    def get(self, option_id):
        """
            Method to get the option_value information for the <option_id>
        :param option_id:
        :return:
        """
        option_value_get = "option"
        return self.connection.make_request(
            "{}/{}/{}/value".format(self.resource_parent, option_value_get, option_id), "GET", {}
        )

    def create(self, option_id, option_values):
        """
            Method to create the option value on the brightpeal
        :param option_id:
        :param option_values:
        :return:
        """
        option_value_create = "option"
        return self.connection.make_request(
            "{}/{}/{}/values".format(self.resource_parent, option_value_create, option_id), "POST", data=option_values
        )
