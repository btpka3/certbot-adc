"""
pip3 install PyYAML 
"""
import yaml
from validate_email import validate_email
import os

"""
key     : domainName        # str
value   : {           
    providerIdx     : 0,    # int
    provider        : ?     # dict, == `cadc.providers[${providerIdx}]`
}
"""
domainMappings = {
}


def readConf(filePath):
    confFile = open("sample.yaml", "r")
    confStr = confFile.read()
    # print(confStr)

    cadcConf = yaml.load(confStr)
    return cadcConf


def checkProviderDomains(conf, providerIdx, provider, domains):
    for domainIdx, domain in enumerate(domains):
        assert domain and type(domain) == str, \
            "`cadc.providers[" + str(providerIdx) + "].domains[" + str(
                domainIdx) + "]` is not configured correctly in yaml file."

        exitedMapping = domainMappings.get(domain)
        if exitedMapping != None:
            raise Exception(domain + " is both configured in `cadc.providers[" + str(
                providerIdx) + "].domains and `cadc.providers[" + str(exitedMapping.get('providerIdx')) + "]")

        domainMappings[domain] = {
            "providerIdx": providerIdx,
            "provider": provider
        }


def checkProviderAliyun(conf, idx, provider):
    accessKeyId = provider.get("accessKeyId")
    assert accessKeyId and type(accessKeyId) == str, \
        "`cadc.providers[" + str(idx) + "].accessKeyId` is not configured correctly in yaml file."

    accessKeySecret = provider.get("accessKeySecret")
    assert accessKeySecret and type(accessKeySecret) == str, \
        "`cadc.providers[" + str(idx) + "].accessKeySecret` is not configured correctly in yaml file."

    regionId = provider.get("regionId")
    assert regionId and type(regionId) == str, \
        "`cadc.providers[" + str(idx) + "].regionId` is not configured correctly in yaml file."

    domains = provider.get("domains")
    assert domains and type(domains) == list, \
        "`cadc.providers[" + str(idx) + "].domains` is not configured correctly in yaml file."

    checkProviderDomains(conf, idx, provider, domains)


def checkProviders(conf, providers):
    names = []
    for idx, provider in enumerate(providers):

        assert provider != None and type(provider) == dict, \
            "`cadc.providers[" + str(idx) + "]` is not configured correctly in yaml file."

        name = provider.get("name")

        # check cadc.providers*.name
        assert name and type(name) == str, \
            "`cadc.providers[" + str(idx) + "].name` is not configured correctly in yaml file."
        try:
            existedNameIdx = names.index(name)
            names.append(name)
            assert False, \
                "`cadc.providers[" + str(idx) + "].name` is same with `cadc.providers[" \
                + str(existedNameIdx) + "].name`."
        except ValueError:
            pass

        _type = provider.get("type")
        assert _type and type(_type) == str, \
            "`cadc.providers[" + str(idx) + "].type` is not configured correctly in yaml file."
        if _type == 'aliyun':
            checkProviderAliyun(conf, idx, provider)
        else:
            raise Exception("`cadc.providers[" + str(idx) + "].type` ='" + _type + "', which is not supported.")


def checkConf(conf):
    cadc = conf.get("cadc")
    assert cadc and type(cadc) == dict, \
        "`cadc` is not configured correctly in yaml file."

    certbot = cadc.get("certbot")
    if certbot:
        assert type(certbot) == str, \
            "`cadc.certbot` is not configured correctly in yaml file. Will using default value. "
        assert os.path.isdir(certbot), \
            "'" + certbot + "' is not a valid certbot path."
    else:
        cadc["certbot"] = '/etc/letsencrypt'

    email = cadc.get("email")
    assert email and type(email) == str and validate_email('example@example.com'), \
        "`cadc.email` is not configured correctly in yaml file."

    renewAhead = cadc.get("renewAhead")
    assert renewAhead != None and type(renewAhead) == int and renewAhead > 0, \
        "`cadc.renewAhead` is not configured correctly in yaml file."

    providers = cadc.get("providers")
    assert providers != None and type(providers) == list, \
        "`cadc.providers` is not configured correctly in yaml file."

    checkProviders(conf, providers)

    None

# f = "sample.yaml"
# c = readConf(f)
# checkCadc(c)
# print(domainMappings)
