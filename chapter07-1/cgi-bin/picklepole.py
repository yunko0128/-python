#!/usr/bin/env/ python
#coding:utf-8

import pickle
from httphandler import request,Response,get_htmltemplate
import cgitb; cgitb.enable()

form_body = u"""
	<form method="POST" action="/cgi-bin/picklepole.py">
	好きな言語は？<br />
	%s
	<input type="submit">
	</form>"""

radio_parts = u"""
<input type="radio" name="language" value="%s" />%s
<div style="border-left:solid %sem red;>%s</div>
"""

lang_dic = {}
try:
	f=open('/Users/sasakiyukiko/Desktop/minnanPython/chapter07-1/favorite_language.dat')
	lang_dic = pickle.loads(f)
except IOError:
	pass

content = ""
req = Request()
if req.form.has_key('language'):
	lang = req.form['language'].value
	lang_dic[lang] = lang_dic.get(lang,0)+1

f=open('/Users/sasakiyukiko/Desktop/minnanPython/chapter07-1/favorite_language.dat','w')
pickle.dump(lang_dic,f)

for lang in ['Perl','PHP','Python','Ruby']
	num = lang_dic.get(lang,0)
	content += radio_parts%(lang,lang,num,num)

res = Response()
body = form_body%content
res.set_body(get_htmltemplate()%body)
print res

'''
  File "/usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/CGIHTTPServer.py", line 248, in run_cgi
    os.execve(scriptfile, args, env)
OSError: [Errno 20] Not a directory
'''