from konlpy.tag import Okt
import re

def leave_only_korean(text):
    korean_left = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
    result = korean_left.sub('', text) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    return result

def get_morpheme(x):
    tagger = Okt()
    pos = tagger.pos(x)
    #pos = ['{}/{}'.format(word,tag) for word, tag in pos] : 분류대상 - 분류 를 format형식에 맞게 출력하기 위한 작업.
    return [word for word, _ in pos]

def analyze(text: str) -> str:
    return get_morpheme(leave_only_korean(text))
    
def test():
    result = leave_only_korean(u'네, 안녕하세요. 반갑습니다.')
    print(result)
    print(type(result))
    parse_morpheme_result = get_morpheme(leave_only_korean(u'네, 안녕하세요. 반갑습니다.'))
    print(parse_morpheme_result) #느리긴 하다..

if __name__ == "__main__":
    test()

    