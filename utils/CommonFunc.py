#!/usr/bin/env python2
# coding: utf-8
# file: CommonFunc.py.py
# time: 16-11-26 下午11:25

__author__ = "lightless"
__email__ = "root@lightless.me"


def format_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "http://" + url
    else:
        return url
