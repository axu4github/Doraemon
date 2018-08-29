# coding=utf-8


class XUtilities(object):
    """Python 工具集"""

    @staticmethod
    def get_file_contents(fpath):
        contents = []
        with open(fpath, "r") as f:
            contents = [content.strip() for content in f.readlines()]

        return contents
