#!/usr/bin/python3
'''
Created on 2016年 4月14日
@author: Westlor
'''
import jieba.posseg as pseg
import read_shell

switch={
    0:read_shell.read
};

mod = input("Please select mod: 0-read_shell, 1-ask_shell, 2-speak_shell...)");

while 1:
    print("...>>>");
    raw = input();
    
    if raw == "quit":
        print("Over...")
        quit() 
    else:
        switch[mod](raw)