import pandas as pd
import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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

df['label'] = df['score'].apply(lambda x: 1 if float(x) > 3 else 0) #df[label]과 df[y]는 같은 것이다


df.to_csv("review_data.csv", index=False)

df = pd.read_csv("review_data.csv")
df_2 = pd.read_csv(R'C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\csv\write.csv')

df['ko_text'] = df['review'].apply(lambda x: text_cleaning(x))
del df['review']


# 한 글자 이상의 텍스트를 가지고 있는 데이터만 추출합니다
df = df[df['ko_text'].str.len() > 0]
print(df)

index_vectorizer = CountVectorizer(tokenizer = lambda x: get_pos(x))
X = index_vectorizer.fit_transform(df['ko_text'].tolist())
print(X.shape)

tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

y = df['y']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
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

#---
print("------\n")
index_vectorizer_2 = CountVectorizer(tokenizer = lambda x: get_pos(x))
X_2 = index_vectorizer_2.fit_transform(df_2['ko_text'].tolist())
print(X_2.shape)

tfidf_vectorizer_2 = TfidfTransformer()
X_2 = tfidf_vectorizer_2.fit_transform(X_2)

y_2 = df_2['y']
x_train_2, x_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2, test_size=0.20)
print(x_train_2.shape)
print(x_test_2.shape)

lr_2 = LogisticRegression(random_state=0)
lr_2.fit(x_train_2, y_train_2)
y_pred_2 = lr_2.predict(x_test_2)

# 로지스틱 회귀모델의 성능을 평가합니다.
print("accuracy: %.2f" % accuracy_score(y_test_2, y_pred_2))
print("Precision : %.3f" % precision_score(y_test_2, y_pred_2))
print("Recall : %.3f" % recall_score(y_test_2, y_pred_2))
print("F1 : %.3f" % f1_score(y_test_2, y_pred_2))
