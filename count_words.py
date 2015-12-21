#-*-coding:utf-8-*-
file_name = raw_input('输入txt文件名字：')
file = open(file_name+'.txt','r')
f1 = file.readline()
f = f1.replace('.','')
file_content = f.split()

for i in range(0,len(file_content)):
	words_count = file_content.count(file_content[i])
	print str(i+1) +'. '+ str(file_content[i]) +' : '+ str(words_count)
