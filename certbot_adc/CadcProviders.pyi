# -*- coding: utf8 -*-

from abc import abstractmethod
from certbot_adc import CadcProviderBase, CadcConf


class CadcProviders(CadcProviderBase):
    cadc_conf: CadcConf

    def __find_mapping(self, domain: str) -> dict: ...

    @abstractmethod
    def update_dns01(self, domain: str, token: str) -> None: ...
