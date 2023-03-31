import preprocessor
import iterate_create_path
import json_to_csv

result_list = iterate_create_path.return_review_rating_list_using_parameter_2("C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\second-trial\\", R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\second-trial")
rating_list, review_list = preprocessor.preprocess_3(result_list)

print("review list : ", len(review_list))
print("rating list : ", len(rating_list))

json_to_csv.write_csv(rating_list, review_list) 

