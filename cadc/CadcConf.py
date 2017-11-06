# -*- coding: utf8 -*-


import yaml
from validate_email import validate_email
import os


class CadcConf:
    """
    key     : domainName        # str
    value   : {           
        providerIdx     : 0,    # int
        provider        : ?     # dict, == `cadc.providers[${providerIdx}]`
    }
    """
    domainMappings = {}
    confFile = None
    confDict = None

    def __init__(self, confFile):

        self.confFile = confFile
        self.confDict = yaml.load(open(self.confFile, "r").read())
        self.check()

    def __checkProviderDomains(self, providerIdx, provider, domains):
        for domainIdx, domain in enumerate(domains):
            assert domain and type(domain) == str, \
                "`cadc.providers[" + str(providerIdx) + "].domains[" + str(
                    domainIdx) + "]` is not configured correctly in yaml file."

            existed_mapping = self.domainMappings.get(domain)
            if existed_mapping != None:
                raise Exception(domain + " is both configured in `cadc.providers[" + str(
                    providerIdx) + "].domains and `cadc.providers[" + str(existed_mapping.get('providerIdx')) + "]")

            else:
                self.domainMappings[domain] = {
                    "providerIdx": providerIdx,
                    "provider": provider
                }

    def __checkProviderAliyun(self, providerIdx, provider):
        accessKeyId = provider.get("accessKeyId")
        assert accessKeyId and type(accessKeyId) == str, \
            "`cadc.providers[" + str(providerIdx) + "].accessKeyId` is not configured correctly in yaml file."

        accessKeySecret = provider.get("accessKeySecret")
        assert accessKeySecret and type(accessKeySecret) == str, \
            "`cadc.providers[" + str(providerIdx) + "].accessKeySecret` is not configured correctly in yaml file."

        regionId = provider.get("regionId")
        assert regionId and type(regionId) == str, \
            "`cadc.providers[" + str(providerIdx) + "].regionId` is not configured correctly in yaml file."

        domains = provider.get("domains")
        assert domains and type(domains) == list, \
            "`cadc.providers[" + str(providerIdx) + "].domains` is not configured correctly in yaml file."

        self.__checkProviderDomains(providerIdx, provider, domains)

    def __checkProviders(self, providers):

        assert providers != None and type(providers) == list, \
            "`cadc.providers` is not configured correctly in yaml file."

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
                self.__checkProviderAliyun(idx, provider)
            else:
                raise Exception("`cadc.providers[" + str(idx) + "].type` ='" + _type + "', which is not supported.")

    def check(self):

        cadc = self.confDict.get("cadc")
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
        self.__checkProviders(providers)

