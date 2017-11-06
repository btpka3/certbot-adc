# -*- coding: utf8 -*-

import sys
from abc import abstractmethod


class CadcProviderBase:
    @abstractmethod
    def updateDns01(self, domain, token):
        # 检查是否配置文件

        pass
