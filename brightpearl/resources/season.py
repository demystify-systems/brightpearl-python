from brightpearl.utils import url_encode_params
class Season(object):

    def __init__(self, connection):
        self.resource_parent = 'product-service'
        self.connection = connection

    def all(self, search_params= None,stream=False):
        """
            Method to get all the seasoons data from the brightpearl.
        :param stream: (boolean) - True if results are supposed to be streamed.
        :return:
        """
        season_get = "season"
        if not search_params:
            search_params = dict()
        return self.connection.make_request(
            "{}/{}?{}".format(self.resource_parent, season_get,  url_encode_params(search_params)), "GET", {}, stream
        )

    def get(self, season_id):
        season_get = "season"
        return self.connection.make_request(
            "{}/{}/{}".format(self.resource_parent, season_get, season_id), "GET", {}
        )

    def create(self, season_info):
        season_create = "season"
        return self.connection.make_request(
            "{}/{}".format(self.resource_parent, season_create), "POST", data=season_info
        )
