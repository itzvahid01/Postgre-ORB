import models
import inspect
from main import manager
from lib import fields,model,orb

items = []
ignores = [name for name,obj in inspect.getmembers(fields)]
ignores+= [name for name,obj in inspect.getmembers(model)]
ignores+= ['ModelMeta']
for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj) or inspect.isfunction(obj):
        if name not in ignores:
            items.append([name,obj])
for item in items:
    try :
        manager.deleteTable(item[0])
        manager.createTable(item[1])
    except Exception as e :
        print(f'Error In Migrations !{e}')