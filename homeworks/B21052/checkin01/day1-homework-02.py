#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @author: caramel


# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print
def main():
	who = '焦糖的妈妈'
	good_price = 6 #小贩的价格
	good_description = '西双版纳的大白菜' #小贩的招牌
	is_cheap = False
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	#开始秀
	#一次跑通吧
	print "%s上街看到了 %s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	#practice
	#看着 day1-sample-code.py 

	# run function
if __name__ == '__main__':
  main()