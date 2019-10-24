from jsonParser import SyntaxException
from jsonParser.JSONParser import JSONParser
from yamlConverter.YAMLConverter import YAMLConverter


def check_root_braces(string):
    if string[0] == '{' and string[len(string) - 1] == '}':
        return True

    return False


def remove_root_braces(string):
    return string[1: len(string) - 1]


if __name__ == "__main__":
    text = open("schedules\\example.json", encoding='UTF-8').read()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    if not check_root_braces(text):
        raise SyntaxException("__main__: синтаксическая ошибка")

    text = remove_root_braces(text)

    entity_set = JSONParser.parse(text)
    result = YAMLConverter.convert(entity_set)

    open("output\\example.yaml", mode='w', encoding='UTF-8').write(result)

