class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        return f'{self.name} is not happy'

    def water(self, quantity):
        self.is_happy = quantity >= self.water_requirements
