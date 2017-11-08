# -*- coding: utf8 -*-

class CadcConf:
    domain_mappings: dict
    name_mappings : dict
    confFile: str
    confDict: str

    def __init__(self, conf_file: str = None): ...

    def find_conf_file(self) -> str: ...

    def __check_provider_domains(self, provider_idx: int, provider: dict, domains: list) -> None: ...

    def __check_provider_aliyun(self, provider_idx: int, provider: dict) -> None: ...

    def __check_providers(self, providers: list) -> None: ...

    def check(self) -> None: ...
