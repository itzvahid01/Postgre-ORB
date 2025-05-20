from abc import ABC,abstractmethod
from .fields import Field
class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._fields = fields  # ✅ ذخیره با نام _fields
        return new_class


class BaseModel(metaclass=ModelMeta):
    @classmethod
    def sql(cls):
        table_name = cls.__name__.lower()
        columns = [field.sql_definition for field in cls._fields.values()]  # ✅ استفاده از _fields
        columns_sql = ",\n    ".join(columns)
        return f"CREATE TABLE {table_name} (\n    {columns_sql}\n);"