from jsonParser.Entity import Entity


class Array(Entity):
    def __init__(self,
                 name,
                 entity_set):
        super().__init__("array", self)
        self.name = name
        self.entity_set = entity_set

    def print(self):
        string = self.name + ": [\n"
        for entity in self.entity_set:
            try:
                string += entity.print() + ",\n"
            except AttributeError:
                string += entity + ",\n"

        string = string[0: len(string) - 2]
        string += "\n]"

        return string
