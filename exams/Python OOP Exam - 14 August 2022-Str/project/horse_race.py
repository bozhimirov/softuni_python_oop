class HorseRace:
    valid_types = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_types

    @race_type.setter
    def race_type(self, value):
        if value not in self.valid_types:
            raise ValueError("Race type does not exist!")
        self.__race_types = value
