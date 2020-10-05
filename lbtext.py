# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QFont
import os
import glob

pathDir = None
image_list = []
index = 0
curentid = -1
zoom = 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 400)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btBrowse = QtWidgets.QPushButton(self.centralWidget)
        self.btBrowse.setGeometry(QtCore.QRect(30, 10, 99, 27))
        self.btBrowse.setCheckable(False)
        self.btBrowse.setObjectName("btBrowse")

        self.lbText = QtWidgets.QLabel(self.centralWidget)
        self.lbText.setGeometry(QtCore.QRect(30, 60, 861, 17))
        self.lbText.setObjectName("lbText")
        
        self.lbImage = QtWidgets.QLabel(self.centralWidget)
        self.lbImage.setGeometry(QtCore.QRect(30, 100, 531, 192))
        self.lbImage.setObjectName("lbImage")
        self.lbImage.setStyleSheet("border: 2px solid blue");

        self.tbEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.tbEdit.setGeometry(QtCore.QRect(580, 100, 381, 51))
        self.tbEdit.setObjectName("tbEdit")
        self.tbEdit.setFont(QFont("Times",15))

        self.btBack = QtWidgets.QPushButton(self.centralWidget)
        self.btBack.setGeometry(QtCore.QRect(580, 180, 99, 27))
        self.btBack.setObjectName("btBack")

        self.btNext = QtWidgets.QPushButton(self.centralWidget)
        self.btNext.setGeometry(QtCore.QRect(720, 180, 99, 27))
        self.btNext.setObjectName("btNext")

        self.btZoomIn = QtWidgets.QPushButton(self.centralWidget)
        self.btZoomIn.setGeometry(QtCore.QRect(30, 330, 99, 27))
        self.btZoomIn.setObjectName("btZoomIn")

        self.btZoomOut = QtWidgets.QPushButton(self.centralWidget)
        self.btZoomOut.setGeometry(QtCore.QRect(170, 330, 99, 27))
        self.btZoomOut.setObjectName("btZoomOut")
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Label Text"))
        self.btBrowse.setText(_translate("MainWindow", "Browse"))
        self.btBrowse.clicked.connect(self.Browse)
        self.lbText.setText(_translate("MainWindow", "None"))
        self.btBack.setText(_translate("MainWindow", "Back"))
        self.btBack.clicked.connect(self.Back)
        self.btNext.setText(_translate("MainWindow", "Next"))
        self.btNext.clicked.connect(self.Next)
        self.btZoomIn.setText(_translate("MainWindow", "Zoom++"))
        self.btZoomIn.clicked.connect(self.ZoomIn)
        self.btZoomOut.setText(_translate("MainWindow", "Zoom--"))
        self.btZoomOut.clicked.connect(self.ZoomOut)
        self.tbEdit.textChanged.connect(self.TextChanged)

    def Browse(self,MainWindow):
        global pathDir,image_list,index,curentid
        pathDir = None
        image_list = []
        index = 0
        curentid = -1
        self.lbText.setText("None")
        self.tbEdit.setText("")
        self.lbImage.clear()
        pathDir = os.path.normpath(QtWidgets.QFileDialog.getExistingDirectory(self.centralWidget))
        try:
            for ext in ('*.jpeg', '*.png', '*.jpg'):
                image_list.extend(glob.glob(os.path.join(pathDir, ext)))
        except:
            pass
        if len(image_list) :
           self.loadData(image_list[index])

    def Next(self,MainWindow):
        global image_list,index
        if(len(image_list)) :
            text =self.tbEdit.text().rstrip()
            pre_txt_path = image_list[index][:-3]+'txt'
            open(pre_txt_path,'w',encoding="utf-8").write(text)
            if index<len(image_list)-1:
                index+=1
            self.loadData(image_list[index])

    def Back(self,MainWindow):
        global image_list,index
        if(len(image_list)) :
            text =self.tbEdit.text().rstrip()
            pre_txt_path = image_list[index][:-3]+'txt'
            open(pre_txt_path,'w',encoding="utf-8").write(text)
            if index>0:
                index-=1
            self.loadData(image_list[index])

    def ZoomIn(self,MainWindow):
        global zoom,image_list,index
        if(len(image_list)) :
            if zoom < 10 :
                zoom += 1
                image = QImage(image_list[index])
                ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
                image = image.scaled(int(zoom*image.width()/ratio),int(zoom*image.height()/ratio))
                pixmap = QPixmap().fromImage(image)
                self.lbImage.setPixmap(pixmap)

    def ZoomOut(self,MainWindow):
        global zoom,image_list,index
        if(len(image_list)) :
            if zoom > 1 :
                zoom -= 1
                image = QImage(image_list[index])
                ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
                image = image.scaled(int(zoom*image.width()/ratio),int(zoom*image.height()/ratio))
                pixmap = QPixmap().fromImage(image)
                self.lbImage.setPixmap(pixmap)

    def TextChanged(self,MainWindow):
        global curentid,index
        if len(image_list) and  curentid==index :
            text =self.tbEdit.text().rstrip()
            pre_txt_path = image_list[index][:-3]+'txt'
            open(pre_txt_path,'w',encoding="utf-8").write(text)

    def loadData(self,img_path):
        global w,zoom,curentid,index
        zoom = 1 #reset zoom
        txt_path = img_path[:-3]+'txt'
        self.lbText.setText(os.path.basename(img_path))
        image = QImage(img_path)
        ratio = max(1,max(image.width()/self.lbImage.frameGeometry().width(),image.height()/self.lbImage.frameGeometry().height()))
        image = image.scaled(int(image.width()/ratio),int(image.height()/ratio))
        pixmap = QPixmap().fromImage(image)
        self.lbImage.setPixmap(pixmap)
        if os.path.exists(txt_path):
            self.tbEdit.setText(open(txt_path, "r",encoding="utf-8").read().rstrip())
        else:
            self.tbEdit.setText("")
        self.tbEdit.setFocus()
        curentid=index

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

