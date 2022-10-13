#!/usr/bin/python

"""
Utility module that repairs the json step by step
"""
import re
import demjson

class JsonParser:
    """
    transform broken into valid json file
    """
    def __init__(self, in_path, out_path):
        "init"
        self.in_path = in_path
        self.out_path = out_path

    def repair(self):
        "read broken data.json and write valid pizzas.json"
        with open(self.in_path, 'r') as data:
            valid_json = self.repair_json(data.read())

        with open(self.out_path, 'w+') as pizzas:
            pizzas.write(str(valid_json))

    # todo: something like a builder pattern
    def repair_json(self, data):
        "repair broken json step by step"
        tmp_1 = self.fix_missing_object_start(data)
        tmp_2 = self.fix_incredient_array(tmp_1)
        tmp_3 = self.fix_missing_comma(tmp_2)
        tmp_4 = self.fix_unquoted_keys(tmp_3)
        tmp_5 = self.fix_single_quotes(tmp_4)
        return tmp_5

    def fix_missing_object_start(self, data):
        "add curly braces to start and end of json"
        return '{' + data + '}'

    def fix_incredient_array(self, data):
        "strip curly braces from incredients"
        tmp = re.sub('(incredients:'+r'\s*'+r'\['+')({)(.*)(})('+r'\]'+',*)', r'\1'r'\3'r'\5', data)
        return tmp

    def fix_missing_comma(self, data):
        "add missing comma"
        tmp = re.sub('Extras', ',Extras', data)
        return tmp

    def fix_unquoted_keys(self, data):
        "add quotes to unqouted object keys"
        return demjson.decode(data)

    def fix_single_quotes(self, data):
        "replace single with double quotes"
        tmp = re.sub(r'\'', '"', str(data))
        return tmp

if __name__ == '__main__':
    JsonParser('../data/json/data.json', '../data/json/pizzas.json').repair()
