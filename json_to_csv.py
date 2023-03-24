import csv
import preprocessor
import os
import json
from pandas import read_csv


def write_csv():
    f = open('write.csv','w', newline='')
    wr = csv.writer(f)
    wr.writerow([1,'림코딩', '부산'])
    wr.writerow([2,'김갑환', '서울'])
 
    f.close()

if __name__ == "__main__":
    a = [1,'림코딩', '부산']
    print(type(a))
    print(a)

    rating_list, review_list = preprocessor.execute()    
    print(len(rating_list))
    print(len(review_list)) #리뷰가 비어있으면 무시하므로 총 41개에서 36개로 줄었음

    f = open(R'C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\csv\write.csv','w', newline='')
    wr = csv.writer(f)

    for i in range(len(rating_list)):
        li = []
        li.append(rating_list[i])
        li.append(review_list[i])
        wr.writerow(li)

    f.close()   

    df = read_csv(R'C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\csv\write.csv', encoding='cp949')
    df.columns = ['y', 'ko_text']
    df.to_csv(R'C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\csv\write.csv')


