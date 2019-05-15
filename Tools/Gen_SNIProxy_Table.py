# -*- coding:utf-8 -*-
import datetime as d
import re
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("sni", help="sniproxy.conf")
parser.add_argument("input", help="Original List")

parser.add_argument('-o', '--output',#可选参数                    
                    required=False,#是否必须携带                    
                    default='sniproxy.conf',#默认值                    
                    help='SNIProxy Config File')#帮助文档

args = parser.parse_args()

#f = open(args.output, 'w')
#f.write('[Hosts]\n## IPv4 SNI Hosts Lists\n## Last update: '+d.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+'\n\n')

try:
	# 处理SNIProxy配置
	f = open(args.sni, 'r')
	sniConfigLines = f.readlines()
	for i,l in enumerate(sniConfigLines):
		y = re.match('.*proxy_hosts {$', l)
		if y:
			for_s = i
			#print("start line:"+str(line_s))
			break

	if for_s <= 0:
		print('Cannot Find the https_host, Aborted!')
		sys.exit(1)

	for j,m in enumerate(sniConfigLines):
		if j < for_s:
			continue
		z = re.match('^}', m)
		if z:
			for_e = j
			break

	# print("start line:"+str(for_s))
	# print("end line:"+str(for_e))

	# 处理SNI列表
	r = open(args.input, 'r')
	sniHostList = list()
	sniHostList.append('\n    ## SNIProxy Generated\n')
	sniHostList.append('    ## Last update: '+d.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+'\n\n')
	for line in r.readlines():
		line=line.strip()
		if not len(line) or line.startswith('#'):        #注释行处理
			continue
		else:
			sniHostList.append('    '+line+' *\n')

	# 列表分割
	sniConfigLines_pre = sniConfigLines[0:for_s+1]
	sniConfigLines_target = sniConfigLines[for_s+1:for_e]
	sniConfigLines_post = sniConfigLines[for_e::]
	
	# 列表合并
	sniConfigLines = sniConfigLines_pre + sniHostList + sniConfigLines_post
	# print(sniConfigLines_target)

	#保存输出
	opt = open(args.output, 'w')
	opt.write(''.join(sniConfigLines)) #保存入结果文件


except IOError as e:
	print("File is not accessible")
	sys.exit(255)

