#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

def main():
  #01.int 
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7
  print 'Total number %d' % (apple_number + pie_number)
  print 'pie price is %d yuan higher than apple price' %(pie_price - apple_price)
  
  #02. *  /
  apple_total_price = apple_number * apple_price
  pie_total_price = pie_number * pie_price
  average_price = apple_total_price / apple_number
  rest = apple_total_price % apple_number
  print 'apple total price is %d'  % apple_total_price
  print 'average price is %g' % (average_price)
  print 'After divided, the rest is %d' %(rest)
  #03. try to explain what's float
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %g ' % (pie_total_price)
  print 'pie cost %0.2f ' % (pie_total_price)

  #04. **
  number = 2**3
  print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  if 1!= 2 and 1 >= 2 :
    print 'test1: %d' % (1 != 2)
    print 'test12: %d' % (1 >= 2)
  if 1 != 2 or 1 >= 2 :
  	print 'test21: %d' % (1 != 2)
  	print 'test22: %d' % (1 >= 2)
  if 1:
    print 'goog'
  if 0:
    print 'xxx'

  if(2 != 2):
    print 'wweewe we w'
  #请开始你的表演


if __name__ == '__main__':
  main()