#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting
import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('yellow')
	#生成一个绿乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('green')
	#设置速度
	bran.speed(1)
	#走几步
	for i in range(1,10):
		bran.forward(250)
		bran.left(90) 
		bran.forward(250)
		bran.left(90)
		bran.forward(250)
		bran.left(90)
		bran.forward(250)
		bran.left(90)
	#停下来
	screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))


if __name__ == '__main__':
	main()