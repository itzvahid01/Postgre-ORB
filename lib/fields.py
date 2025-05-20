from abc import ABC,abstractmethod
class Field(ABC):
    def __init__(self,unique=False):
        self.name = None
        self.unique = unique
    def __set_name__(self, owner, name):
        if self.name is None:
            self.name = name
    @property
    @classmethod
    def sql_definition(cls):
        raise NotImplementedError("باید در زیرکلاس پیاده‌سازی شود")
    @property
    @abstractmethod
    def query(self):
        pass
class CharField(Field):
    def __init__(self,limit=255,fix=False):
        super().__init__()
        self.limit = limit
        self.fix = fix  
        self.field_type = 'VARCHAR' if fix else 'CHAR'
    @property
    def query(self):
        query = f'{self.name}{self.field_type}({self.limit})' if not self.fix else f'{self.name} {self.field_type}'
        if self.unique :
            query+=' UNIQUE'
        return query
    @property
    def sql_definition(self):
        return f"{self.name} VARCHAR({self.limit})"
class IntegerField(Field):
    def __init__(self,field_type='INT'):
        super().__init__()
    @property
    def query(self):
        query = f'{self.name} {self.field_type}' if not self.fix else f'{self.name} {self.field_type}'
        if self.unique :
            query+=' UNIQUE'
        return query
    @property
    def sql_definition(self):
        return f"{self.name} INT"