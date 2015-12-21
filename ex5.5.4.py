#-*-coding:utf-8-*-

#对应显示姓名和年龄

names = ['anne','beth','george','damon']
ages = [12,45,32,102]
#方法一：
for i in names:
	print i+' is '+str(ages[names.index(i)])+' years old.'
print '-' * 25

#方法二：
for j in range(len(names)):
	print names[j],'is',ages[j],'years old.'
print '-' * 25

#方法三：
zip(names,ages)
for name, age in zip(names,ages):
	print name,'is',age,'years old.'
print '-' * 25
