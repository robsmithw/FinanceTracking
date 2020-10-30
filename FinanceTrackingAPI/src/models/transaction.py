from json import JSONEncoder
from datetime import date, datetime

class Transaction:

    def __init__(self, description, amount, dateArg):
        self.description = description
        self.amount = amount
        self.date = dateArg

class TransactionEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return o.__dict__
