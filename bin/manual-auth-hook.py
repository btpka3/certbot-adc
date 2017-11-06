#!/usr/bin/env python

import os


print "----------- manual-auth-hook.py : CERTBOT_DOMAIN     = ", os.environ.get('CERTBOT_DOMAIN')
print "----------- manual-auth-hook.py : CERTBOT_VALIDATION = ", os.environ.get('CERTBOT_VALIDATION')
print "----------- manual-auth-hook.py : CERTBOT_TOKEN      = ", os.environ.get('CERTBOT_TOKEN')
print "----------- manual-auth-hook.py : CERTBOT_CERT_PATH  = ", os.environ.get('CERTBOT_CERT_PATH')
print "----------- manual-auth-hook.py : CERTBOT_KEY_PATH   = ", os.environ.get('CERTBOT_KEY_PATH')
print "----------- manual-auth-hook.py : CERTBOT_SNI_DOMAIN = ", os.environ.get('CERTBOT_SNI_DOMAIN')
print "----------- manual-auth-hook.py : CERTBOT_AUTH_OUTPUT= ", os.environ.get('CERTBOT_AUTH_OUTPUT')

"""
1. 解析并检查配置文件
2. 调用相应的API "_acme-challenge.test13"
"""