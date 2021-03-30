import unittest
from bson import ObjectId
from parameterized import parameterized
from common.config_http import ConfigHttp
from common.read_excel import ReadExcel
from common.read_config import ReadConfig
from common.config_db import ConfigMongodb

profile_xls = ReadExcel().get_xls('userCases.xls', 'Sheet2')  # 读取userCases表中的sheet2工作表

client = ConfigMongodb("123.206.217.183", "milu", "KuJ9i_of3hU_dGz3d", "mintmuse")  # 创建数据库连接对象


class TestProfile(unittest.TestCase):
    @parameterized.expand(profile_xls)  # 用于参数化的装饰器
    def test_profile(self, case_name, path, data, method):
        base_url = ReadConfig().get_base_url()
        new_url = base_url + path
        resp = ConfigHttp().run_main(method=method, url=new_url, data=data)
        # 断言状态码：200
        self.assertEqual(resp.status_code, 200)
        # 将响应内容转为字典
        body = resp.json()
        # 将字符串转换为字典
        data = eval(data)
        instrument = data["instrumentName"].lower()
        product_beginner = "course." + instrument + ".beginner"
        product_intermediate = "course." + instrument + ".intermediate"
        # mongodb查询语句
        beginner = {
            "_id": ObjectId(data["userId"]),
            "courseProductId": product_beginner,
            "transactionType": "course"
        }
        intermediate = {
            "_id": ObjectId(data["userId"]),
            "courseProductId": product_intermediate,
            "transactionType": "course"
        }
        result_1 = client.search_to_boolean("transactions", beginner)
        result_2 = client.search_to_boolean("transactions", intermediate)
        # 断言用户的购买状态
        self.assertEqual(body['payload']['isStudyPlanProductPurchased']['Primary'], result_1)
        self.assertEqual(body['payload']['isStudyPlanProductPurchased']['Intermediate'], result_2)


if __name__ == '__main__':
    unittest.main()
