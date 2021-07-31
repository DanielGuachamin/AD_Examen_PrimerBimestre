pip install pandas
pip install pysqlite3
import pandas as pd
import sqlite3 
con = sqlite3.connect("database.db")
doc=pd.read_json('juegosolimpicos_1627693060255.json')
doc
doc.to_sql('olimpicos', con)