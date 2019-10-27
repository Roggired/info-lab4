from jsonParser.Entity import Entity, EntityType


class Array(Entity):
    def __init__(self,
                 name,
                 entity_set):
        super().__init__(EntityType.ARRAY, self)
        self.name = name
        self.entity_set = entity_set
