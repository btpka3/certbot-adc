# -*- coding: utf8 -*-

from CadcProviderBase import CadcProviderBase
from CadcConf import CadcConf
from CadcProviderAliyun import CadcProviderAliyun
from aliyunsdkcore.client import AcsClient


class CadcProviders(CadcProviderBase):
    cadc_conf = None

    def __init__(self, cadc_conf_file=None):
        self.cadc_conf = CadcConf(cadc_conf_file)

    def __find_mapping(self, domain):

        if not domain:
            return None

        # full match ("aaa.test.kingsilk.net.cn" eg.)
        m = self.cadc_conf.domain_mappings.get(domain)
        if m:
            return m

        # check root matches
        # aaa.test.kingsilk.net.cn
        #   -> test.kingsilk.net.cn
        #        -> kingsilk.net.cn
        #                 -> net.cn
        #                     -> cn
        i = domain.find(".")
        while i >= 0:
            r = domain[i + 1:]
            m = self.cadc_conf.domain_mappings.get(r)
            if m:
                return m
            i = domain.find(".", i + 1)

        return None

    def update_dns01(self, domain, token):
        m = self.__find_mapping(domain)

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


    def clean_dns01(self, domain):
        m = self.__find_mapping(domain)

        assert m, "'" + domain + "' is not configured."

        p = m.get("provider")

        if p.get("type") == "aliyun":
            acs_client = AcsClient(
                p.get("accessKeyId"),
                p.get("accessKeySecret"),
                p.get("regionId")
            )
            aliyun_provider = CadcProviderAliyun(acs_client)
            aliyun_provider.clean_dns01(domain)
