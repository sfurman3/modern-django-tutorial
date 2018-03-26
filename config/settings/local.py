from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
        'DJANGO_SECRET_KEY',
        default='z_v9+1t6o4+tkcby!(hb^x*1ado-8++74iwd(fk-jxz@v3l##e'
)

DEBUG = True
