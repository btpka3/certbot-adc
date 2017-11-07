# -*- coding: utf8 -*-


import yaml
from validate_email import validate_email
import os


class CadcConf:
    """
    key     : domainName        # str
    value   : {           
        providerIdx     : 0,    # int
        provider        : ?     # dict, == `providers[${providerIdx}]`
    }
    """
    domain_mappings = {}
    conf_file = None
    conf_dict = None

    def __init__(self, conf_file):

        self.conf_file = conf_file
        self.conf_dict = yaml.load(open(self.conf_file, "r").read())
        self.check()

    def __check_provider_domains(self, provider_idx, provider, domains):
        for domain_idx, domain in enumerate(domains):
            assert domain and type(domain) == str, \
                "`providers[" + str(provider_idx) + "].domains[" + str(
                    domain_idx) + "]` is not configured correctly in yaml file."

            existed_mapping = self.domain_mappings.get(domain)
            if existed_mapping != None:
                raise Exception(domain + " is both configured in `providers[" + str(
                    provider_idx) + "].domains and `providers[" + str(existed_mapping.get('providerIdx')) + "]")

            else:
                self.domain_mappings[domain] = {
                    "providerIdx": provider_idx,
                    "provider": provider
                }

    def __check_provider_aliyun(self, provider_idx, provider):
        access_key_id = provider.get("accessKeyId")
        assert access_key_id and type(access_key_id) == str, \
            "`providers[" + str(provider_idx) + "].accessKeyId` is not configured correctly in yaml file."

        access_key_secret = provider.get("accessKeySecret")
        assert access_key_secret and type(access_key_secret) == str, \
            "`providers[" + str(provider_idx) + "].accessKeySecret` is not configured correctly in yaml file."

        region_id = provider.get("regionId")
        assert region_id and type(region_id) == str, \
            "`providers[" + str(provider_idx) + "].regionId` is not configured correctly in yaml file."

        domains = provider.get("domains")
        assert domains and type(domains) == list, \
            "`providers[" + str(provider_idx) + "].domains` is not configured correctly in yaml file."

        self.__check_provider_domains(provider_idx, provider, domains)

    def __check_providers(self, providers):

        assert providers is not None and type(providers) == list, \
            "`providers` is not configured correctly in yaml file."

        names = []
        for idx, provider in enumerate(providers):

            assert provider is not None and type(provider) == dict, \
                "`providers[" + str(idx) + "]` is not configured correctly in yaml file."

            name = provider.get("name")

            # check certbot_cadc.providers*.name
            assert name and type(name) == str, \
                "`providers[" + str(idx) + "].name` is not configured correctly in yaml file."
            try:
                existed_name_idx = names.index(name)
                names.append(name)
                assert False, \
                    "`providers[" + str(idx) + "].name` is same with `providers[" \
                    + str(existed_name_idx) + "].name`."
            except ValueError:
                pass

            _type = provider.get("type")
            assert _type and type(_type) == str, \
                "`providers[" + str(idx) + "].type` is not configured correctly in yaml file."
            if _type == 'aliyun':
                self.__check_provider_aliyun(idx, provider)
            else:
                raise Exception("`providers[" + str(idx) + "].type` ='" + _type + "', which is not supported.")

    def check(self):

        # certbot = self.conf_dict.get("certbot")
        # if certbot:
        #     assert type(certbot) == str, \
        #         "`certbot` is not configured correctly in yaml file. Will using default value. "
        #     assert os.path.isdir(certbot), \
        #         "'" + certbot + "' is not a valid certbot path."
        # else:
        #     self.conf_dict["certbot"] = '/etc/letsencrypt'
        #
        # email = self.conf_dict.get("email")
        # assert email and type(email) == str and validate_email('example@example.com'), \
        #     "`email` is not configured correctly in yaml file."
        #
        # renew_ahead = self.conf_dict.get("renewAhead")
        # assert renew_ahead != None and type(renew_ahead) == int and renew_ahead > 0, \
        #     "`renewAhead` is not configured correctly in yaml file."

        providers = self.conf_dict.get("providers")
        self.__check_providers(providers)
