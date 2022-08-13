from konlpy.tag import Komoran 
def ng(bow,num_gram):
    text=tuple(bow)
    ngrams=[text[x:x+num_gram] for x in range(0,len(text))]
    return tuple(ngrams)
def similarity(doc1,doc2):
    cnt=0
    for t in doc1:
        if t in doc2:
            cnt=cnt+1
    return cnt/len(doc1)

sentence1='인터페이스 챗봇을 8월달에 만들어 보자.'
sentence2='인터페이스 홈페이지를 8월 달에 만들어 보자.'
sentence3='인터페이스는 정말 좋은 동아리다.'

komoran=Komoran()
bow1=komoran.nouns(sentence1)
bow2=komoran.nouns(sentence2)
bow3=komoran.nouns(sentence3)

result1=ng(bow1,2)
result2=ng(bow2,2)
result3=ng(bow3,2)

print("문장 1과 문장2의 유사도:",similarity(result1,result2))
print("문장 1과 문장3의 유사도:",similarity(result1,result3))
print("문장 2와 문장3의 유사도:",similarity(result2,result3))



