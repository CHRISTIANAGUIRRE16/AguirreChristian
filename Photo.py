# se crea la clase
class Photo:
    id = int
    size = float
    format = str
    location = str
    author = str
    note = str
    adress = str
    photo = str
# se define el constructor
def __init__(self, size,format):
    self.size = size
    self.format = format
    