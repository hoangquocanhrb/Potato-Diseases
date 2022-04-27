import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel
from Potato import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QTimer
import os 
import time 
import cv2 
import pyrebase 
from PIL import Image
import numpy as np 
import argparse

import torch 
import torch.nn as nn 
from torchvision import transforms
from network import VGG16

def args_input():
    parser = argparse.ArgumentParser(description='Set up mode')
    parser.add_argument('--use_webcam', type=bool, default=False, help='Choose webcam or not')
    return parser

class MainWindow:
    def __init__(self, storage=None, database=None, use_webcam=False):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # self.pixmap = QPixmap('/home/hqanh/Pictures/arrow.png')
        self.uic.label_10.setScaledContents(True)
        self.uic.label_11.setScaledContents(True)
        self.uic.label_early_blight.setScaledContents(True)
        self.uic.label_late_blight.setScaledContents(True)
        self.uic.label_healthy.setScaledContents(True)
        self.disease_label_uic = [self.uic.label_early_blight, 
                                  self.uic.label_late_blight, 
                                  self.uic.label_healthy]
        self.prob_label = [self.uic.prob_early,
                           self.uic.prob_late,
                           self.uic.prob_healthy]
        # self.uic.label_10.setPixmap(self.pixmap)
        self.img_captured = 0 # image to predict
        self.disease = {'name': 0, 'prob': 0}
        self.time = time.time()
        # create a timer
        self.timer = QTimer()

        self.storage = storage
        self.database = database
        # set timer timeout callback function
        self.use_webcam = use_webcam
        if use_webcam:
            self.timer.timeout.connect(self.viewCam)
        else:
            self.timer.timeout.connect(self.viewData)
        # self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.uic.control_bt.clicked.connect(self.controlTimer)

    #get data from firebase
    def getData(self):
        self.storage.child('leaf.png').download('leaf.png')
        # image = cv2.imread('leaf.png')
        image = Image.open('leaf.png')
        self.database.child('Data').update({'Image': 'received'})
        return image
    
    def viewData(self):
        user = self.database.child('Data').get().val()
        
        if (user['Image'] == 'sent'):
            self.img_captured = self.getData()
            image = self.img_captured.copy()
            image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
            self.Predict()

            height, width, channel = image.shape 
            step = channel * width
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            self.uic.label_10.setPixmap(QPixmap.fromImage(qImg))

            for d in self.disease_label_uic:
                d.setText('  ')
            for p in self.prob_label:
                p.setText('  ')

            self.disease_label_uic[self.disease['name']].setPixmap(QPixmap.fromImage(qImg))
            self.prob_label[self.disease['name']].setText('{}'.format(self.disease['prob']))

    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        if time.time() - self.time >= MIN_DURATION:
            self.img_captured = image.copy()
            self.uic.label_11.setPixmap(QPixmap.fromImage(qImg)) #set image for label 11
            self.Predict()
            self.time = time.time()
            for d in self.disease_label_uic:
                d.setText('  ')
            for p in self.prob_label:
                p.setText('  ')

            self.disease_label_uic[self.disease['name']].setPixmap(QPixmap.fromImage(qImg))
            self.prob_label[self.disease['name']].setText('{}'.format(self.disease['prob']))

        self.uic.label_10.setPixmap(QPixmap.fromImage(qImg))

    def Predict(self):
        self.img_captured = data_transforms(self.img_captured)
        self.img_captured = self.img_captured.unsqueeze(0).to(device)
        outputs = model(self.img_captured)
        prob, preds = torch.max(outputs, 1)
        status = ['early_blight', 'late_blight', 'healthy']
        print(outputs)
        self.disease['name'] = preds.item()
        self.disease['prob'] = prob.item()
        print('Predicted: ', status[preds.item()])

    def Grabcut(self):
        pass 

    def Reset(self):
        pass 
        
    # start/stop timer
    def controlTimer(self):
        self.time = time.time()
        # if timer is stopped
        if not self.timer.isActive():
            if self.use_webcam:
                # create video capture
                self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.uic.control_bt.setText("Stop")
            
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            if self.use_webcam:
                # release video capture
                self.cap.release()
            # update control_bt text
            self.uic.control_bt.setText("Start")

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    parser = args_input().parse_args()
    
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

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    data_transforms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    model = VGG16(num_classes=3)

    model.load_state_dict(torch.load('Models/VGG16_custom.pth', map_location=torch.device(device)))
    model.to(device)
    model.eval()

    MIN_DURATION = 2 # time to capture image

    app = QApplication(sys.argv)
    main_win = MainWindow(storage=storage, database=database, use_webcam=parser.use_webcam)
    main_win.show()
    sys.exit(app.exec())