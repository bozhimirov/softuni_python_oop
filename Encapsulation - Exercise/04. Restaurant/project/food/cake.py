from project.food.dessert import Dessert
# from encapsulation.restaurant.project.food.dessert import Dessert


class Cake(Dessert):
    PRICE = 5
    CALORIES = 1000
    GRAMS = 250

    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)
