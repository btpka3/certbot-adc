"""
1. 获取指定域名的解析记录列表，以确定是要添加，还是要更新。

"""

from aliyunsdkalidns.request.v20150109 import \
    DescribeDomainsRequest, \
    DescribeDomainRecordsRequest, \
    DescribeSubDomainRecordsRequest, \
    DescribeDomainRecordInfoRequest

from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.client import AcsClient

import sys
import yaml


def updateDns01(domain, token):

    # 检查是否配置文件

    pass

def listDomainRecords(acsClient, domain):
    pass


accessKey = "Q6Yig4iuGXUu50Nd"
accessSecret = "mW34f9ridJkBplbgEa3SldLVgnsjBh"
regionId = "cn-hangzhou"

client = AcsClient(accessKey, accessSecret, regionId)

request = DescribeDomainsRequest.DescribeDomainsRequest()
request.set_accept_format("JSON")

request.set_PageNumber(1)
request.set_PageSize(20)
# request.set_KeyWord("")
# request.set_GroupId("")
#
# request.set_domain('alidns.aliyuncs.com')
# request.set_accept_format("JSON")
# request.set_version("2015-01-09")
# # AccessKeyId
# # Signature
# # SignatureMethod
# # Timestamp
# # SignatureVersion
# # SignatureNonce
#
# # Action
# request.set_action_name('DescribeDomains')
#
# # PageNumber
# request.add_query_param('PageNumber', '1')
# # PageSize
# request.add_query_param('PageSize', '20')
# # KeyWord
# # request.add_query_param('KeyWord', 'test')
# # GroupId
# # request.add_query_param('GroupId', '')
# request.set_method('GET')

response = client.do_action_with_exception(request)
print(type(response))
print(response)
