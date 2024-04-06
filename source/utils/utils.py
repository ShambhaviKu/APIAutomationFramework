# collection of headers

class Util(object):
    def common_headers_json(self):
        Header = {"Content-Type": "application/json"}
        return Header

    def common_headers_xml(self):
        Header = {"Content-Type": "application/xml"}
        return Header

    # put, patch, delete --> HEADERS

    def put_patch_delete_headers_cookie(self, token):
        Header = {"Content-Type": "application/json",
                  "cookie": "token=" + str(token)
                  }
        return Header

    def put_patch_delete_headers_basicAuth(self, basicAuthValue):
        Header = {"Content-Type": "application/json",
                  "Authorization": "Basic" + str(basicAuthValue)
                  }
        return Header

    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass
