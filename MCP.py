__author__ = 'Administrator'
#coding=utf-8
import copy

relation={}
relation['1']=set(['a','b','c'])
relation['a']=set(['1','b','3','c'])
relation['b']=set(['1','a','c','3'])
relation['c']=set(['1','a','b','3','d','e','2'])
relation['d']=set(['c','2','e','3'])
relation['e']=set(['3','d','2','c'])
relation['2']=set(['c','d','e',])
relation['3']=set(['a','b','c','d','e'])
# relation['1']=set(['2','3'])
# relation['2']=set(['1','3'])
# relation['3']=set(['2','1'])
all=set(relation.keys())

def mcp(all):
    result=[]
    if all.__len__()<=1:
        result.append(all)
        return result
    temp=copy.copy(all)
    while temp.__len__()!=0:
        t=temp.pop()
        nextlist=mcp(relation[t]&all)
        for n in nextlist:
            result.append(set(t)|n)
            temp=temp-n
    return result
for t in mcp(all):
    print(t)