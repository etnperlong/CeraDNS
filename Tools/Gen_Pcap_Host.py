# -*- coding:utf-8 -*-
import datetime as d
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Original List")
parser.add_argument('-s', '--sni',
					required=False,
					default='0.0.0.0',
					help='SNI Server')
parser.add_argument('-o', '--output',#可选参数                    
                    required=False,#是否必须携带                    
                    default='SNIHosts.txt',#默认值                    
                    help='Pcap_DNSProxy NULL(Deny):A Record Hosts File')#帮助文档
parser.parse_args()

args = parser.parse_args()

f = open(args.output, 'w')
f.write('[Hosts]\n## IPv4 SNI Hosts Lists\n## Last update: '+d.datetime.now().strftime("%Y.%m.%d %H:%M:%S")+'\n\n')

try:
	r = open(args.input, 'r')
	result = list()
	for line in r.readlines():
		line=line.strip()
		if not len(line) or line.startswith('#'):        #注释行处理
			continue
		else:
			result.append(args.sni+' '+line)
	f.write('%s' % '\n'.join(result)) #保存入结果文件
except IOError as e:
	print("File is not accessible")
	sys.exit(255)

