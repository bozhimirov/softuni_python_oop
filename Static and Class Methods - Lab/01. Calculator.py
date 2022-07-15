from functools import reduce

class Calculator:
    @staticmethod
    def add(*args):
    #     amount = 0
    #     for num in args:
    #         amount += num
    #     return sum(*args)
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

