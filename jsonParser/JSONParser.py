from jsonParser.Entity import EntityType
from jsonParser.SyntaxException import SyntaxException
from jsonParser.ParsingQueue import ParsingQueue
from jsonParser.ParsingTask import ParsingTask


class JSONParser:
    EXTRA_PARENTHESIS_EXCEPTION = "parse: непарная квадратная скобка"
    EXTRA_BRACE_EXCEPTION = "parse: непарная фигурная скобка"

    def __init__(self,
                 string):
        self.parsing_queue = ParsingQueue();
        self.buffer = ""
        self.in_object_flag = False
        self.in_array_flag = False
        self.string = string

    def parse(self):
        for index in range(len(self.string)):
            symbol = self.string[index]
            self.buffer += symbol

            self.if_left_parenthesis(symbol)
            self.if_right_parenthesis(symbol)
            self.if_left_brace(symbol)
            self.if_right_brace(symbol)

            if not self.in_object_flag and not self.in_array_flag:
                self.if_comma(symbol)

            self.if_end_of_string(index)

        return self.parsing_queue.execute()

    def if_left_parenthesis(self, symbol):
        if symbol == '[':
            self.in_array_flag = True

    def if_right_parenthesis(self, symbol):
        if symbol == ']':
            if not self.in_array_flag:
                raise SyntaxException(self.EXTRA_PARENTHESIS_EXCEPTION)

            self.create_task(EntityType.ARRAY)

            self.in_array_flag = False

    def if_left_brace(self, symbol):
        if symbol == '{':
            self.in_object_flag = True

    def if_right_brace(self, symbol):
        if symbol == '}':
            if not self.in_object_flag:
                raise SyntaxException(self.EXTRA_BRACE_EXCEPTION)

            self.create_task(EntityType.OBJECT)

            self.in_object_flag = False

    def if_comma(self, symbol):
        if symbol == ',':
            self.delete_last_symbol_from_buffer()
            if not self.buffer_is_empty():
                self.create_task(EntityType.KEY_VALUE_PAIR)

    def if_end_of_string(self, index):
        if index == len(self.string) - 1 and not self.buffer_is_empty():
            self.create_task("row")

    def create_task(self,
                    task_type):
        task = ParsingTask(self.buffer, task_type)
        self.parsing_queue.add_task(task)
        self.buffer = ""

    def delete_last_symbol_from_buffer(self):
        self.buffer = self.buffer[0:len(self.buffer) - 1]

    def buffer_is_empty(self):
        if self.buffer == "":
            return True

        return False
