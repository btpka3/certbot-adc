# -*- coding: utf8 -*-

import sys
from abc import abstractmethod
from cadc import CadcProviderBase
import json

from aliyunsdkalidns.request.v20150109 import \
    AddDomainRecordRequest, \
    DescribeDomainsRequest, \
    UpdateDomainRecordRequest, \
    DescribeDomainRecordsRequest, \
    DescribeSubDomainRecordsRequest, \
    DescribeDomainRecordInfoRequest

from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.client import AcsClient


class CadcProviderAliyun:
    cadcConf = None

    def __init__(self, cadcConf):
        self.cadcConf = cadcConf

    def getTxtRecord(self, acsClient, recordId):

        req = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
        req.set_RecordId(recordId)

        respStr = acsClient.do_action_with_exception(req)
        respDict = json.loads(respStr)

        print(respStr)

        return respDict

    def updateTxtRecord(self, acsClient, recordId, rr, value):

        req = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
        req.set_RecordId(recordId)
        req.set_Type("TXT")
        req.set_RR(rr)
        req.set_Value(value)

        respStr = acsClient.do_action_with_exception(req)
        respDict = json.loads(respStr)

        print(respStr)

        recordId = respDict.get('RecordId')
        if recordId and type(recordId) == str:
            return recordId
        else:
            return None

    def addTxtRecord(self, acsClient, domain, rr, value):

        req = AddDomainRecordRequest.AddDomainRecordRequest()
        req.set_DomainName(domain)
        req.set_Type("TXT")
        req.set_RR(rr)
        req.set_Value(value)

        respStr = acsClient.do_action_with_exception(req)
        respDict = json.loads(respStr)
        recordId = respDict.get('RecordId')

        print(respStr)

        if recordId and type(recordId) == str:
            return recordId
        else:
            return None

    def findTargetTxtRecord(self, acsClient, domain, rr):
        req = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        # req.set_accept_format("JSON")
        req.set_DomainName(domain)
        req.set_PageNumber(1)
        req.set_PageSize(500)
        req.set_RRKeyWord(rr)

        respStr = acsClient.do_action_with_exception(req)
        respDict = json.loads(respStr)
        print(respStr)

        totalCount = respDict.get("TotalCount")

        if totalCount and type(totalCount) == int:

            for rec in respDict["DomainRecords"]["Record"]:
                if rec["Type"] == 'TXT' and rec['RR'] == rr:
                    return rec['RecordId']

        return None

    def updateDns01(self, domain, token):
        m = self.cadcConf.domainMappings.get(domain)

        assert m, "'" + domain + "' is not configured."

        p = m.get("provider")

        acsClient = AcsClient(
            p.get("accessKeyId"),
            p.get("accessKeySecret"),
            p.get("regionId")
        )

        # domain = 'subdomain.domain.ext'
        d1, d0 = domain.split('.')[-2:]

        mainDomain = d1 + "." + d0
        subDomain = domain.replace(mainDomain, "")
        if subDomain:
            subDomain = subDomain.rstrip(".")

        subDomain = "_acme-challenge." + subDomain

        recordId = self.findTargetTxtRecord(acsClient, mainDomain, subDomain)

        if recordId:
            recResp = self.getTxtRecord(acsClient, recordId)
            if recResp and recResp.get('Value') != token:
                self.updateTxtRecord(acsClient, recordId, subDomain, token)
        else:
            self.addTxtRecord(acsClient, mainDomain, subDomain, token)
