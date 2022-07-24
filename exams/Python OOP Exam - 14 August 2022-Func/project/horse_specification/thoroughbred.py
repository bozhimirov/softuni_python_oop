from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        value = self.speed + 3
        if value > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = value


