import pymongo
from pymongo import MongoClient
import queue
#import threading
import json

class DBClass:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.db
        self.collection = self.db.collection
            
    def findPerson(self, person):
        count = self.collection.find_one(person)
        try:
            name = count['username'];
            return True
        except:
            return False

    def addUser(self, person):#, out_queue):
        if self.findPerson(person):
            return "That user already exists"
        else:
            self.collection.insert_one(person)
            return "Sucessfully added {}".format(person['username'])
            
    
    def deleteUser(self, person):
        count = self.collection.find_one_and_delete(book)
        try:
            return ("Successfully deleted {}".format(count['username']) )
        except:
            return ("ERROR: User doesn't exist.")
     
            
    def delete(self):
        self.collection.delete_many({})






