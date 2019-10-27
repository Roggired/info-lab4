from jsonParser.Entity import Entity, EntityType


class Object(Entity):
    def __init__(self,
                 name,
                 key_value_pair_set):
        super().__init__(EntityType.OBJECT, self)
        self.name = name
        self.key_value_pair_set = key_value_pair_set
