#!/usr/bin/env python
#coding=utf-8
###File Name:uninstall.py
###Author:haicg
###Mail:lihaicg@126.com
###Created Time: 2015年12月13日 星期日 18时07分43秒
###File Name : rm_files_according_dir.py
#目前仅仅是能运行，还有很多不完善的地方
#note: 本程序主要是通过对文件夹的扫描和比对，来删除目标路劲下和源文件夹中同名的文件

'''
1.有些地方的判断是多余的，可以简化
'''
Usage =\
'''
Usage : uninstall.py DEST SOURCE
'''

import sys
import os
import pdb
src_root = ""
dst_root = ""
src_dir = []
src_dir_mask = []

class fileState:
    read_flag = 0
    path = ""
    def __init__(self, path):
        self.read_flag = 0
        self.path = path


def deal_one_dir(file_struct_val):
    global src_root
    global dst_root
    global src_dir
    pop_flag = 0
    src_relative = file_struct_val.path
    print src_root + src_relative
    if src_relative == ".":
        src_relative = ""

    src_absolute_path = src_root+"/"+src_relative
    dst_absolute_path = dst_root+"/"+src_relative

    if (os.path.isdir(dst_absolute_path)):
        print len(os.listdir(dst_absolute_path))
        if (len(os.listdir(dst_absolute_path)) == 0):
            os.rmdir(dst_absolute_path)
            src_dir.pop()
            return
    else :
        src_dir.pop()
        return
    if (file_struct_val.read_flag == 1):
        src_dir.pop()
        return
    files = os.listdir(src_absolute_path)
    file_struct_val.read_flag = 1;

    for file in files:
        file_path = dst_absolute_path + "/" + file
        file_path = os.path.normpath(file_path)
        print "dst_absolute_path " + file_path
        if (os.path.isdir(file_path)):
            if (len(os.listdir(file_path)) != 0):
                file_struct_val2 = fileState(src_relative + "/" + file)
                src_dir.append(file_struct_val2)
            else:
                os.rmdir(file_path)
        else :
            if (os.path.exists(file_path)):
                pop_flag = 1
                os.remove(file_path)


def main():
    global src_root
    global dst_root
    global src_dir
    if len(sys.argv) < 3:
        print Usage
        #print "Please input parm"
        exit(1)
#for i in range(1,len(sys.argv)):
#   print "parm", i, sys.argv[i]
    print "script name :", sys.argv[0]
    print "DST dir is :", sys.argv[1]
    print "SRC dir is :", sys.argv[2]
    confirm = raw_input("Are you confirm del files from " + sys.argv[1] + "(default y)\n")
    print confirm
    if not (confirm == 'y' or confirm == 'Y' or confirm == ""):
        exit(1)
    if os.path.isabs(sys.argv[2]):
        src_root = sys.argv[2]
    else:
        src_root = os.getcwd() + "/" + sys.argv[2]
    if os.path.isabs(sys.argv[1]):
        dst_root = sys.argv[1]
    else:
        dst_root = os.getcwd() + "/" + sys.argv[1]

    file_struct_val = fileState(".")
    src_dir.append(file_struct_val)
    print dst_root + "   " + src_root
    while len(src_dir) != 0:
        print len(src_dir)
        print src_dir
        deal_one_dir(src_dir[-1])

main()
