import re
from jsonParser.SyntaxException import SyntaxException
from jsonParser.KeyValuePair import KeyValuePair


class KeyValuePairCreator:
    KEY_RE = '\s*"\w+"'
    VALUE_RE = '\s*"?[\w().-]+"?'
    SYNTAX_EXCEPTION_MESSAGE = "key_value_pair_creator: синтаксическая ошибка"

    @staticmethod
    def create_key_value_pair(string):
        string = str(string)

        if not KeyValuePairCreator.is_valid_key_value_pair(string):
            raise SyntaxException(KeyValuePairCreator.SYNTAX_EXCEPTION_MESSAGE)

        string_set = string.split(":")

        return KeyValuePair(string_set[0], string_set[1])

    @staticmethod
    def is_valid_key_value_pair(string):
        value = re.fullmatch(KeyValuePairCreator.KEY_RE + ':' + KeyValuePairCreator.VALUE_RE, string)

        if value:
            return True

        return False
