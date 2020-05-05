'''
Created on 2018年3月15日

@author: westl
'''
def classification(sentence):
    content    = []
    functional = []
    for words in sentence:
        if words[2] in ('副词', '介词', '连词', '助词'):
            functional.append(words[0])
        else:
            content.append(words[0])
            
    print('实词：' , content)
    print('虚词：' , functional)