#!/usr/bin/env python
# __author__= 'wanggangdan'

import os
import sys

from lib.core.Download import Downloader

filename = os.path.join(sys.path[0],"data","web_shell.dic")
payload = []
f = open(filename)
a = 0
for i in f:
    payload.append(i.strip())
    a+=1
    if(a==999):
        break

class spider:
    def run(self,url,html):
        if(not url.endswith(".php")):
            return False
        print '[Webshell check]:',url
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s";' % _payload
            r = Downloader.post(url,post_data)
            if(r):
                print("webshell:%s"%r)
                return True
        return False
