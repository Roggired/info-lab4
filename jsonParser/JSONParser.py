from jsonParser.SyntaxException import SyntaxException
from jsonParser.ParsingQueue import ParsingQueue
from jsonParser.ParsingTask import ParsingTask


class JSONParser:

    @staticmethod
    def parse(string):
        parsing_queue = ParsingQueue()
        buffer = ""
        in_object_flag = False
        in_array_flag = False
        for index in range(len(string)):
            if string[index] == '[' and not in_object_flag:
                buffer += string[index]
                in_array_flag = True
                continue

            if string[index] == ']' and not in_object_flag:
                if not in_array_flag:
                    raise SyntaxException("parse: непарная квадратная скобка")

                buffer += string[index]
                task = ParsingTask(buffer, "array")
                buffer = ""
                parsing_queue.add_task(task)
                in_array_flag = False
                continue

            if string[index] == '{' and not in_array_flag:
                buffer += string[index]
                in_object_flag = True
                continue

            if string[index] == '}' and not in_array_flag:
                if not in_object_flag:
                    raise SyntaxException("parse: непарная скобка")

                buffer += string[index]
                task = ParsingTask(buffer, "object")
                buffer = ""
                parsing_queue.add_task(task)
                in_object_flag = False
                continue

            if string[index] == ',' and not in_object_flag and not in_array_flag:
                if buffer != "":
                    task = ParsingTask(buffer, "row")
                    buffer = ""
                    parsing_queue.add_task(task)

                continue

            if index == len(string) - 1:
                task = ParsingTask(buffer, "row")
                buffer = ""
                parsing_queue.add_task(task)

            buffer += string[index]

        return parsing_queue.execute()
