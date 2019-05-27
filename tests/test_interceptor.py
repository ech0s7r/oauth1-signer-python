#!/usr/bin/env python
# -*- coding: utf-8 -*-#
#
#
# Copyright (c) 2019 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
import unittest
import requests
from urllib.parse import urlencode
from oauth1.oauth import OAuth
from oauth1.signer_interceptor import SignerInterceptor
import oauth1.authenticationutils as authenticationutils
from os.path import dirname, realpath, join, os
from oauth1.signer import OAuthSigner
from oauth1.signer_interceptor import add_signing_layer
from oauth1.signer_interceptor import get_signing_layer


class OAuthInterceptorTest(unittest.TestCase):


    """ add an interceptor, check api client has changed """
    def test_add_interceptor(self):
        if os.path.exists('./test_key_container.p12'):
            key_file = './test_key_container.p12'
            key_password = "Password1"
            consumer_key = 'uLXKmWNmIkzIGKfA2injnNQqpZaxaBSKxa3ixEVu2f283c95!33b9b2bd960147e387fa6f3f238f07170000000000000000'

            signing_layer1 = get_signing_layer(self, requests)
            
            add_signing_layer(self, requests, key_file, key_password, consumer_key)

            signing_layer2 = get_signing_layer(self, requests)

            self.assertNotEqual(signing_layer1, signing_layer2)            


        else:
            print("Please add a ./test_key_container.p12 file to enable key tests")



if __name__ == '__main__':
    unittest.main()
