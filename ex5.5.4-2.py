#-*-coding:utf-8-*-
#把包含 -- 的全部进行替换
strings = ['roc--','max','charles--']
print strings
index = 0
for string in strings:
	if '--' in string:
		strings[index] = 'changed part'
	index += 1
print strings