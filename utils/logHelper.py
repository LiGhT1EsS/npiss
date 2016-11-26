#!/usr/bin/env python2
# coding: utf-8
# file: logHelper.py.py
# time: 16-11-26 下午10:47

import logging

import colorlog
from django.conf import settings

__author__ = "lightless"
__email__ = "root@lightless.me"

__all__ = ['logger']


handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(levelname)s] [%(threadName)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s',
        datefmt="%H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
    )
)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
# if settings.DEBUG:
#     logger.setLevel("DEBUG")
# else:
#     logger.setLevel("INFO")
logger.setLevel("DEBUG")
