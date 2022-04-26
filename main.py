import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel
from Potato import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QTimer
import os 
import time 
import cv2 

import torch 
import torch.nn as nn 
from torchvision import transforms
from network import VGG16

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
data_transforms = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

model = VGG16(num_classes=3)

model.load_state_dict(torch.load('Models/VGG16_custom.pth', map_location=torch.device(device)))
model.to(device)
model.eval()

MIN_DURATION = 2 # time to capture image

class MainWindow:
    def __init__(self):
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
        # set timer timeout callback function
        # self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        # self.uic.control_bt.clicked.connect(self.controlTimer)


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
            # release video capture
            self.cap.release()
            # update control_bt text
            self.uic.control_bt.setText("Start")

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())