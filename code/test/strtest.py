#!/usr/bin/python3
#encoding=utf-8
'''
Created on 2016年4月25日

@author: Westlor
'''
# 查找arr元组中item项的索引
from _multiprocessing import flags
def find_all_index(arr,item): 
    return [i for i,a in enumerate(arr) if a==item] 

# 去除句子中的副词
def rm_adverb(words, flags):
    for w,f in zip(words,flags):
        if f == 'd':
            words.remove(w)
            flags.remove(f)
            print(words)
            print(flags)

if __name__ == '__main__':
    
    if 'hehe' in "afs d hehefeswfeheh... heh fsdfds":
        print("hehe")
        
    words = ['wo', 'shi', 'fds', 'ha', 'he', 'f', 'fdsf', 'hi']
    flags = ['n', 'v', 'd', 'b', 'a', 'dd', 'd', 'fd']
    
    print(words)
    print(flags)
    
    rm_adverb(words, flags)
        
    pass