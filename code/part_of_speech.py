'''
Created on 2018年3月1日

@author: westlor
@explain: 对句子进行拆分
'''
import jieba.posseg as posseg
import nltk

'''
NOUN n,VERB v ,ADJ a, ADV r, ADJ_SAT s
    NOUN: [('s', ''), ('ses', 's'), ('ves', 'f'), ('xes', 'x'),
               ('zes', 'z'), ('ches', 'ch'), ('shes', 'sh'),
               ('men', 'man'), ('ies', 'y')],
    VERB: [('s', ''), ('ies', 'y'), ('es', 'e'), ('es', ''),
               ('ed', 'e'), ('ed', ''), ('ing', 'e'), ('ing', '')],
    ADJ: [('er', ''), ('est', ''), ('er', 'e'), ('est', 'e')],
    ADV: [],
    ADJ_SAT:[('er', ''), ('est', ''), ('er', 'e'), ('est', 'e')]
    pos_tag(word_tokenize("John's big idea isn't all that bad.")) # doctest: +SKIP
        [('John', 'NNP'), ("'s", 'POS'), ('big', 'JJ'), ('idea', 'NN'), ('is',
        'VBZ'), ("n't", 'RB'), ('all', 'DT'), ('that', 'DT'), ('bad', 'JJ'),
        ('.', '.')]
1.      CC      Coordinating conjunction 连接词   c
2.     CD     Cardinal number  基数词             m

3.     DT     Determiner  限定词（如this,that,these,those,such，不定限定词：no,some,any,each,every,enough,either,neither,all,both,half,several,many,much,(a) few,(a) little,other,another.
4.     EX     Existential there 存在句
5.     FW     Foreign word 外来词

6.     IN     Preposition or subordinating conjunction 介词或从属连词     p
7.     JJ     Adjective 形容词或序数词                                    a
8.     JJR     Adjective, comparative 形容词比较级
9.     JJS     Adjective, superlative 形容词最高级

10.     LS     List item marker 列表标示
11.     MD     Modal 情态助动词

12.     NN     Noun, singular or mass 常用名词 单数形式
13.     NNS     Noun, plural  常用名词 复数形式
14.     NNP     Proper noun, singular  专有名词，单数形式
15.     NNPS     Proper noun, plural  专有名词，复数形式
16.     PDT     Predeterminer 前位限定词
17.     POS     Possessive ending 所有格结束词

20.     RB     Adverb 副词
21.     RBR     Adverb, comparative 副词比较级
22.     RBS     Adverb, superlative 副词最高级
23.     RP     Particle 小品词
24.     SYM     Symbol 符号
25.     TO     to 作为介词或不定式格式
26.     UH     Interjection 感叹词
27.     VB     Verb, base form 动词基本形式
28.     VBD     Verb, past tense 动词过去式
29.     VBG     Verb, gerund or present participle 动名词和现在分词
30.     VBN     Verb, past participle 过去分词
31.     VBP     Verb, non-3rd person singular present 动词非第三人称单数
32.     VBZ     Verb, 3rd person singular present 动词第三人称单数
33.     WDT     Wh-determiner 限定词（如关系限定词：whose,which.疑问限定词：what,which,whose.）

18.     PRP     Personal pronoun 人称代词
19.     PRP$     Possessive pronoun 所有格代名词
34.     WP      Wh-pronoun 代词（who whose which）
35.     WP$     Possessive wh-pronoun 所有格代词
36.     WRB     Wh-adverb   疑问代词（how where when）
'''
ParticipleName = {'Ag':'形语素', 'a':'形容词', 'ad':'副形词', 'an':'名形词', 
                  'b':'区别词', 'c':'连词', 'dg':'副语素', 'd':'副词', 
                  'e':'叹词', 'eng':'英文', 'f':'方位词', 'g':'语素', 'h':'前接成分', 
                  'i':'成语', 'j':'简称略语', 'k':'后接成分', 'l':'习用语', 
                  'm':'数词', 'ng':'名语素', 'n':'名词', 'nr':'人名', 'ns':'地名', 
                  'nt':'机构团体', 'nz':'其他专名', 'o':'拟声词', 'p':'介词', 
                  'q':'量词', 'r':'代词', 's':'所处词', 'tg':'时语素', 't':'时间词', 
                  'u':'组词', 'vg':'动语素', 'v':'动词', 'vd':'副动词', 'vn':'名动词', 
                  'w':'标点符号', 'x':'非语素字', 'y':'语气词', 'z':'状态词', 'un':'未知词', 'E':'英文', 'U':'未知词'};
                  
ParticipleToNLTK = {'Ag':'JJ', 'a':'JJ', 'ad':'RB', 'an':'JJ', 
                  'b':'区别词', 'c':'CC', 'dg':'RB', 'd':'RB', 
                  'e':'UH', 'eng':'英文', 'f':'方位词', 'g':'语素', 'h':'前接成分', 
                  'i':'成语', 'j':'简称略语', 'k':'后接成分', 'l':'习用语', 
                  'm':'CD', 'ng':'名语素', 'n':'NN', 'nr':'人名', 'ns':'地名', 
                  'nt':'机构团体', 'nz':'其他专名', 'o':'拟声词', 'p':'IN', 
                  'q':'量词', 'r':'WP', 's':'所处词', 'tg':'时语素', 't':'时间词', 
                  'u':'组词', 'vg':'动语素', 'v':'VB', 'vd':'副动词', 'vn':'名动词', 
                  'w':'SYM', 'x':'非语素字', 'y':'语气词', 'z':'状态词', 'un':'未知词' };
        
def is_nominal_equals(nominal1, nominal2):
    if(nominal1 == nominal2):
        return True
    elif nominal1 == 'eng' or nominal2 == 'eng':
        return False
    elif nominal1 == 'un' or nominal2 == 'un':
        return False
    if nominal1[0].upper() == nominal2[0].upper():
        return True;
    else:
        return False;        
                  
def get_nominal_simple(nominal):
    nominal_s = nominal
    if nominal == 'Ag':
        nominal_s = 'a'
    elif nominal == 'eng':
        nominal_s = 'E'
    elif nominal == 'un':
        nominal_s = 'U'

    try:
        nominal_simple = (nominal_s[0], ParticipleName[nominal_s[0]])
    except KeyError:
        nominal_simple = (nominal_s[0], '未知词')
    return nominal_simple

# 分词，返回词组，词性标注
def word_segmentation(sentence):
    sentence_seg         = []
    
    print("input:" + sentence)
    words = posseg.cut(sentence)

    for w in words:
        try:
            sentence_seg.append((w.word, w.flag, ParticipleName[w.flag]))
        except KeyError:
            sentence_seg.append((w.word, w.flag, '未知词'))
    
    print(sentence_seg)
    return sentence_seg

def chunking(sentence):
#     text = nltk.word_tokenize(sentence, language='english')
#     print(text)
#     texts = nltk.pos_tag(text)
#     print(texts)    
    grammar = "n_uj_adj: {<n><uj>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    print(result)
    result.draw()