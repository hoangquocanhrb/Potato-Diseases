# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Potato.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(31, 171, 137);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 441, 31))
        self.label.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"\n"
"font: 75 15pt \"Ubuntu Mono\";\n"
"border-radius: 10px;\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 300, 151, 31))
        self.label_2.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 75 15pt \"Ubuntu Mono\";\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 300, 141, 31))
        self.label_3.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 75 15pt \"Ubuntu Mono\";\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 490, 71, 21))
        self.label_4.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 490, 81, 21))
        self.label_5.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 490, 101, 21))
        self.label_6.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"border-radius: 10px;")
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 60, 231, 231))
        self.label_10.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"border-radius: 10px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(450, 60, 231, 231))
        self.label_11.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"border-radius: 10px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 360, 131, 111))
        self.widget.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_early_blight = QtWidgets.QLabel(self.widget)
        self.label_early_blight.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.label_early_blight.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_early_blight.setText("")
        self.label_early_blight.setObjectName("label_early_blight")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(350, 360, 131, 111))
        self.widget_2.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"border-radius: 10px;")
        self.widget_2.setObjectName("widget_2")
        self.label_late_blight = QtWidgets.QLabel(self.widget_2)
        self.label_late_blight.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.label_late_blight.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_late_blight.setText("")
        self.label_late_blight.setObjectName("label_late_blight")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(570, 360, 131, 111))
        self.widget_3.setStyleSheet("background-color: rgb(157, 243, 196);\n"
"border-radius: 10px;")
        self.widget_3.setObjectName("widget_3")
        self.label_healthy = QtWidgets.QLabel(self.widget_3)
        self.label_healthy.setGeometry(QtCore.QRect(10, 10, 111, 91))
        self.label_healthy.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_healthy.setText("")
        self.label_healthy.setObjectName("label_healthy")
        self.prob_healthy = QtWidgets.QLabel(self.centralwidget)
        self.prob_healthy.setGeometry(QtCore.QRect(570, 460, 61, 21))
        self.prob_healthy.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;")
        self.prob_healthy.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prob_healthy.setObjectName("prob_healthy")
        self.prob_late = QtWidgets.QLabel(self.centralwidget)
        self.prob_late.setGeometry(QtCore.QRect(350, 460, 61, 21))
        self.prob_late.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;")
        self.prob_late.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prob_late.setObjectName("prob_late")
        self.prob_early = QtWidgets.QLabel(self.centralwidget)
        self.prob_early.setGeometry(QtCore.QRect(120, 460, 61, 21))
        self.prob_early.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-radius: 10px;")
        self.prob_early.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prob_early.setObjectName("prob_early")
        self.control_bt = QtWidgets.QPushButton(self.centralwidget)
        self.control_bt.setGeometry(QtCore.QRect(20, 170, 89, 25))
        self.control_bt.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.control_bt.setObjectName("control_bt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " TOPIC NAME: POTATO DISEASES CLASSIFICATION"))
        self.label_2.setText(_translate("MainWindow", " ẢNH CHỤP ĐƯỢC"))
        self.label_3.setText(_translate("MainWindow", "  ẢNH XỬ LÝ"))
        self.label_4.setText(_translate("MainWindow", " Úa sớm"))
        self.label_5.setText(_translate("MainWindow", " Héo muộn"))
        self.label_6.setText(_translate("MainWindow", "Khỏe mạnh"))
        self.prob_healthy.setText(_translate("MainWindow", "Xác suất"))
        self.prob_late.setText(_translate("MainWindow", "Xác suất"))
        self.prob_early.setText(_translate("MainWindow", "Xác suất"))
        self.control_bt.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
