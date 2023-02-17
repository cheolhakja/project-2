import iterate_create_path
import rating_converter

def execute():
    rating_review_list = iterate_create_path.return_rating_review_list() #JSON파일을 리스트로 불러옴
    print(type(rating_review_list))
        
    for i in range(len(rating_review_list)):
        new_rating = rating_converter.convert(rating_review_list[i].get_rating()) #모든 리뷰 데이터의 별점을 0과 1로 바꿈
        rating_review_list[i].set_rating(new_rating) #모든 리뷰 데이터의 별점을 0과 1로 바꿈

    for i in rating_review_list:
        print(i.get_rating())

if __name__ == "__main__":
    execute()