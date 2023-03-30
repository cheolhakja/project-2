import unittest
import preprocessor
import iterate_create_path

class TestCase(unittest.TestCase):

    def test_return_review_rating_list_using_parameter_works(self):
        expected_num = 12
        result_list = iterate_create_path.return_review_rating_list_using_parameter("C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\testing\\", R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\testing")
        self.assertEqual(len(result_list), expected_num)



