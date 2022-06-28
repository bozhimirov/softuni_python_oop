from project.beverage.beverage import Beverage
# from encapsulation.restaurant.project.beverage.beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)
