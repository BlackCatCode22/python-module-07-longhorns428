from datetime import date
from utils import gen_birth_date, gen_unique_id

class Lion:
    sound = "roar"
    species = "Lion"

    def __init__(self, name, age, sex, season, color, weight, origin, count):
        self.id = gen_unique_id("Lion", count)
        self.name = name
        self.birth_date = gen_birth_date(season, age)
        self.sex = sex
        self.color = color
        self.weight = weight
        self.origin = origin
        self.arrived = str(date.today())

    def __str__(self):
        return (f"{self.id}; {self.name}; birth date: {self.birth_date}; "
            f"{self.color} color; {self.sex}; {self.weight} pounds; "
            f"from {self.origin}; arrived {self.arrived}")