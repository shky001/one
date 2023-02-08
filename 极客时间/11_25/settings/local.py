from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

LDAP_AUTH_URL = "ldap://xxxxx:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"

INSTALLED_APPS += (
    # other apps for production site
    'debug_toolbar',
)

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=e9101fb417f6afce2a7d96e81ff560e33908611323cb82e66f01cd433cc4cbb3"
