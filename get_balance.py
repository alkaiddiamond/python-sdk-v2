#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json

#实例化 API 句柄


if __name__=='__main__':
    arg_length = len(sys.argv)

    params = {}
    params['Action.1'] = "GetBalance"
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    response = ApiClient.get("/", params);
    print response;
