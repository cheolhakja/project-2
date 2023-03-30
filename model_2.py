import preprocessor
import iterate_create_path

if __name__ == "__main":

    result_list = iterate_create_path.return_review_rating_list_using_parameter("C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\testing\\", R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\testing")
    rating_list, review_list = preprocessor.preprocess(result_list)
