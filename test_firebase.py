import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2 

img = cv2.imread('arrow.png')

cred = credentials.Certificate("potato_firebase_sdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://potato-diseases-default-rtdb.firebaseio.com'
})

ref = db.reference('/')
ref.set({
    'Data':
    {
        'Image': img
    }
})


'''
ref = db.reference('Employee')
emp_ref = ref.child('emp1')
emp_ref.update({
    'name':"Hello"
})
'''

'''
ref = db.reference('Employee')
ref.update({
    'emp1/name': 'hello 1',
    'emp2/name': 'hello 2'
})
'''
'''
ref = db.reference('Employee2')
emp_ref = ref.push({
    'name': 'Bob',
    'email': 'adadadsd'
})
'''

# ref = db.reference('Employee')
# print(ref.get())