class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, mililiters):
        if self.status() >= mililiters:
            self.quantity += mililiters
