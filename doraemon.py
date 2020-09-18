# coding=utf-8

import os
import pandas as pd
import xml.etree.ElementTree as ET
import xmltodict


class Doraemon(object):
    """Python 工具集"""

    @staticmethod
    def get_files_by_suffix(_dir, suffix=None):
        """ 获取指定后缀的文件 """
        file_filter = None
        if suffix is not None:
            def suffix_filter_fn(fpath):
                return suffix.lower() == os.path.splitext(fpath)[-1].lower()

            file_filter = suffix_filter_fn

        return Doraemon.get_files(_dir, file_filter=file_filter)

    @staticmethod
    def get_files(_dir, file_filter=None):
        """ 获取文件 """
        match_files = []
        if os.path.isfile(_dir):
            match_files.append(_dir)
        else:
            for root, dirs, files in os.walk(_dir):
                if file_filter is not None:
                    files = filter(file_filter, files)

                for fname in files:
                    match_files.append(os.path.join(root, fname))

        return match_files

    @staticmethod
    def get_file_contents(fpath, in_charset=None):
        """ 文件读到数组 """
        contents = []
        with open(fpath, "r") as f:
            for content in f.readlines():
                if in_charset is not None:
                    content = content.decode(in_charset)

                contents.append(content.strip())

        return contents

    @staticmethod
    def put_file_contents(fpath, contents):
        """ 数组写到文件 """
        with open(fpath, "w") as f:
            if isinstance(contents, list):
                for content in contents:
                    f.write("{0}{1}".format(content, os.linesep))
            else:
                f.write(contents)

        return True

    @staticmethod
    def get_excel_contents(fpath, *args, **kwargs):
        """ 获取Excel文件内容 """
        return pd.read_excel(fpath, *args, **kwargs)

    @staticmethod
    def put_excel_contents(fpath, contents, *args, **kwargs):
        """ 写入Excel文件内容 """
        return pd.DataFrame(contents).to_excel(fpath, *args, **kwargs)

    @staticmethod
    def get_xml_contents(fpath, in_charset='utf-8'):
        """ 获取XML文件内容 """
        xml_data = ET.parse(fpath).getroot()
        xml_str = ET.tostring(xml_data, encoding=in_charset, method='xml')
        data_dict = xmltodict.parse(xml_str)
        return data_dict

    @staticmethod
    def hit(parttern, _str):
        """
        根据单个规则验证是否命中

        :param parttern 命中规则
        :param _str 需要验证的内容
        """
        return re.search(parttern, _str)
