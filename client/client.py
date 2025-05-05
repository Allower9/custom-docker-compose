#!/usr/bin/env python3
import urllib.request

fp = urllib.request.urlopen("http://server:1234/")
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")
print(decodedContent)
fp.close()
