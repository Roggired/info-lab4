import re

from jsonParser.SyntaxException import SyntaxException
from jsonParser.Array import Array


class ArrayCreator:
    KEY_RE = '\s*"\w+"'
    ENTITY_RE = '\s*\[[\s\S]*'
    SYNTAX_EXCEPTION_MESSAGE = "create_array: синтаксическая ошибка"

    @staticmethod
    def create_array(string):
        string = str(string)

        if not ArrayCreator.is_valid_array(string):
            raise SyntaxException(ArrayCreator.SYNTAX_EXCEPTION_MESSAGE)

        name = ArrayCreator.create_name(string)

        entity_string_set = ArrayCreator.create_entity_string_set(string)
        entity_set = ArrayCreator.create_entity_set(entity_string_set)

        return Array(name, entity_set)

    @staticmethod
    def is_valid_array(string):
        value = re.fullmatch(ArrayCreator.KEY_RE + ':' + ArrayCreator.ENTITY_RE, string)

        if value and string[len(string) - 1] == ']':
            return True

        return False

    @staticmethod
    def create_name(string):
        double_dot_index = string.index(":")

        return string[0: double_dot_index]

    @staticmethod
    def create_entity_string_set(string):
        first_brace = string.index("[")

        entity = string[first_brace + 1: len(string) - 1]

        return entity.split(",")

    @staticmethod
    def create_entity_set(entity_string_set):
        entity_set = []

        for row in entity_string_set:
            entity_set.append(row)

        return entity_set
