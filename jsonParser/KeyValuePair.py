from jsonParser.Entity import Entity, EntityType


class KeyValuePair(Entity):
    def __init__(self,
                 key,
                 value):
        super().__init__(EntityType.KEY_VALUE_PAIR, self)
        self.key = key
        self.value = value

