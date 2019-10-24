from jsonParser.ParsingTask import ParsingTask


class ParsingQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self,
                 task: ParsingTask):
        self.tasks.append(task)

    def execute(self):
        entity_set = []
        for task in self.tasks:
            entity_set.append(task.execute())

        return entity_set
