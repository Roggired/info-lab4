from jsonParser.Entity import Entity
from jsonParser.ObjectCreator import ObjectCreator
from jsonParser.KeyValuePairCreator import KeyValuePairCreator
from jsonParser.ArrayCreator import ArrayCreator


class ParsingTask:
    def __init__(self,
                 entity,
                 entity_type):
        self.entity = entity
        self.entity_type = entity_type

    def execute(self):
        if self.entity_type == "object":
            return ObjectCreator.create_object(self.entity)

        if self.entity_type == "array":
            return ArrayCreator.create_array(self.entity)

        return KeyValuePairCreator.create_key_value_pair(self.entity)
