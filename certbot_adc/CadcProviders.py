# -*- coding: utf8 -*-

from abc import abstractmethod
from CadcProviderBase import CadcProviderBase
from CadcConf import CadcConf
from CadcProviderAliyun import CadcProviderAliyun
from aliyunsdkcore.client import AcsClient


class CadcProviders(CadcProviderBase):
    cadc_conf = None

    def __init__(self, cadc_conf_file):
        self.cadc_conf = CadcConf(cadc_conf_file)

    @abstractmethod
    def update_dns01(self, domain, token):
        m = self.cadc_conf.domain_mappings.get(domain)

        assert m, "'" + domain + "' is not configured."

        p = m.get("provider")

        if p.get("type") == "aliyun":
            acs_client = AcsClient(
                p.get("accessKeyId"),
                p.get("accessKeySecret"),
                p.get("regionId")
            )
            aliyun_provider = CadcProviderAliyun(acs_client)
            aliyun_provider.update_dns01(domain, token)

        pass
