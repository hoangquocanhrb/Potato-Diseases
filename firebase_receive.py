# from google.cloud import storage
# from firebase import firebase
# import os# You just get your CREDENTIALS on previous step
# import cv2 

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="potato_firebase_sdk.json"  

# db_url = 'https://potato-diseases-default-rtdb.firebaseio.com'
# firebase = firebase.FirebaseApplication(db_url,None)
# client = storage.Client()
# bucket = client.get_bucket('potato-diseases.appspot.com')

# img = cv2.imread('arrow.png')
# print(img.shape)
# img = cv2.resize(img, (224,224))
# cv2.imwrite('resized_img.png', img)

# # imageBlob = bucket.blob("/")
# imagePath = '' # Replace with your own path
# imageBlob = bucket.blob('resized.png')
# imageBlob.upload_from_filename('resized_img.png') # Upload your image

import pyrebase
import os


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

storage.child('arrow.png').download('aa.png')
# all_files = storage.list_files()

# for file in all_files:
#     print(file.name)
#     file.download_to_filename(file.name)