# coding=utf-8

from doraemon import Doraemon
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


class TestDoraemon(unittest.TestCase):
    """ Doraemon 单元测试 """

    def setUp(self):
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.resources = os.path.join(self.root, "resources")

    def test_get_file_contents(self):
        fpath = os.path.join(self.resources, "test_get_file_contents.txt")
        self.assertEqual(14, len(Doraemon.get_file_contents(fpath)))

    def test_get_none_contents_file_contents(self):
        fpath = os.path.join(self.resources, "none_contents_file.txt")
        self.assertEqual(0, len(Doraemon.get_file_contents(fpath)))

    def test_get_files(self):
        files = Doraemon.get_files(self.resources)
        self.assertTrue(
            os.path.join(self.resources, "d", "e", "2.txt") in files)

    def test_get_file_filter(self):
        self.assertEqual(
            0, len(Doraemon.get_files(
                self.resources,
                file_filter=lambda fpath: "foobar" == fpath.split(".")[-1])))

    def test_get_files_by_suffix(self):
        self.assertEqual(
            0, len(Doraemon.get_files_by_suffix(self.resources, "foobar")))

    def test_get_files_by_suffix_lower(self):
        self.assertTrue(
            len(Doraemon.get_files_by_suffix(self.resources, "TXT")) > 0)


if __name__ == "__main__":
    unittest.main()
