import psycopg2
from .settings import connection_settings as sett
from .fields import *
from models import *
class Connection:
    def start(self):
        try:
            self.conn = psycopg2.connect(
                host= sett['host'] ,
                database=sett['database'],
                user=sett['user'],
                password=sett['password'],
                port=sett['port']
            )
            return self.conn

        except Exception :
            raise TimeoutError(f'Connection Error !')
    def stop(self):
        self.conn.close()
class Manager:
    def __init__(self):
        self.conn = Connection()
        if (base:=self.conn.start()):
            self.cursor = base.cursor()
        else:
            raise SystemError('Cursor Creation Error !')
    @property
    def db(self) -> str :
        try :
            self.cursor.execute('SELECT current_database();')
            loc = self.cursor.fetchone()
        except:
            loc = False        
        return loc
    def __create(self,what,query):
        self.cursor.execute(f'CREATE {what} {query};')
    def createTable(self,Model):
        self.cursor.execute(f'{Model.sql()}')
        self.conn.conn.commit()
    def deleteTable(self,modelName):
        self.cursor.execute(f'DROP TABLE IF EXISTS {modelName};')
        self.conn.conn.commit()
    def finish(self):
        self.conn.stop
