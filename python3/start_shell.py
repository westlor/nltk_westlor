#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
Created on 2016年 4月14日
@author: Westlor
'''
import read_shell
import ask_shell

switch={
    '0': read_shell.read,
    '1': ask_shell.read,
};

mod = input("Please select mod: 0-read_shell, 1-ask_shell, 2-speak_shell...):~$ ");

while 1:
    raw = input("ws@nltk:~$ ");
    
    if raw == "quit":
        print("Over...")
        quit() 
    elif raw == '':
        pass
    else:
        switch.get(mod)(raw)