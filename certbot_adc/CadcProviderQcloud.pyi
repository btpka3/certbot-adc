# -*- coding: utf8 -*-

from certbot_adc import CadcProviderBase
from QcloudApi.qcloudapi import QcloudApi


class CadcProviderQcloud(CadcProviderBase):
    qcloud_api: QcloudApi

    def __init__(self, qcloud_api):

    def list(self,domain:str) -> None: ...

    def update_dns01(self, domain: str, token: str) -> None: ...

    def clean_dns01(self, domain: str) -> None: ...
