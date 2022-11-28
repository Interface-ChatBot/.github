from konlpy.tag import Komoran
ko=Komoran()
def n_list(sentence):#명사리스트로 변환
    return ko.nouns(sentence)
def m_list(sentence):#형태소 리스트로 변환
    return ko.morphs(sentence)
def s_list(sentence):#글자별 리스트로 변환(슬라이싱)
    s=[]
    for i in range(len(sentence)):
        if(sentence[i]==' '):
            continue
        else:
            s.append(sentence[i])
    return s
def ngram(bow,num_gram):#n그램 방식으로 튜플로 전환
    text=tuple(bow)
    if len(bow)==1:            
        num_gram=1
    ngrams=[text[x:x+num_gram] for x in range(0,len(text))]
    return tuple(ngrams)

def similarity(x,y):#유사도 검사를 실행
    cnt=0
    for token in x:
        if token in y:
            cnt=cnt+1
    return cnt/len(x)
def check(sentence):
    for i in range(len(sentence)):
        if('z'>=sentence[i]>='a'or 'Z'>=sentence[i]>='A'):
            return 1
    return 0
def evaluation(input_sentence,sentence):#유사도에 따른 유사함 비교
    if check(input_sentence):
        a1=ngram(s_list(input_sentence),1)
        b1=ngram(s_list(sentence),1)
        print(similarity(a1,b1))
        if similarity(a1,b1)>=0.5:
             print("유사함")
        else: 
            print("유사하지 않음")
    else:
        cnt=0
        a1=ngram(s_list(input_sentence),1)
        a2=ngram(n_list(input_sentence),1)
        a3=ngram(m_list(input_sentence),1)
        b1=ngram(s_list(sentence),1)
        b2=ngram(n_list(sentence),1)
        b3=ngram(m_list(sentence),1)
        if(similarity(a2,b2)>=0.5):
            cnt+=0.1
        if(similarity(a3,b3)>=0.5):
            cnt+=0.1
        if(similarity(a1,b1)+cnt>=0.5):
            print(similarity(a1,b1)+cnt)
            print("유사합니다.")
        else:
            print("유사하지 않습니다.")
a=input()
b="동방비밀번호"
evaluation(a,b)
