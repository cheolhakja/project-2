import iterate_create_path
import rating_converter
import pull_out_korean
from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt


def get_pos(x):
    tagger = Okt()
    pos = tagger.pos(x)
    pos = [word for word, _ in pos]
    return pos

def execute():
    rating_review_list = (
        iterate_create_path.return_rating_review_list()
    )  # JSON파일을 리스트로 불러옴

    for i in range(len(rating_review_list)):
        new_rating = rating_converter.convert(
            rating_review_list[i].get_rating()
        )  # 모든 리뷰 데이터의 별점을 0과 1로 바꿈
        rating_review_list[i].set_rating(new_rating)  # 모든 리뷰 데이터의 별점을 0과 1로 바꿈

    for i in range(len(rating_review_list)):
        analyzed_review = pull_out_korean.leave_only_korean(rating_review_list[i].get_review())
        rating_review_list[i].set_review(analyzed_review) #리뷰에서 한글만 추출함

    only_korean_review_list = []  #Pair객체에서 리뷰만 빼서 리스트로 만들어봄
    for i in rating_review_list:
        only_korean_review_list.append(i.get_review())

    return only_korean_review_list    


if __name__ == "__main__":
    result_list = execute()

    index_vectorizer = CountVectorizer(tokenizer=lambda x: get_pos(x))
    X = index_vectorizer.fit_transform(result_list)
    print(X.shape)
    ##해결 CountVectorize의 tokenizer로 넘겨주면 되겟네 pull_out_korean의 analyze를
