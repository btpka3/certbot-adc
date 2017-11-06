# -*- coding: utf8 -*-


from CadcConf import CadcConf
from cadc import CadcProviderAliyun

c = CadcConf("../.tmp/sample.yaml")
p = CadcProviderAliyun.CadcProviderAliyun(c)

p.updateDns01("test12.kingsilk.xyz","999")
