pip install pymongo
pip install pandas
#Aqui se hace la conexion de forma local a mongodb
from pymongo import MongoClient
CLIENT = MongoClient('mongodb://localhost:27017/')
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
    import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
import json
from bson.raw_bson import RawBSONDocument

    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))
response = requests.get('https://olympics.com/tokyo-2020/es/deportes/')
soup = BeautifulSoup(response.content, "lxml")

Titulo=[]
Noticia=[]

post_titulo=soup.find_all("h2", class_="tk-disciplines__title")


for element in post_titulo:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Titulo.append(limpio.strip())

        
def listado():
    i=0
    for n in range(len(Titulo)):
        Noticia.append("Noticia " + str(i+1))
        i=i+1
listado()
#Aqui se pasa el diccionario obtenido a DataFrame y se guarda como json
Doc=pd.DataFrame({'titulo':Titulo}, index=Noticia)
Doc
Doc.to_json('juegosolimpicos.json')
#Mediante la conexion se establece el nombre de la BD y la colección
db = CLIENT["olimpicos"]
Collection = db["noticias"] 

#Obtiene el documento json generado anteriormente y lo carga en una variable
with open('juegosolimpicos.json') as file: 
    file_data = json.load(file) 
      
#Finalmente carga el json en mongo        
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 
print("Se ha guardado exitosamente")