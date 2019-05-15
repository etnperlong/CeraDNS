# -*- coding:utf-8 -*-

import datetime as d
import argparse
import sys
import json
import os
import urllib.request as request

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',
					required=False,
					default='hosts_source.json',
					help='Hosts source URL (default: hosts_source.json, use internel list if not provided)')
parser.add_argument('-o', '--output',
					required=False,
					default='adblock_hosts_merged.txt', 
					help='Merged Hosts file(default: adblock_hosts_merged.txt)')
parser.add_argument('-r', '--ip',
					required=False,
					default='127.0.0.1', 
					help='Redirect to IP(default: 127.0.0.1)')
parser.parse_args()
args = parser.parse_args()
HOSTS_TMP = "./hosts.tmp"

HOSTS_SOURCE_URL = [
    "https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts",
]

source = []
total_sum_line = 0

def _error_feedback(e, *arg):
	print("An Error occurred!\n",e,"\n",repr(arg))

def load_source():
	global source
	if not os.path.exists(args.input):
		source = HOSTS_SOURCE_URL
	else:
		source = json.load(open(args.input,mode="r"))

def get_raw(url):
	"""
	Get raw file of Hosts
	@param url: URL of Hosts
	"""
	try:
		with request.urlopen(url) as f:
			return f.read()
	except request.HTTPError as e:
		_error_feedback(e,url)
		return ""
	except request.URLError as e:
		_error_feedback(e,url)
		return ""
	except ValueError as e:
		_error_feedback(e,url)
		return ""
		

def simple_merge():
	global source, HOSTS_TMP
	print("Downloading Hosts ...")
	print(str(source))
	with open(HOSTS_TMP, mode="wb") as f:
		for i in source:
			print("Downloading %s from %s." % (os.path.split(i)[-1], i))
			f.write(get_raw(i))
			f.write(b"\n")
			print("Downloaded %s from %s." % (os.path.split(i)[-1],i))
	print("Downloaded..")
	
def bake_strip():
	"""
	Delete note & empty line
	"""
	global total_sum_line, HOSTS_TMP
	try:
		print("Baker[1/3]: Stripping useless line...")
		r = open(HOSTS_TMP, 'rb')
		baker = list()
		_count = 0
		for line in r.readlines():
			line=line.strip()
			if not len(line) or line.startswith(b'#'):
				continue
			else:
				baker.append(line)
				_count += 1
		# r.write('%s' % '\n'.join(baker))
		print("count of lines: " + str(_count))
		total_sum_line = _count
		return baker
	except IOError as e:
		print("File is not accessible")
		sys.exit(255)
		
def bake_dedup(baker):
	"""
	Delete duplicated host lines
	"""
	print("Baker[2/3]: Deduplicating...")
	baker_s1 = list()
	baker_s2 = list()
	for line in baker:
		hostname = line.split()[1]  #127.0.0.1 ad.com
		baker_s1.append(hostname)
	baker_s2 = list(set(baker_s1))
	baker_s2.sort(key=baker_s1.index)
	_count = len(baker_s2)
	print("count of lines: " + str(_count))
	return baker_s2
			
def bake_generate(baker):
	"""
	Generate Hosts
	"""
	global total_sum_line, source, HOSTS_TMP
	try:
		print("Baker[3/3]: Generating Hosts...")
		f = open(args.output, 'wb')
		HEADER_LINES = '#########################################\n' \
					   '#                                       #\n' \
					   '#         Adblock Merged Hosts          #\n' \
					   '#   Last Update: ' + d.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '    #\n' \
					   '#                                       #\n' \
					   '#           Credit: etnperlong          #\n' \
					   '#                                       #\n' \
					   '#########################################\n'
		
		DESP_LINES =  "#\n#  Original Hosts source:\n#\n"
		for desp_line in source:
			DESP_LINES += '# ' + desp_line + "\n"
		DESP_LINES += "#\n#  Total Host Line: " + str(total_sum_line) + "\n\n\n"
		
		HOST_LINES = ""
		for host_line in baker:
			HOST_LINES += str(args.ip) + ' ' + host_line.decode() + "\n"

		FULL_HOSTS_LINES = HEADER_LINES + DESP_LINES + HOST_LINES
		f.write(FULL_HOSTS_LINES.encode('utf8')) #Save File
		print("Cleaning temp file...")
		os.remove(HOSTS_TMP)
		print("Successfully merged Hosts!")
		
	except IOError as e:
		print("File is not accessible")
		sys.exit(255)
		
if __name__ == "__main__":
	load_source()
	simple_merge()
	pan = bake_strip()
	jam = bake_dedup(pan)
	oreo = bake_generate(jam)