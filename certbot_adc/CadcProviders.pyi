# -*- coding: utf8 -*-

from certbot_adc import CadcProviderBase, CadcConf

class CadcProviders(CadcProviderBase):
    cadc_conf: CadcConf

    def __find_mapping(self, domain: str) -> dict: ...

    def update_dns01(self, domain: str, token: str) -> None: ...

    def clean_dns01(self, domain: str) -> None: ...
