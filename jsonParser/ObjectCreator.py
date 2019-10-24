import re

from jsonParser.KeyValuePairCreator import KeyValuePairCreator
from jsonParser.Object import Object
from jsonParser.SyntaxException import SyntaxException


class ObjectCreator:
    @staticmethod
    def create_object(string):
        string = str(string)

        if not ObjectCreator.is_valid_object(string):
            raise SyntaxException("create_object: синтаксическая ошибка")

        name = ObjectCreator.create_name(string)

        key_value_pair_string_set = ObjectCreator.create_key_value_pair_string_set(string)
        key_value_pair_set = ObjectCreator.create_key_value_pair_set(key_value_pair_string_set)

        return Object(name, key_value_pair_set)

    @staticmethod
    def is_valid_object(string):
        value = re.fullmatch('\s*"\w+":\s*{[\s\S]*', string)

        if value and string[len(string) - 1] == '}':
            return True

        return False

    @staticmethod
    def create_name(string):
        double_dot_index = string.index(":")

        return string[0: double_dot_index]

    @staticmethod
    def create_key_value_pair_string_set(string):
        first_brace = string.index("{")

        entity = string[first_brace + 1: len(string) - 1]

        return entity.split(",")

    @staticmethod
    def create_key_value_pair_set(key_value_pair_string_set):
        key_value_pair_set = []

        for row in key_value_pair_string_set:
            key_value_pair_set.append(KeyValuePairCreator.create_key_value_pair(row))

        return key_value_pair_set
