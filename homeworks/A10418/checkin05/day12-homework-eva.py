#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	tup=(1,2,3,4)


	#取值
	print tup[1]

	#切片
	print tup
	print tup[0:3]
	print tup[2:]

	#是否存在某值
	print (1 in tup)
	print (5 in tup)

	#赋值
	a,b,c,d = (1,2,3,4)
	print a
	print b
	print c
	print d

	#遍历
	for item in tup:
		print item

	# print 'enumerate'
	for index, item in enumerate(tup):
		print index

	return tup

	print '--------'

#Homework: try

def main2(tup):
	#1)插入
	try:
		tup.append('6')
	except Exception,e:
		print e

	#2)修改
	try:
		tup[0]='aaa'

	except Exception,e:
		print e

	#3)删除
	try:
		del tup[0]
	except Exception,e:
		print e

if __name__ == '__main__':
	tup = main()
	main2(tup)
