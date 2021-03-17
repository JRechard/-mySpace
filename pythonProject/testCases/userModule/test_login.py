import unittest
from parameterized import parameterized
from common.config_http import ConfigHttp
from common.read_excel import ReadExcel
from common.read_config import ReadConfig

login_xls = ReadExcel().get_xls('userCases.xls', 'Sheet1')


class TestLogin(unittest.TestCase):
    @parameterized.expand(login_xls)
    def test_login(self, case_name, path, data, method):
        base_url = ReadConfig().get_base_url()
        new_url = base_url + path
        result = ConfigHttp().run_main(method=method, url=new_url, data=data)
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
