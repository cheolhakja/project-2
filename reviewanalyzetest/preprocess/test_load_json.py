import unittest
import reviewanalyze.preprocess.load_json

path_prefix = "hello"
path_suffix = ["James", "Richman"]


class CreateFilePathTest(unittest.TestCase):
    def test_file_path_create_func(self):
        self.assertEquals(
            reviewanalyze.preprocess.load_json.return_path(path_prefix, path_suffix),
            (["helloJames", "helloRichman"], 2),
        )


if __name__ == "__main__":
    unittest.main()
