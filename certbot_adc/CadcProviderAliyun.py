# -*- coding: utf8 -*-

from CadcProviderBase import CadcProviderBase
import json
import logging

from aliyunsdkalidns.request.v20150109 import \
    AddDomainRecordRequest, \
    UpdateDomainRecordRequest, \
    DescribeDomainRecordsRequest, \
    DescribeDomainRecordInfoRequest

logger = logging.getLogger("certbot_adc.CadcProviderAliyun")


class CadcProviderAliyun(CadcProviderBase):
    acs_client = None

    def __init__(self, acs_client):
        self.acs_client = acs_client

    def get_txt_record(self, record_id):

        req = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
        req.set_RecordId(record_id)

        resp_str = self.acs_client.do_action_with_exception(req)
        resp_dict = json.loads(resp_str)

        logger.debug("get_txt_record:" + resp_str)

        return resp_dict

    def update_txt_record(self, record_id, rr, value):

        req = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        req.set_RecordId(record_id)
        req.set_Type("TXT")
        req.set_RR(rr)
        req.set_Value(value)

        resp_str = self.acs_client.do_action_with_exception(req)
        resp_dict = json.loads(resp_str)

        logger.debug("update_txt_record:" + resp_str)

        record_id = resp_dict.get('RecordId')
        if record_id and type(record_id) == str:
            return record_id
        else:
            return None

    def add_txt_record(self, domain, rr, value):

        req = AddDomainRecordRequest.AddDomainRecordRequest()
        req.set_DomainName(domain)
        req.set_Type("TXT")
        req.set_RR(rr)
        req.set_Value(value)

        resp_str = self.acs_client.do_action_with_exception(req)
        resp_dict = json.loads(resp_str)
        record_id = resp_dict.get('RecordId')

        logger.debug("add_txt_record:" + resp_str)

        if record_id and type(record_id) == str:
            return record_id
        else:
            return None

    def find_target_txt_record(self, domain, rr):
        req = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        # req.set_accept_format("JSON")
        req.set_DomainName(domain)
        req.set_PageNumber(1)
        req.set_PageSize(500)
        req.set_RRKeyWord(rr)

        resp_str = self.acs_client.do_action_with_exception(req)
        resp_dict = json.loads(resp_str)

        logger.debug("find_target_txt_record:" + resp_str)

        total_count = resp_dict.get("TotalCount")

        if total_count and type(total_count) == int:

            for rec in resp_dict["DomainRecords"]["Record"]:
                if rec["Type"] == 'TXT' and rec['RR'] == rr:
                    return rec['RecordId']

        return None

    def update_dns01(self, domain, token):

        # domain = 'subdomain.domain.ext'
        d1, d0 = domain.split('.')[-2:]

        main_domain = d1 + "." + d0
        sub_domain = domain.replace(main_domain, "")
        if sub_domain:
            sub_domain = sub_domain.rstrip(".")

        sub_domain = "_acme-challenge." + sub_domain

        record_id = self.find_target_txt_record(main_domain, sub_domain)

        if record_id:
            rec_resp = self.get_txt_record(record_id)
            logger.error(rec_resp)
            logger.error(type(rec_resp))
            logger.error(rec_resp.get('Value'))
            logger.error(token)

            if rec_resp is not None and type(rec_resp) == dict and rec_resp.get('Value') != token:
                self.update_txt_record(record_id, sub_domain, token)
                logger.info("==================OKKKKK")
            else:
                logger.error("==================ERROR====")
        else:
            self.add_txt_record(main_domain, sub_domain, token)
            logger.info("==================OKKKKK~~")
