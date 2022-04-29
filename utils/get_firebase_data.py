import os 
import pyrebase
from PIL import Image 

class firebase_receiver:
    def __init__(self, storage=None, database=None):
        self.storage = storage
        self.database = database

        self.storage_child = 'leaf.png'
        self.storage_download = 'leaf.png'

        self.data_child = 'Data'
        self.update_2_child = 'Image'

        self.image = 0

    def getData(self):
        if self.storage != None:
            self.storage.child(self.storage_child).download(self.storage_download)
            self.image = Image.open(self.storage_download)
        if self.database != None:
            self.database.child(self.data_child).update({self.update_2_child: 'received'})
        return self.image
