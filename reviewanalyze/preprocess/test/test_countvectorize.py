from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt

test_instance = [
    "녹는다 녹아",
    "좋아요",
    "흠잡을곳 없는 반찬이 정갈합니다",
    "코로나 땜에 걱정했는데 방역수칙도 잘 지키시고 살치실이랑 등심 부드러워서 너무 좋아",
    "살치살 미쳤네요 대박입니다 퀄리티 굳이에요",
]

def get_pos(x):
    tagger = Okt()
    pos = tagger.pos(x)
    pos = [word for word, _ in pos]
    return pos



if __name__ == "__main__":
    index_vectorizer = CountVectorizer(tokenizer=lambda x: get_pos(x))
    X = index_vectorizer.fit_transform(test_instance)
    print(X.shape)