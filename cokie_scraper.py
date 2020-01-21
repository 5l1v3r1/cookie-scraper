#!/usr/bin/env python
# CodeName BY Ari
# @WongNdesoCok

import cfscrape
import sys
import requests

request = "GET / HTTP/1.1\r\n"
sess = cfscrape.create_scraper()
print"""
  ____            _    _        ____
 / ___|___   ___ | | _(_) ___  / ___|  ___ _ __ __ _ _ __   ___ _ __ 
| |   / _ \ / _ \| |/ / |/ _ \ \___ \ / __| '__/ _` | '_ \ / _ \ '__|
| |__| (_) | (_) |   <| |  __/  ___) | (__| | | (_| | |_) |  __/ |   
 \____\___/ \___/|_|\_\_|\___| |____/ \___|_|  \__,_| .__/ \___|_|   
                                                Code: By WongNdesoCok
                                                    |_|
"""

jancok = raw_input("Masukan Target{ex:http/https://Target.com}~# ")

cookie_value, user_agent = cfscrape.get_cookie_string(jancok)
request += "Cookie: %s\r\nUser_Agent: %s\r\n" % (cookie_value, user_agent)
print
print sess.get(jancok).content
print 
print request 

