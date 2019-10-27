from enum import Enum


class Entity:
    def __init__(self,
                 type,
                 value):
        self.type = type
        self.value = value


class EntityType(Enum):
    OBJECT = "object"
    ARRAY = "array"
    KEY_VALUE_PAIR = "row"
