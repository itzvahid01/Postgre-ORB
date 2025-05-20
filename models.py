from lib.fields import *
from lib.model import *
class UserTable(BaseModel):
    name = CharField()
    family = CharField()
    price = IntegerField()
class AdminTable(BaseModel):
    name = CharField()
    family = CharField()