pip install facebook-scraper
pip install pymongo
import time
import json
from facebook_scraper import get_posts
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
#Aqui se hace la conexion de forma local a mongodb
from pymongo import MongoClient
CLIENT = MongoClient('mongodb://localhost:27017/')
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
    i=1
for post in get_posts('Olympics', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db = CLIENT["olimpicosfacebook"]
        Collection = db["noticias"] 
        Collection.insert_one(doc) 
    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))