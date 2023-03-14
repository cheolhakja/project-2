import reviewanalyze.preprocess.iterate_create_path
import reviewanalyze.preprocess.preprocessor
def execute():
    rating_review_list =  reviewanalyze.preprocess.iterate_create_path.return_review_rating_list_using_parameter(
            "C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\testing\\", R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\testing")
        
    rating, review = reviewanalyze.preprocess.preprocessor.preprocess(rating_review_list)
    print(rating," : ", review)
    

if __name__ == "__main__":
    
    execute()
