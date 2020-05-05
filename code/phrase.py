'''
Created on 2018年3月15日

@author: westl
短语划分
'''
import part_of_speech

def divide(sentence):
    slen = len(sentence)
    newSentence = []
    for index in range(slen):
        # 并列短语：是由两个或两个以上的名词、动词或形容词并列组成的，词和词之间是平等的联合，没有轻重主次之分。
        if index > 0:
            if part_of_speech.is_nominal_equals(sentence[index][1] , sentence[index-1][1]):
                list_word = list(newSentence[index-1])
                list_word[0] = list_word[0] + sentence[index][0]
                temp = part_of_speech.get_nominal_simple(list_word[1])
                list_word[1] = temp[0]
                list_word[2] = temp[1]
                newSentence[index-1] = tuple(list_word)
            else:
                newSentence.append(sentence[index])
        else:
            newSentence.append(sentence[0])     
    print(newSentence)   
 
