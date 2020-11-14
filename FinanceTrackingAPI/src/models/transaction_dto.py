from json import JSONEncoder
from datetime import date, datetime

class TransactionDto:

    def __init__(self, description, amount, dateArg):
        self.description = description
        self.amount = amount
        self.date = dateArg

class TransactionDtoEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return o.__dict__
