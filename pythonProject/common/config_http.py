import requests
import ast


class ConfigHttp:
    def get_handler(self, url, data):
        result = requests.get(url=url, params=data)
        return result

    def post_handler(self, url, data):
        result = requests.post(url=url, data=data)
        return result

    def put_handler(self, url, data):
        result = requests.put(url=url, data=data)
        return result

    def run_main(self, method, url, data):
        if method == "get" or method == "GET":
            result = self.get_handler(url=url, data=ast.literal_eval(data))
        elif method == "post" or method == "POST":
            result = self.post_handler(url=url, data=ast.literal_eval(data))
        elif method == "put" or method == "PUT":
            result = self.post_handler(url=url, data=ast.literal_eval(data))
        else:
            raise Exception("unexpected method!")
        return result
