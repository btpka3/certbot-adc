# -*- coding: utf8 -*-

from abc import abstractmethod


class CadcProviderBase:
    @abstractmethod
    def update_dns01(self, domain, token):
        pass
