# -*- coding: utf8 -*-


from cadc import CadcConf
from cadc import CadcProviderBase
from aliyunsdkcore.client import AcsClient


class CadcProviderAliyun:
    cadcConf: CadcConf

    def __init__(self, cadcConf: CadcConf): ...

    def getTxtRecord(self, acsClient: AcsClient, recordId: str) -> dict: ...

    def updateTxtRecord(self, acsClient: AcsClient, recordId: str, rr: str, value: str) -> str: ...

    def addTxtRecord(self, acsClient: AcsClient, domain: str, rr: str, value: str) -> str: ...

    def findTargetTxtRecord(self, acsClient: AcsClient, domain: str, rr: str) -> str: ...

    def updateDns01(self, domain: str, token: str) -> None: ...
