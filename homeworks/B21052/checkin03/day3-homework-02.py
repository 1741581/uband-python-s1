#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def main():
	who = '焦糖的妈妈'
	good_description = '西双版纳大白菜'

	good_price = 2
	reasonable_price = 5
	buy_amount = 2

	is_cheap = False 
	
	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
		 buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
	main ()