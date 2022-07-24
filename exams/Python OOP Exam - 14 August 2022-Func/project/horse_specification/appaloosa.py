from project.horse_specification.horse import  Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        value = self.speed + 2
        if value > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = value



