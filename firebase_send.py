import argparse

import pyrebase
import os
import cv2 

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

img_path = 'Test_img/' + parser.parse_args().img_path
img = cv2.imread(img_path)
img = cv2.resize(img, (224,224))
cv2.imwrite(img_path, img)

storage.child("leaf.png").put(img_path)

database.child('Data').update({'Image': 'sent'})