# -*- coding: utf8 -*-

from abc import abstractmethod
from certbot_adc import CadcProviderBase, CadcConf


class CadcProviders(CadcProviderBase):
    cadc_conf: CadcConf

    @abstractmethod
    def update_dns01(self, domain: str, token: str) -> None: ...
