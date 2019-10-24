class YAMLConverter:
    @staticmethod
    def convert(entity_set):
        result = "!!map {\n"

        for entity in entity_set:
            if entity.type == "object":
                result += "  !!str " + entity.name + " : !!map {\n"

                for key_value_pair in entity.key_value_pair_set:
                    result += "    !!str " + key_value_pair.key + " : !!str " + key_value_pair.value + ",\n"

                result = result[0:len(result) - 2]
                result += "\n  },\n"

            if entity.type == "array":
                result += "  !!str " + entity.name + " : !!seq [\n"

                for array_entity in entity.entity_set:
                    result += "    !!str " + array_entity.name + ",\n"

                result = result[0:len(result) - 2]
                result += "\n  ],\n"

            if entity.type == "row":
                result += "  !!str " + entity.key + " : !!str " + entity.value + ",\n"

        result = result[0:len(result) - 2]
        result += "\n}"

        return result
