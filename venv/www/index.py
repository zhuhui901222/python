#!/usr/bin/python
# -*- coding: UTF-8 -*-


def application(environ, start_response):
	# 创建 FieldStorage 的实例化
	#print 124
    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
 
    return [output]

"""
print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>'
print '</body>'
print '</html>'
"""