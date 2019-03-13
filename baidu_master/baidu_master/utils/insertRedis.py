# -*- coding: utf-8 -*-
import redis

def inserintota(key, val):
    try:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    except:
        print('连接redis失败')
    else:
        r.lpush(key, val)