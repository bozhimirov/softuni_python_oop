from project.supply.supply import Supply
# from supply.supply import Supply


class Food(Supply):
    ENERGY = 25

    def __init__(self, name, energy=ENERGY):
        super().__init__(name, energy)

    def details(self):
        return f'{self.__class__.__name__}: {self.name}, {self.ENERGY}'
