'''
Created on 2016年4月25日

@author: Westlor
'''

# 查找arr元组中item项的索引
def find_all_index(arr,item): 
    return [i for i,a in enumerate(arr) if a==item] 

if __name__ == '__main__':
    pass