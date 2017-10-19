# -*- coding:utf-8 -*-

import os
from sys import argv
import click

@click.command()
@click.option("-n", help="qing shu ru yi ge wang luo hao", prompt='请输入一个网络号')
@click.option("-r", help="qing shu ru yi ge di zhi fan wei eg: 101-201", prompt='请输入开始和结束地址并以“-”号分隔')

def IP_address(n,r):
#接受外部传入的地址段
	IP_net = n
	IP_range = r

#以"."对IP地址段进行分割，并存为列表
	IP_address_list = IP_net.split('.')
	
#判断网络合法性
	if len(IP_address_list) != 4 or int(IP_address_list[0]) > 255 or int(IP_address_list[1]) > 255 or int(IP_address_list[2]) > 255 or int(IP_address_list[3]) > 255:
		print "IP地址不合法！"
		return

	ping_lists = []
	ip_number = 0

#以"-"对地址范围进行分割
	IP_range_xy = IP_range.split('-')
	IP_range_x = int(IP_range_xy[0])
	IP_range_y = int(IP_range_xy[1])
	
#判断地址范围合法性
	if IP_range_x > IP_range_y or IP_range_x > 255 or IP_range_y > 255:
		print "地址范围不合法！"
		return

	for change_address in range(IP_range_x,IP_range_y + 1):

#循环修改最后一个字段的地址号
		IP_address_list[-1] = str(change_address)

#以"."重组IP地址
		IP_address = '.'.join(IP_address_list)

		ping_list = os.popen("ping %s -w 1 -c 1 | grep 'bytes from'" % IP_address)
		ping_list = ping_list.read()
		ping_list = ping_list.replace("\n","")
	
		datalen = len(ping_list)
		if datalen != 0:
			print "\033[1;32;42m" + IP_address + "\033[0m"
			ping_lists.append(ping_list)
			ip_number += 1
		else:
			print IP_address
	print "\n" + "_" * 60 + "\n"
	print "Ping检测完成"

	for i in ping_lists:
		print i

	print "主机在线数为：%d 台 \n" % ip_number


if __name__ == '__main__':
	IP_address()
