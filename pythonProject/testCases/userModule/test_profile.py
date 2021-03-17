import json
import unittest
from parameterized import parameterized
from common.config_http import ConfigHttp
from common.read_excel import ReadExcel
from common.read_config import ReadConfig

profile_xls = ReadExcel().get_xls('userCases.xls', 'Sheet2')


class TestProfile(unittest.TestCase):
    @parameterized.expand(profile_xls)
    def test_profile(self, case_name, path, data, method):
        base_url = ReadConfig().get_base_url()
        new_url = base_url + path
        result = ConfigHttp().run_main(method=method, url=new_url, data=data)
        self.assertEqual(result.status_code, 200)

        body = json.loads(json.dumps(result.json()))
        if case_name == "user_profile_guitar":
            self.assertEqual(body['payload']['isStudyPlanProductPurchased']['Primary'], False)
        elif case_name == "user_profile_ukulele":
            self.assertEqual(body['payload']['isStudyPlanProductPurchased']['Intermediate'], True)
        else:
            pass


if __name__ == '__main__':
    unittest.main()
