from CadcConf import CadcConf

c = CadcConf("sample.yaml")
c.check()
print(("confFile =  ", c.confFile))
print("confDict =  ", c.confDict)
print("domainMappings =  ", c.domainMappings)


