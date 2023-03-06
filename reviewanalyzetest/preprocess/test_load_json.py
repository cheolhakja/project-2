import unittest
import reviewanalyze.preprocess.iterate_create_path

class TestLoadFile(unittest.TestCase):
    def test_load_file_func(self):
        list_test = reviewanalyze.preprocess.iterate_create_path.return_review_rating_list_using_parameter(
            "C:\\Users\\IBK\\Desktop\\나만의-우테코\\kakaomap-data-scrap\\reviewdata\\testing\\", R"C:\Users\IBK\Desktop\나만의-우테코\kakaomap-data-scrap\reviewdata\testing")
        self.assertEquals(
            len(list_test), 113
        )

if __name__ == "__main__":
    unittest.main()
