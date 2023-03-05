# -*- coding: utf-8 -*-
from konlpy.tag import Komoran

ko=Komoran()

def n_list(sentence):#문장에서 명사 리스트 추출
    return ko.nouns(sentence)

def m_list(sentence):
    return ko.morphs(sentence)

def s_list(sentence):
    s=[]
    print("sentence")
    print(sentence)
    for i in range(len(sentence)):
        print(i)
        if sentence[i]==' ':
            continue
        else:
            s.append(sentence[i])

    return s

def ngram(bow,num_gram):#bow에는 위에 함수를 통한 명사 리스트 ,num_gram 은 명사를 몇개씩 비교할지 정하는 수 높아 질수록 정확도는 올라가지만 유사도는 감소 
    text=tuple(bow)

    if len(bow)==1:            
        num_gram=1

    ngrams=[text[x:x+num_gram] for x in range(0,len(text))]

    return tuple(ngrams)

def similarity(x,y):#두 문장의 명사 튜풀을 넣고 같은 지 비교하고 유사도 리턴 (x,y는 위에 ngram함수를 통해 뽑은 명사 튜플)
    cnt=0

    for token in x:
        if token in y:
            cnt=cnt+1

    if len(x)==0:
        return 0
    
    return cnt/len(x)

def check(sentence):
    for i in range(len(sentence)):
        try:
            if('z'>=sentence[i]>='a'or 'Z'>=sentence[i]>='A'):
                return 1
        except KeyError:pass
    return 0


'''a=input()
b="와이파이"

if check(a):
    a1=ngram(s_list(a),1)
    print(a1)
    
    b1=ngram(s_list(b),1)
    print(b1)
    
    print(similarity(a1,b1))
    
    if similarity(a1,b1)>=0.5:
        print("유사함")
    else: 
        print("유사하지 않음")
        
else:
    cnt=0
    a1=ngram(s_list(a),1)
    b1=ngram(s_list(b),1)
    a2=ngram(n_list(a),1)
    a3=ngram(m_list(a),1)
    b2=ngram(n_list(b),1)
    b3=ngram(m_list(b),1)
    
    if(similarity(a2,b2)>=0.5):
        cnt+=0.1
    if(similarity(a3,b3)>=0.5):
        cnt+=0.1
    if(similarity(a1,b1)+cnt>=0.5):
        print(similarity(a1,b1)+cnt)
        print("유사합니다.")
    else:
        print("유사하지 않습니다.")'''
