#!/usr/bin/env python3
import csv
import os
import re
import operator
error={}
user={}

with open('txt.txt') as syslog:
	for log in syslog.readlines():
		result = re.search(r'ticky: ([A-Z]+) ([\w \']*)[\[\]\d#]* \(([\w\.]+)\)',log)
		name=result.group(3)
		log_type=result.group(1)
		log_desc=result.group(2)
		if name not in user:
			user[name]=[0,0]
		if log_type=='INFO':
			user[name]=[user[name][0]+1,user[name][1]]
		else:
			error[log_desc]=error.get(log_desc,0)+1
			user[name]=[user[name][0],user[name][1]+1]

sorted(error.items(),key=operator.itemgetter(1),reverse=True)
sorted(user.items(),key=operator.itemgetter(0))

with open('error_message','w') as errors:
	writer = csv.writer(errors)
	writer.writerow(['Error','Count'])
	for error,count in sorted(error.items(),key=operator.itemgetter(1),reverse=True):
		writer.writerow([error,count])
with open('user_statistics.csv','w') as users:
	writer = csv.writer(users)
	writer.writerow(['Username','INFO','ERROR'])
	for user,stat in sorted(user.items(),key=operator.itemgetter(0)):
		writer.writerow([user,stat[0],stat[1]])
