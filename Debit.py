# se crea la clase
class Debit:
    id = int
    holder_name = str
    card_number = str
    expiration_date = str
    security_code = str
    signature = str
# se define el constructor


def __init__(self, card_number, expiration_date):
    self.card_number = card_number
    self.expiration_date = expiration_date
