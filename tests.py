# coding=utf-8

from xutilities import XUtilities
import random
import unittest
import os


class TestPython(unittest.TestCase):

    def test_file_io_exception(self):
        try:
            with open(random.random(), "r") as f:
                f.readlines()
        except Exception as e:
            self.assertTrue("need string or buffer" in str(e))


class TestXUtilities(unittest.TestCase):
    """ XUtilities 单元测试 """

    def setUp(self):
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.resources = os.path.join(self.root, "resources")

    def test_get_file_contents(self):
        fpath = os.path.join(self.resources, "test_get_file_contents.txt")
        self.assertEqual(14, len(XUtilities.get_file_contents(fpath)))

    def test_get_none_contents_file_contents(self):
        fpath = os.path.join(self.resources, "none_contents_file.txt")
        self.assertEqual(0, len(XUtilities.get_file_contents(fpath)))


if __name__ == "__main__":
    unittest.main()
