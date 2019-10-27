from jsonParser.Entity import EntityType


class YAMLConverter:
    def __init__(self, entity_set):
        self.entity_set = entity_set
        self.result = ""

    def convert(self):
        for entity in self.entity_set:
            self.if_object(entity)
            self.if_array(entity)
            self.if_key_value_pair(entity)

        return self.result

    def if_object(self, entity):
        if entity.type == EntityType.OBJECT:
            self.result += self.remove_quotes(entity.name) + ":\n"

            for key_value_pair in entity.key_value_pair_set:
                self.result += "    " + self.remove_quotes(key_value_pair.key) + ": " + key_value_pair.value + "\n"

    def if_array(self, entity):
        if entity.type == EntityType.ARRAY:
            self.result += self.remove_quotes(entity.name) + ": \n"

            for array_entity in entity.entity_set:
                self.result += "  - " + self.remove_quotes(array_entity.name) + "\n"

    def if_key_value_pair(self, entity):
        if entity.type == EntityType.KEY_VALUE_PAIR:
            self.result += self.remove_quotes(entity.key) + ": " + entity.value + "\n"

    @staticmethod
    def remove_quotes(string):
        return string[1:len(string) - 1]
