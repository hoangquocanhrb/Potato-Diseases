import argparse

import pyrebase
import os
import cv2 
import numpy as np 
import random

def cut_img(img2):
    mask =	np.zeros(img2.shape[:2],np.uint8) 
    bgdModel =  np.zeros((1,65),np.float64)
    fgdModel =  np.zeros((1,65),np.float64)
    rect =	(10,10,200,200)
    cv2.grabCut(img2,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT) 
    mask2  =  np.where((mask==2)|(mask==0),0,1).astype('float32')
    img2  =	img2*mask2[:,:,np.newaxis]
    
    back_ground = cv2.imread('Test_img/back_ground.JPG')
    back_ground = back_ground - back_ground*mask2[:,:,np.newaxis]

    img2 = img2 + back_ground/1.1
    return img2

parser = argparse.ArgumentParser()
parser.add_argument('--img_path', type=str, nargs='?', default='early/1.JPG')
config = {
  'apiKey': "AIzaSyApriNxJBruBDUVc5ge3y4bX3jZCR-ZThU",
  'authDomain': "potato-diseases.firebaseapp.com",
  'databaseURL': "https://potato-diseases-default-rtdb.firebaseio.com",
  'projectId': "potato-diseases",
  'storageBucket': "potato-diseases.appspot.com",
  'messagingSenderId': "580742106890",
  'appId': "1:580742106890:web:ed3e7805edb99b8a5234f3",
  'measurementId': "G-1TSSJ3FM5V",
  "serviceAccount": "potato_firebase_sdk.json"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()
database = firebase_storage.database()

# back = cv2.imread('back_ground.JPG')
# back = cv2.resize(back, (224,224))
# cv2.imwrite('back_ground.JPG', back)

img_path = 'Test_img/' + parser.parse_args().img_path
origin_path = 'Test_img/origin_leaf.JPG'
img = cv2.imread(img_path)
img = cv2.resize(img, (224,224))
origin = img.copy()

img = cut_img(img)

cv2.imwrite('Test_img/leaf.JPG', img)
cv2.imwrite(origin_path, origin)

storage.child("leaf.JPG").put('Test_img/leaf.JPG')
storage.child("origin_leaf.JPG").put(origin_path)

database.child('Data').update({'Image': 'sent'})
