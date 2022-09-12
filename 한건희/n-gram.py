from konlpy.tag import Komoran
def n_list(sentence):#문장에서 명사 리스트 추출
    return Komoran.nouns(sentence)
def ngram(bow,num_gram):#bow에는 위에 함수를 통한 명사 리스트 ,num_gram 은 명사를 몇개씩 비교할지 정하는 수 높아 질수록 정확도는 올라가지만 유사도는 감소 
    text=tuple(bow)
    ngrams=[text[x:x+num_gram] for x in range(0,len(text))]
    return tuple(ngrams)

def similarity(x,y):#두 문장의 명사 튜풀을 넣고 같은 지 비교하고 유사도 리턴 (x,y는 위에 ngram함수를 통해 뽑은 명사 튜플)
    cnt=0
    for token in x:
        if token in y:
            cnt=cnt+1
    return cnt/len(x)
def evaluation(x):#유사도가 60% 이상시 참 아닐시 거짓 리턴 x는 similarity 넣은면 됌
    if x>=0.6:
        return 1
    else:
        return 0
