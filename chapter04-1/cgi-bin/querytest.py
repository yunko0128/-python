#!/usr/bin/env python
#coding:utf-8

html_body = """
<html><body>
foo = %s
</body></html>"""

import cgi
testForm = cgi.FieldStorage()

print "Content-type: text/html¥n"
print ""
#print html_body % testForm['foo'].value
print testForm.getvalue('foo','N/A')
	#getvalue()の第一引数：キー、第二引数：クエリが無い場合