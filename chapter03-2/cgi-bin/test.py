#!/usr/bin/env python
#coding:utf-8

import datetime

html_body = """
<html><body>
%d
</body></html>"""

nowTime = datetime.datetime.now()

print "Content-type: text/html¥n"
print ""
print html_body % (nowTime.minute)
#print "<html><body>test</body></html>"