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

    def test_path_splitext(self):
        self.assertEqual(".txt", os.path.splitext("/1/2/3/4/5.txt")[-1])


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

    def test_get_file_by_get_files(self):
        filepath = os.path.join(self.resources, "none_contents_file.txt")
        files = Doraemon.get_files(filepath)
        self.assertEqual(files, [filepath])

    def test_get_file_filter(self):
        self.assertEqual(
            0, len(Doraemon.get_files(
                self.resources,
                file_filter=lambda fpath: ".foobar" == fpath.split(".")[-1])))

    def test_get_files_by_suffix(self):
        self.assertEqual(
            0, len(Doraemon.get_files_by_suffix(self.resources, ".foobar")))

    def test_get_files_by_suffix_lower(self):
        self.assertTrue(
            len(Doraemon.get_files_by_suffix(self.resources, ".TXT")) > 0)

    def test_put_file_contents_str(self):
        s, fpath = "123", os.path.join(self.resources, "foo.bar")

        self.assertTrue(not os.path.isfile(fpath))
        self.assertTrue(Doraemon.put_file_contents(fpath, s))
        self.assertTrue(os.path.isfile(fpath))
        self.assertEqual(1, len(Doraemon.get_file_contents(fpath)))
        self.assertEqual(s, Doraemon.get_file_contents(fpath)[0])

        if os.path.isfile(fpath):
            os.remove(fpath)

        self.assertTrue(not os.path.isfile(fpath))

    def test_put_file_contents_list(self):
        _l, fpath = range(0, 10), os.path.join(self.resources, "foo.bar")

        self.assertTrue(not os.path.isfile(fpath))
        self.assertTrue(Doraemon.put_file_contents(fpath, _l))
        self.assertTrue(os.path.isfile(fpath))
        self.assertEqual(10, len(Doraemon.get_file_contents(fpath)))
        self.assertEqual(
            map(lambda num: str(num), _l),
            Doraemon.get_file_contents(fpath))

        if os.path.isfile(fpath):
            os.remove(fpath)

        self.assertTrue(not os.path.isfile(fpath))


if __name__ == "__main__":
    unittest.main()
