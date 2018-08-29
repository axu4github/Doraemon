# coding=utf-8

import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    from doraemon import Doraemon

    fpath = sys.argv[1]
    contents = Doraemon.get_file_contents(
        fpath, in_charset="gbk", out_charset="utf-8")
    Doraemon.put_file_contents(
        "utf_8_{0}".format(os.path.basename(fpath)), contents)
