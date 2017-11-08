# -*- coding: utf8 -*-

from CadcProviderBase import CadcProviderBase
from QcloudApi.qcloudapi import QcloudApi
import json
import logging

logger = logging.getLogger("certbot_adc.CadcProviderAliyun")


class CadcProviderQcloud(CadcProviderBase):
    qcloud_api = None

    def __init__(self, qcloud_api):
        self.qcloud_api = qcloud_api

    def list(self, domain):
        params = {
            "domain": domain
        }
        resp =  self.qcloud_api.call("RecordList", params)
        print(type(resp))
        print(resp)

    def update_dns01(self, domain, token):
        pass

    def clean_dns01(self, domain):
        pass
