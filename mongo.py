from pymongo import MongoClient
from bson.json_util import dumps
from bson import BSON
from bson import json_util
import time
import regex
from pymongo import TEXT

def mongo_ext(str1):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.cloud
    t0=time.clock()
    print(str1)
    db.bookinventory.create_index([('Bookname',TEXT), ('Authorname',TEXT)],default_language='english')
    rowss=db.bookinventory.find( { '$text': { '$search': str1 } } )
    t1=time.clock()
    total=t1-t0
    print("mongo db Time:")
    print(total)
    ls=[]
    for row in rowss:
        ls.append(row)
        print(row)
    return dumps(ls)
