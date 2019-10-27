from jsonParser.SyntaxException import SyntaxException
from jsonParser.JSONParser import JSONParser
from yamlConverter.YAMLConverter import YAMLConverter

import json
import yaml
from time import time


def check_root_braces(string):
    if string[0] == '{' and string[len(string) - 1] == '}':
        return True

    return False


def remove_root_braces(string):
    return string[1: len(string) - 1]


def use_own_parser_and_converter(text):
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    if not check_root_braces(text):
        raise SyntaxException("__main__: синтаксическая ошибка")

    text = remove_root_braces(text)

    json_parser = JSONParser(text)
    entity_set = json_parser.parse()

    yaml_converter = YAMLConverter(entity_set)
    return yaml_converter.convert()


def use_libs(text, output_file):
    jsons_data = json.loads(text)
    yaml.dump(jsons_data, output_file, encoding='UTF-8', allow_unicode=True)


if __name__ == "__main__":
    mode = input()

    start_time = time()
    for counter in range(10):
        input_file = open("schedules\\example.json", encoding='UTF-8')
        text = input_file.read()
        input_file.close()

        output_file = open("output\\example.yaml", mode='w', encoding='UTF-8')

        if mode == '0':
            use_libs(text, output_file)

        if mode == '1':
            output_file.write(use_own_parser_and_converter(text))

        output_file.close()

    end_time = time()

    delta_time = end_time - start_time
    print("Время выполнения: " + str(delta_time))