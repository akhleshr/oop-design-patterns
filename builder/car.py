class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def __str__(self):
        return f'Car: {self.make} {self.model}, {self.year}, {self.color}'
