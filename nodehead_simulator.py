#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pgeorge
#
# Created:     11/07/2011
# Copyright:   (c) pgeorge 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib.parse

import sys
sys.path.append('..\gemalto')
import gemalto

HOST_NODE_HEAD='http://nodehead.botoxsmile.cloud9ide.com/'

class NodeHeadAPI(gemalto.RESTAPI):
    def __init__(self,verbose=False):
        super().__init__(verbose)

    def postNodeHead(self,msg):
        req=self.build_request(HOST_NODE_HEAD,'/','POST')
        req.add_data(msg)
        req.add_header('Content-Type','application/x-www-form-urlencoded')
        resp=self.send_request(req)
        return self.get_data(resp).decode('utf-8')

if __name__ == '__main__':
    nh=NodeHeadAPI()
    print(nh.postNodeHead(b'Hello NodeHead'))