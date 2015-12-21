#-*-coding:utf-8-*-
file_name = raw_input('输入txt文件名字：')
file = open(file_name+'.txt','r')
f = file.readline()
file_content = f.split()
print "内容为："+str(file_content)
print "-"*20

#character = [',','。','.','?']
#单词计算：
for i in range(0,len(file_content)):
	clean_file_content = file_content[i].replace('.','')
	#print clean_file_content
	words_count = clean_file_content.count(file_content[i])
	print str(i+1) +'. '+ str(clean_file_content) +' : '+ str(words_count)


		

