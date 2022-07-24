from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    race_type_list = []

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type == "Appaloosa":
            for horse in self.horses:
                if horse.name == horse_name:
                    raise Exception(f"Horse {horse_name} has been already added!")
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        if horse_type == "Thoroughbred":
            for horse in self.horses:
                if horse.name == horse_name:
                    raise Exception(f"Horse {horse_name} has been already added!")
            horse1 = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse1)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockeys in self.jockeys:
            if jockeys.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for races in self.horse_races:
            if race_type == races.race_type:
                raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        c_jockey = self.find_jockey_by_name(jockey_name)
        c_horse = None
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    c_horse = horse

        if not c_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if c_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        if not c_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        c_jockey.horse = c_horse
        c_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {c_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        c_jockey = self.find_jockey_by_name(jockey_name)
        c_race = self.find_race(race_type)
        if not c_race:
            raise Exception(f"Race {race_type} could not be found!")
        if not c_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if c_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if c_jockey in c_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        c_race.jockeys.append(c_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.find_race(race_type):
            raise Exception(f"Race {race_type} could not be found!")
        if len(self.find_race(race_type).jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = {}
        for jockey in self.find_race(race_type).jockeys:
            winner[jockey.name] = jockey.horse.speed
        jockey_name_best = max(winner, key=winner.get)
        jockey = self.find_jockey_by_name(jockey_name_best)

        return f"The winner of the {race_type} race, with a speed of {jockey.horse.speed}km/h is {jockey.name}! Winner's horse: {jockey.horse.name}."

    def find_jockey_by_name(self, jockey_name):
        for jockeys in self.jockeys:
            if jockeys.name == jockey_name:
                return jockeys

    def find_horse_by_type(self, horse_type):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                return horse

    def find_race(self, race_type):
        for race in self.horse_races:
            if race_type == race.race_type:
                return race


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.horses[0].__class__.__name__)
print(horseRaceApp.horses[1].__class__.__name__)
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))
