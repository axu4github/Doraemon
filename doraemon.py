# coding=utf-8

import os


class Doraemon(object):
    """Python 工具集"""

    @staticmethod
    def get_files_by_suffix(_dir, suffix=None):
        file_filter = None
        if suffix is not None:
            file_filter = lambda fpath: suffix.lower() == os.path.splitext(fpath)[-1].lower()

        return Doraemon.get_files(_dir, file_filter=file_filter)

    @staticmethod
    def get_files(_dir, file_filter=None):
        match_files = []
        for root, dirs, files in os.walk(_dir):
            if file_filter is not None:
                files = filter(file_filter, files)

            for fname in files:
                match_files.append(os.path.join(root, fname))

        return match_files

    @staticmethod
    def get_file_contents(fpath):
        contents = []
        with open(fpath, "r") as f:
            contents = [content.strip() for content in f.readlines()]

        return contents
