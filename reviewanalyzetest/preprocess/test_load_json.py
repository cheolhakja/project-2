import unittest

path_prefix = "hello"
path_suffix = ["James", "Richman"]


def return_path(path_prefix, path_list_suffix):
    path_list = []
    for i in path_list_suffix:
        path = path_prefix + i
        path_list.append(path)

    return len(path_list), path_list


class CreateFilePathTest(unittest.TestCase):
    def test_file_path_creation(self):
        self.assertEquals(
            return_path(path_prefix, path_suffix), (2, ["helloJames", "helloRichman"])
        )


if __name__ == "__main__":
    unittest.main()
