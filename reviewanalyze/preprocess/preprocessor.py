import iterate_create_path
import rating_converter

def execute():
    rating_review_list = iterate_create_path.return_rating_review_list() #JSON파일을 리스트로 불러옴
    print(type(rating_review_list))
    for i in rating_review_list:
        print(rating_converter.convert(i.get_rating()))

if __name__ == "__main__":
    execute()