# https://github.com/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch11/Sentiment_Analysis.ipynb 

import pandas as pd
import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np



# konlpy라이브러리로 텍스트 데이터에서 형태소를 추출합니다.
def get_pos(x):
    tagger = Okt()
    pos = tagger.pos(x)
    pos = ['{}/{}'.format(word,tag) for word, tag in pos]
    return pos

# 텍스트 정제 함수 : 한글 이외의 문자는 전부 제거
def text_cleaning(text):
    # 한글의 정규표현식으로 한글만 추출합니다.
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    return result

df = pd.read_csv("review_data.csv")
df_2 = pd.read_csv(R'C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\csv\write.csv')

df['ko_text'] = df['review'].apply(lambda x: text_cleaning(x))
del df['review']
df = df[df['ko_text'].str.len() > 0]

review_data_train = df['ko_text'].tolist() + df_2['ko_text'].tolist()

index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
X = index_vectorizer.fit_transform(review_data_train)

tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

y = df['y']
yy = df_2['y']

series_to_array = yy.values
print(type(series_to_array))

print(series_to_array)
print("\n\n")
print(yy)
result = np.concatenate((y,yy),axis=0)

#모델을 학습합니다
print("----------학습----------")
x_train, x_test, y_train, y_test = train_test_split(X, result, test_size=0.20)
print(x_train.shape)
print(x_test.shape)

lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

# 로지스틱 회귀모델의 성능을 평가합니다.
print("accuracy: %.2f" % accuracy_score(y_test, y_pred))
print("Precision : %.3f" % precision_score(y_test, y_pred))
print("Recall : %.3f" % recall_score(y_test, y_pred))
print("F1 : %.3f" % f1_score(y_test, y_pred))


