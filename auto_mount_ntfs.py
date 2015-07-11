#!/usr/bin/env python
#coding=utf-8
import os
import subprocess
import re
def main():
	#subprocess.call("sudo blkid")
	mount_point_pre = "/media/"
	label = 'C'
	appendStr = ""
	p = subprocess.Popen("sudo blkid", stdout=subprocess.PIPE, shell = True)
	(uuidListStr, err)  = p.communicate()
	pattern = re.compile('UUID="([^"]+)"')
	uuidList = pattern.findall(uuidListStr)

	pattern = re.compile('TYPE="([^"]+)"')
	pTypeList = pattern.findall(uuidListStr)
	for (uuid,pType) in zip(uuidList,pTypeList):
		if (pType == "ntfs") :
			mount_point = mount_point_pre + label 
			mkdir(mount_point)
			appendStr += "UUID=%s	%s	ntfs	defaults	0	0\n" %(uuid, mount_point) 
			label = chr(ord(label)+1)
	os.system("cp /etc/fstab /etc/fstab_bak")
	with open("/etc/fstab", 'a') as fp:
		#print fp.readall();
		print appendStr
		fp.write(appendStr)
	print "Success\n"


def mkdir(path):
	# 引入模块
	import os

	# 去除首位空格
	path=path.strip()
	# 去除尾部 \ 符号
	path=path.rstrip("\\")

	# 判断路径是否存在
	# 存在     True
	# 不存在   False
	isExists=os.path.exists(path)

	# 判断结果
	if not isExists:
		# 如果不存在则创建目录
		print path+' 创建成功'
		# 创建目录操作函数
		os.makedirs(path)
		return True
	else:
		# 如果目录存在则不创建，并提示目录已存在
		print path+' 目录已存在'
		return False
main()
