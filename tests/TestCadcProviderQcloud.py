from certbot_adc import CadcUtils, CadcProviderQcloud, CadcConf
from QcloudApi.qcloudapi import QcloudApi
import unittest


class TestCadcProviderQcloud(unittest.TestCase):
    cadc_conf = None
    qcloud_api = None
    q = None

    def setUp(self):
        self.cadc_conf = CadcConf.CadcConf("../.tmp/certbot_adc.yaml")

        m = self.cadc_conf.name_mappings.get("zhang3")
        p = m['provider']
        self.qcloud_api = QcloudApi("cns", {
            'Region': p["region"],
            'secretId': p["secretId"],
            'secretKey': p["secretKey"],
            'method': 'get'
        })
        self.q = CadcProviderQcloud.CadcProviderQcloud(self.qcloud_api)

    def tearDown(self):
        pass

    def test_list_01(self):
        self.q.list("btpka3.xyz")


if __name__ == '__main__':
    unittest.main()
