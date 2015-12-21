#-*-coding:utf-8-*-
#寻找100以内最大的平方数
from math import sqrt
for n in range(99,0,-1):
	root = sqrt(n)
	print str(n)+"----"+str(root)
	if root == int(sqrt(n)):
		print "最大的是："+str(n)+"----"+str(root)
		break
