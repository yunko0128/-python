#!/usr/bin/env python
#coding:utf-8

import cgi
from datetime import datetime

html_body = u"""
<html><head>
<meta http-equiv="content-type" content ="text/html;charset=utf-8">
</head>
<body>
%s
</body>
</html>"""

content = ''

testForm = cgi.FieldStorage()
year_str = testForm.getvalue('year','N/A')
if not year_str.isdigit():
	content = "query error"
else:
	content = "queryy ok "
	content += u"<br /><br />"
	year = int(year_str)
	friday13 = 0
	for month in range(1,13):
		date = datetime(year,month,13)
		if date.weekday() == 4:
			friday13 += 1
			content += u"%d年%d月13日は金曜です" % (year,date.month)
			content += u"<br />"

	if friday13:
		content+= u"%d年には合計%d日の13日金曜日があります" % (year ,friday13)

print "Content-type: text/html;charset=utf-8¥n"
print ""
#print html_body % content
print (html_body % content).encode('utf-8')