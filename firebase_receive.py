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
