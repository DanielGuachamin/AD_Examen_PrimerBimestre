pip install tweepy
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
###API Personales########################
ckey = ""
csecret = ""
atoken = ""
asecret = ""
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            #print ("SAVED" + str(doc) +"=>" + str(data))
            print("Se guardo con éxito")
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://daniel:dani16rya@127.0.0.1:5984')  #('http://115.146.93.184:5984/')
try:
    db = server.create('olimpicos')
except:
    db = server['olimpicos']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['juegos olimpicos'])