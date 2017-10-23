#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,sys,shutil,time,commands

#定义系统常用变量
fstabdir = '/etc/fstab'
uuiddir = '/dev/disk/by-uuid/'
mountdir = '/storage/'

#将fstab文件中现有的UUID做成List为 fstablist
fstablist = []
fstab = os.popen("grep UUID %s | awk '{print $1}'" % fstabdir)
for fstab in fstab.readlines():
    fstab = fstab.replace('UUID=', '')
    fstab = fstab.replace('\n','')
    fstablist.append(fstab)

#将目录下的UUID和设备名，分别做成两个List为 uuid 和 dev
uuid = []
dev = []
uuid_dev = os.popen("ls -l %s | grep vd | awk '{print $9,$11 | \"sort -k2\"}'" % uuiddir)
for uuid_dev in uuid_dev.readlines():
    uuid_dev = uuid_dev.replace('../../','')
    uuid_dev = uuid_dev.split()
    uuid.append(uuid_dev[0])
    dev.append(uuid_dev[1])

#判断如果uuid不在fstablist中则打印uuid和对应的dev到fstab中
i = 0
while i < len(uuid) :
    if uuid[i] not in fstablist:
        fstabline = 'UUID=' + uuid[i] + ' ' + mountdir + dev[i] + ' ' + '       xfs     ' + 'defaults   ' + '0 0'
        fstabfile = open(fstabdir,'a')
        fstabfile.write(fstabline + '\n')
    i += 1

#没有写 mount -a ;chown -R mfs:mfs /storage
