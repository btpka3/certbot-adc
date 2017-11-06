# -*- coding: utf8 -*-

from abc import abstractmethod

class CadcProviderBase:
    @abstractmethod
    def updateDns01(self, domain: str, token: str) -> None: ...
