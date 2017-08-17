# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_try.ui'
#
# Created: Tue Jul 18 16:36:13 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!


import cv2,sys
import numpy as np
from PyQt4 import QtCore, QtGui
from feature_extractor import Extractor,NaiveDlib
from preprocess.crop_util import crop_rotate_v2
from preprocess.image_preprocess import proc_img
from collections import deque


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_Face_Verification(object):
    def __init__(self):
        ext_model_path = './model/facenet/inception-ring-1024.pb'
        self.video_capture = cv2.VideoCapture(-1)
        self.capture = None
        self.id_image = None
        self.probe_image = None
        self.ID_flag = None
        self.Probe_flay = None


        self.naivedlib = NaiveDlib()
        self.extractor = Extractor(ext_model_path,gpu_fraction=0.5)
        temp = np.ones((5, 112, 96, 1))
        self.extractor.extract_feature(im_arr=temp)
        self.query = deque(maxlen=4)
        self.start()



    def setupUi(self, Face_Verification):
        Face_Verification.setObjectName(_fromUtf8("Face_Verification"))
        Face_Verification.resize(956, 674)

        frameGm = Face_Verification.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        Face_Verification.move(frameGm.topLeft())

        self.horizontalLayoutWidget = QtGui.QWidget(Face_Verification)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 490, 651, 161))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ID_Reader = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.ID_Reader.setObjectName(_fromUtf8("ID_Reader"))
        self.horizontalLayout.addWidget(self.ID_Reader)
        self.Take_Photo = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Take_Photo.setObjectName(_fromUtf8("Take_Photo"))
        self.horizontalLayout.addWidget(self.Take_Photo)
        self.Verify = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Verify.setObjectName(_fromUtf8("Verify"))
        self.horizontalLayout.addWidget(self.Verify)
        self.Clean = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Clean.setObjectName(_fromUtf8("Clean"))
        self.horizontalLayout.addWidget(self.Clean)
        self.label_3 = QtGui.QLabel(Face_Verification)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayoutWidget = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 260, 160, 251))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.Exit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.verticalLayout.addWidget(self.Exit)
        self.label_4 = QtGui.QLabel(Face_Verification)
        self.label_4.setGeometry(QtCore.QRect(770, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Face_Verification)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 180, 211, 311))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ID_photo = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.ID_photo.setText(_fromUtf8(""))
        self.ID_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.ID_photo.setObjectName(_fromUtf8("ID_photo"))
        self.horizontalLayout_2.addWidget(self.ID_photo)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Face_Verification)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(250, 180, 441, 311))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.Probe_photo = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.Probe_photo.setText(_fromUtf8(""))
        self.Probe_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.Probe_photo.setObjectName(_fromUtf8("Probe_photo"))
        self.horizontalLayout_4.addWidget(self.Probe_photo)
        self.label = QtGui.QLabel(Face_Verification)
        self.label.setGeometry(QtCore.QRect(100, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Face_Verification)
        self.label_2.setGeometry(QtCore.QRect(410, 130, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.retranslateUi(Face_Verification)
        QtCore.QMetaObject.connectSlotsByName(Face_Verification)

    def retranslateUi(self, Face_Verification):
        Face_Verification.setWindowTitle(_translate("Face_Verification", "Face_Verification", None))
        self.ID_Reader.setText(_translate("Face_Verification", "证件读取", None))
        self.Take_Photo.setText(_translate("Face_Verification", "拍照", None))
        self.Verify.setText(_translate("Face_Verification", "比对", None))
        self.Clean.setText(_translate("Face_Verification", "清空", None))
        self.label_3.setText(_translate("Face_Verification", "人证自动核验系统", None))
        self.pushButton_3.setText(_translate("Face_Verification", "数据报表", None))
        self.pushButton_4.setText(_translate("Face_Verification", "信息保存", None))
        self.pushButton_2.setText(_translate("Face_Verification", "账号管理", None))
        self.Exit.setText(_translate("Face_Verification", "退        出", None))
        self.label_4.setText(_translate("Face_Verification", "功能选项", None))
        self.label.setText(_translate("Face_Verification", "身份证信息", None))
        self.label_2.setText(_translate("Face_Verification", "照片信息", None))
        self.ID_Reader.clicked.connect(self.display_id_image)
        # self.Take_Photo.clicked.connect(self.)
        self.Clean.clicked.connect(self.clean_data)
        self.Verify.clicked.connect(self.verify)


    def display_id_image(self):
        try:
            image1 = cv2.imread('./card/zp.bmp')
            self.id_image = image1.copy()
            image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(image, image.shape[1],\
                                image.shape[0], image.shape[1] * 3,QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap(image)
            self.ID_photo.setPixmap(pix)
        except:
            self.ID_photo.setText(_translate("Face_Verification", "未检测到身份证", None))
            self.ID_photo.setStyleSheet('color: red')


    def display_probe_image(self):
        ret,image1 = self.video_capture.read()
        if ret:
            self.probe_image = image1.copy()
            try:
                bbox = self.naivedlib.getLargestFaceBoundingBox(image1)
                image1 = self.naivedlib.drawbbox(image1,bbox)
                if bbox:
                    image1 = cv2.rectangle(image1,(bbox.left(),bbox.top()),(bbox.right(),bbox.bottom()),[0,255,0],2)
            except:
                pass
            image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image,(320,240))
            # image = cv2.flip(image,1)
            image = QtGui.QImage(image, image.shape[1], \
                                 image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(image)
            self.Probe_photo.setPixmap(pix)
        else:
            self.probe_image = None
            self.Probe_photo.setText(_translate("Face_Verification", "未读取到图片", None))
            self.Probe_photo.setStyleSheet('color: red')

    def verify(self):
        web = Web_Browser()
        web.setModal(False)
        web.setWindowTitle(_translate("Face_Verification", "比对结果", None))
        if self.id_image is not None:
            ID_bbox = self.naivedlib.getLargestFaceBoundingBox(self.id_image)
            # if ID_bbox is not None:
            ID_left_eye, ID_right_eye = self.naivedlib.get_eyes(self.id_image, ID_bbox)
            ID_crop_image = crop_rotate_v2(self.id_image[:, :, ::-1], ID_left_eye, ID_right_eye,
                                           ID_bbox.width() * 1.03)
            ID_crop_image = proc_img(ID_crop_image, is_whiten=False)

            bbox = self.naivedlib.getLargestFaceBoundingBox(self.probe_image)
            if bbox is not None:
                left_eye, right_eye = self.naivedlib.get_eyes(self.probe_image, bbox)
                crop_image = crop_rotate_v2(self.probe_image[:, :, ::-1], left_eye, right_eye,
                                            bbox.width() * 1.0)
                flip_image = cv2.flip(crop_image.copy(), 1)
                crop_image = proc_img(crop_image, is_whiten=False)
                flip_image = proc_img(flip_image, is_whiten=False)
                self.query.append(crop_image[0])
                self.query.append(flip_image[0])

                prob_image = np.asarray(self.query)
                crop_house = np.concatenate((ID_crop_image, prob_image), axis=0)

                fea_house = self.extractor.extract_feature(im_arr=crop_house)
                score = self.extractor.cal_score(fea_house)
                if score>0.55:
                    web.write_result("比对成功")
                else:
                    web.write_result("比对失败",'red')
            else:
                 web.write_result("未检测到人脸", 'red')
        else:
            web.write_result("未检测到身份证", 'red')

        web.exec_()

    def clean_data(self):
        self.ID_photo.clear()
        self.Probe_photo.clear()
        self.id_image = None
        self.probe_image = None

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_probe_image)
        self.timer.start(1000./24)




class Web_Browser(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setObjectName(_fromUtf8("Result"))
        self.resize(400, 102)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 301, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

    def write_result(self,string,color='black'):
        self.label.setText(_translate("Result",string, None))
        self.label.setStyleSheet('color: {}'.format(color))

class QtCapture(QtGui.QWidget):
    def __init__(self, cap, label):
        # super(QtGui.QWidget, self).__init__()
        self.fps = 24
        self.cap = cap
        self.video_frame = label

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        # OpenCV yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)










if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    Face_Verification = QtGui.QWidget()
    ui = Ui_Face_Verification()
    ui.setupUi(Face_Verification)
    Face_Verification.show()
    sys.exit(app.exec_())






