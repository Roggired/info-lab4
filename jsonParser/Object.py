from jsonParser.Entity import Entity


class Object(Entity):
    def __init__(self,
                 name,
                 key_value_pair_set):
        super().__init__("object", self)
        self.name = name
        self.key_value_pair_set = key_value_pair_set

    def print(self):
        string = self.name + ": {\n"

        for key_value_pair in self.key_value_pair_set:
            string += key_value_pair.print() + ",\n"

        string = string[0:len(string) - 2]
        string += "\n}"
        return string

