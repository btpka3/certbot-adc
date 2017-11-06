# certbot-auto-dns-challenge



```bash
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-alidns

docker run -it --rm --entrypoint "" \
    -v /data0/store/soft/certbot/docker/etc/letsencrypt:/etc/letsencrypt \
    -v /data0/store/soft/certbot/docker/var/lib/letsencrypt:/var/lib/letsencrypt \
    -v /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge:/data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge \
    certbot/certbot \
    sh
    certbot \
        -d test13.kingsilk.xyz \
        --manual \
        --preferred-challenges dns \
        certonly

docker \
    create  \
    --entrypoint "/bin/sh" \
    -t \
    --name my-certbot \
    -v /data0/store/soft/certbot/docker/etc/letsencrypt:/etc/letsencrypt \
    -v /data0/store/soft/certbot/docker/var/lib/letsencrypt:/var/lib/letsencrypt \
    -v /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge:/data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge \
    certbot/certbot


docker run -it --rm --entrypoint "" \
    -v /data0/store/soft/certbot/docker/etc/letsencrypt:/etc/letsencrypt \
    -v /data0/store/soft/certbot/docker/var/lib/letsencrypt:/var/lib/letsencrypt \
    -v /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge:/data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge \
    certbot/certbot \
    certbot \
        -n \
        -d test12.kingsilk.xyz \
        --manual-public-ip-logging-ok \
        --manual \
        --manual-auth-hook /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge/manual-auth-hook.py \
        --manual-cleanup-hook /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge/manual-cleanup-hook.py \
        --preferred-challenges dns \
        certonly
```



# 计划

```bash

# 第一次初始化，需要设置邮箱。
docker exec my-cdac certbot \
    register \
    -n \
    --email admin@kingsilk.net \
    --eff-email \
    --agree-tos

# 手动执行
docker exec my-cdac certbot \
    certonly \
    --manual \
    --manual-public-ip-logging-ok \
    --manual-auth-hook /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge/manual-auth-hook.py \
    --manual-cleanup-hook /data0/work/git-repo/github/btpka3/certbot-auto-dns-challenge/manual-cleanup-hook.py \
    --preferred-challenges dns \
    -d kingsilk.club

# 定时任务
docker stop my-cdac
docker start my-cdac
docker exec my-cdac 

```
# 参考

- dev
    - [python - pem](https://pem.readthedocs.io/en/stable/api.html#pem-objects)
    - [python - rsa](https://stuvel.eu/rsa)
- [certbot hooks](https://certbot.eff.org/docs/using.html#pre-and-post-validation-hooks)
- [阿里云 python SDK - 快速开始](https://help.aliyun.com/document_detail/53090.html)
- [PyPI - aliyun-python-sdk-alidns](https://pypi.python.org/pypi/aliyun-python-sdk-alidns)
- [Github - aliyun-python-sdk-alidns](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-alidns)
- [阿里云-云解析-API](https://help.aliyun.com/document_detail/29740.html )
- [腾讯-云解析-API](https://cloud.tencent.com/document/api/302/8519)
