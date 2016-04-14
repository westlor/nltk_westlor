#!/usr/bin/python3
#nltk:bin:python3:r_shell.py
import nltk
import jieba
import jieba.posseg as pseg

while 1:
	print("...");
	raw = input();
	print(raw);	
	words = pseg.cut(raw)
	for word, flag in words:
		print('%s->%s' % (word, flag))
	if word == "quit":
		quit()
	else
	

print("Over...");
