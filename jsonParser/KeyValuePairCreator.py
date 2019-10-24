import re
from jsonParser.SyntaxException import SyntaxException
from jsonParser.KeyValuePair import KeyValuePair


class KeyValuePairCreator:
    @staticmethod
    def create_key_value_pair(string):
        string = str(string)

        if string.index(":") < 0:
            raise SyntaxException("create_key_value_pair: синтаксическая ошибка")

        string_set = string.split(":")

        if len(string_set) > 2:
            raise SyntaxException("create_key_value_pair: синтаксическая ошибка")

        key = KeyValuePairCreator.create_key(string_set[0])
        value = KeyValuePairCreator.create_value(string_set[1])

        return KeyValuePair(key, value)

    @staticmethod
    def create_key(string):
        string = str(string)

        if not KeyValuePairCreator.is_valid_key(string):
            raise SyntaxException("create_key: синтаксическая ошибка.")

        return string

    @staticmethod
    def is_valid_key(string):
        value = re.fullmatch('\s*"\w+"', string)

        if value:
            return True

        return False

    @staticmethod
    def create_value(string):
        string = str(string)

        if KeyValuePairCreator.is_valid_value(string):
            return string

        raise SyntaxException("create_value: синтаксическая ошибка.")

    @staticmethod
    def is_valid_value(string):
        value = re.fullmatch('\s*"?[\w().-]+"?', string)
        if value:
            return True

        return False
