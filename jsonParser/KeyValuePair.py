from jsonParser.Entity import Entity


class KeyValuePair(Entity):
    def __init__(self,
                 key,
                 value):
        super().__init__("row", self)
        self.key = key
        self.value = value

    def print(self):
        return self.key + ": " + self.value

