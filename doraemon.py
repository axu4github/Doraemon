# coding=utf-8

import os


class Doraemon(object):
    """Python 工具集"""

    @staticmethod
    def get_files(_dir, file_filter=None):
        match_files = []
        for root, dirs, files in os.walk(_dir):
            if file_filter is not None:
                files = filter(file_filter, files)

            match_files = [os.path.join(root, fname) for fname in files]

        return match_files

    @staticmethod
    def get_file_contents(fpath):
        contents = []
        with open(fpath, "r") as f:
            contents = [content.strip() for content in f.readlines()]

        return contents
