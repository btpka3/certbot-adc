# -*- coding: utf8 -*-

import sys
from abc import abstractmethod
import CadcProviderBase


class CadcProviders(CadcProviderBase):

    cadcConf = None

    def __init__(self, cadcConf):
        self.cadcConf = cadcConf


    @abstractmethod
    def updateDns01(self, domain, token):
        # 检查是否配置文件

        pass
