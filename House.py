# se crea la clase
class House:
    id = int
    location = str
    price = float
    m2_construction = float
    m2_land = float
# se define el constructor


def __init__(self, m2_contruction, m2_land):
    self.m2_contruction = m2_contruction
    self.m2_land = m2_land
