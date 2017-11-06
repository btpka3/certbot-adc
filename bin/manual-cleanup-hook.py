#!/usr/bin/env python

import os

print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_DOMAIN     = ", os.environ.get('CERTBOT_DOMAIN')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_VALIDATION = ", os.environ.get('CERTBOT_VALIDATION')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_TOKEN      = ", os.environ.get('CERTBOT_TOKEN')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_CERT_PATH  = ", os.environ.get('CERTBOT_CERT_PATH')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_KEY_PATH   = ", os.environ.get('CERTBOT_KEY_PATH')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_SNI_DOMAIN = ", os.environ.get('CERTBOT_SNI_DOMAIN')
print "~~~~~~~~~ manual-cleanup-hook.py : CERTBOT_AUTH_OUTPUT= ", os.environ.get('CERTBOT_AUTH_OUTPUT')


