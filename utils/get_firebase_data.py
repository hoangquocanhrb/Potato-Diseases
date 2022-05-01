import os 
import pyrebase
from PIL import Image 

class firebase_receiver:
    def __init__(self, storage=None, database=None):
        self.storage = storage
        self.database = database

        self.storage_child = 'leaf.JPG'
        self.storage_download = 'Test_img/leaf.JPG'

        self.origin_child = 'origin_leaf.JPG'
        self.origin_download = 'Test_img/origin_leaf.JPG'

        self.data_child = 'Data'
        self.update_2_child = 'Image'

        self.image = 0
        self.origin = 0
        
    #Get image from firebase and then send 'received' to confirm
    def getData(self):
        if self.storage != None:
            self.storage.child(self.storage_child).download(self.storage_download)
            self.image = Image.open(self.storage_download)

            self.storage.child(self.origin_child).download(self.origin_download)
            self.origin = Image.open(self.origin_download)
            
        if self.database != None:
            self.database.child(self.data_child).update({self.update_2_child: 'received'})
        return self.image, self.origin
