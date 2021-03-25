import requests
import ast


class ConfigHttp:
    """
        配置http请求
    """
    # 处理get请求
    def get_handler(self, url, data):
        result = requests.get(url=url, params=data)
        return result

    # 处理post请求
    def post_handler(self, url, data):
        result = requests.post(url=url, data=data)
        return result

    # 处理put请求
    def put_handler(self, url, data):
        result = requests.put(url=url, data=data)
        return result

    # 根据请求类型，处理对应请求
    def run_main(self, method, url, data):
        # ast.literal_eval(data) 将数据转换为json格式
        if method == "get" or method == "GET":
            result = self.get_handler(url=url, data=ast.literal_eval(data))
        elif method == "post" or method == "POST":
            result = self.post_handler(url=url, data=ast.literal_eval(data))
        elif method == "put" or method == "PUT":
            result = self.post_handler(url=url, data=ast.literal_eval(data))
        else:
            raise Exception("unexpected method!")
        return result
