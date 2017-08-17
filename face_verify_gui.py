# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work_try.ui'
#
# Created: Tue Jul 18 16:36:13 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!


import cv2,sys,os,time
import shutil
import subprocess
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
        self.video_capture = cv2.VideoCapture(0)
        self.id_image = None
        self.probe_image = None
        self.ID_label = 0
        self.ID_lib = {}
        self.ID_name = {}


        self.naivedlib = NaiveDlib()
        self.extractor = Extractor(ext_model_path,gpu_fraction=0)
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

        self.verticalLayoutWidget = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(750, 230, 160, 251))
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
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Face_Verification)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 260, 211, 311))
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
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(280, 260, 441, 311))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.Probe_photo = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.Probe_photo.setText(_fromUtf8(""))
        self.Probe_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.Probe_photo.setObjectName(_fromUtf8("Probe_photo"))
        self.horizontalLayout_4.addWidget(self.Probe_photo)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 180, 160, 80))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(290, 40, 391, 80))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayoutWidget_4 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(420, 180, 160, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayoutWidget_5 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(750, 100, 160, 80))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayoutWidget_6 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(780, 510, 160, 80))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.Open_ID = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.Open_ID.setObjectName(_fromUtf8("Open_ID"))
        self.verticalLayout_6.addWidget(self.Open_ID)
        self.verticalLayoutWidget_7 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(250, 610, 160, 31))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.Verify = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.Verify.setObjectName(_fromUtf8("Verify"))
        self.verticalLayout_7.addWidget(self.Verify)
        self.verticalLayoutWidget_8 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(40, 610, 160, 31))
        self.verticalLayoutWidget_8.setObjectName(_fromUtf8("verticalLayoutWidget_8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.add_to_id_query = QtGui.QPushButton(self.verticalLayoutWidget_8)
        self.add_to_id_query.setObjectName(_fromUtf8("add_to_id_query"))
        self.verticalLayout_8.addWidget(self.add_to_id_query)
        self.verticalLayoutWidget_9 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(460, 610, 160, 31))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.ID_search = QtGui.QPushButton(self.verticalLayoutWidget_9)
        self.ID_search.setObjectName(_fromUtf8("ID_search"))
        self.verticalLayout_9.addWidget(self.ID_search)
        self.verticalLayoutWidget_10 = QtGui.QWidget(Face_Verification)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(660, 610, 160, 31))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.clear = QtGui.QPushButton(self.verticalLayoutWidget_10)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.verticalLayout_10.addWidget(self.clear)

        self.retranslateUi(Face_Verification)
        QtCore.QMetaObject.connectSlotsByName(Face_Verification)

    def retranslateUi(self, Face_Verification):
        Face_Verification.setWindowTitle(_translate("Face_Verification", "Face_Verification", None))
        self.pushButton_3.setText(_translate("Face_Verification", "数据报表", None))
        self.pushButton_4.setText(_translate("Face_Verification", "信息保存", None))
        self.pushButton_2.setText(_translate("Face_Verification", "账号管理", None))
        self.Exit.setText(_translate("Face_Verification", "退        出", None))
        self.label.setText(_translate("Face_Verification", "身份证信息", None))
        self.label_3.setText(_translate("Face_Verification", "人证自动核验系统", None))
        self.label_2.setText(_translate("Face_Verification", "照片信息", None))
        self.label_4.setText(_translate("Face_Verification", "功能选项", None))
        self.Open_ID.setText(_translate("Face_Verification", "打开身份证阅读器", None))
        self.Verify.setText(_translate("Face_Verification", "人证验证", None))
        self.add_to_id_query.setText(_translate("Face_Verification", "添加到比对库", None))
        self.ID_search.setText(_translate("Face_Verification", "身份检索", None))
        self.clear.setText(_translate("Face_Verification", "清空", None))
        self.Open_ID.clicked.connect(self.Open_ID_Reader)
        self.add_to_id_query.clicked.connect(self.add_to_lib)
        self.Verify.clicked.connect(self.verify)
        self.ID_search.clicked.connect(self.search_ID)
        self.clear.clicked.connect(self.all_clean)
        self.start_read_ID()

        # self.Clean.clicked.connect(self.clean_data)
        # self.Verify.clicked.connect(self.verify)
        # self.Open_ID.clicked.connect(self.Open_ID_Reader)



    def display_id_image(self):
        image = cv2.cvtColor(self.id_image, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(image, image.shape[1],\
                            image.shape[0], image.shape[1] * 3,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap(image)
        self.ID_photo.setPixmap(pix)


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

    def all_clean(self):
        self.id_image = None
        self.probe_image = None
        self.ID_label = 0
        self.ID_lib = {}
        self.ID_name = {}
        self.ID_photo.clear()
        self.Probe_photo.clear()
        self.id_image = None
        self.probe_image = None
        try:
            os.remove('./card/zp.bmp')
            os.remove('./card/ID_image/*')
        except:
            pass


    def search_ID(self):
        web = Web_Browser()
        web.setModal(False)
        web.setWindowTitle(_translate("Face_Verification", "比对结果", None))
        bbox = self.naivedlib.getLargestFaceBoundingBox(self.probe_image)
        try:
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
                fea_house = self.extractor.extract_feature(im_arr=prob_image)
                target = self.extractor.search_face(fea_house,self.ID_lib)
                if target is not None:
                    self.id_image = cv2.imread("./card/ID_img/{}.bmp".format(target))
                    self.display_id_image()
                    web.write_result("检索结果: {}".format(self.ID_name[target].encode('utf-8')), 'black')
                else:
                    web.write_result("不在检索库中", 'red')
                web.exec_()
        except:
            web.write_result("检索库为空", 'red')
            web.exec_()

    def add_to_lib(self):
        web = Web_Browser()
        web.setModal(False)
        web.setWindowTitle(_translate("Face_Verification", "比对结果", None))
        try:
            file = open('./card/wz.txt','rb')
            data = file.read()
            name = data.decode('utf-16').strip().split(' ')[0]
            shutil.copyfile("./card/zp.bmp","./card/ID_img/{}.bmp".format(self.ID_label))
            ID_bbox = self.naivedlib.getLargestFaceBoundingBox(self.id_image)
            ID_left_eye, ID_right_eye = self.naivedlib.get_eyes(self.id_image, ID_bbox)
            ID_crop_image = crop_rotate_v2(self.id_image[:, :, ::-1], ID_left_eye, ID_right_eye,
                                           ID_bbox.width() * 1.03)
            ID_crop_image = proc_img(ID_crop_image, is_whiten=False)
            ID_fea = self.extractor.extract_feature(im_arr=ID_crop_image)
            self.ID_lib[self.ID_label] = ID_fea
            self.ID_name[self.ID_label] = name
            self.ID_label = self.ID_label + 1
        except:
            web.write_result("未检测到身份证信息", 'red')
            web.exec_()


    def verify(self):
        web = Web_Browser()
        web.setModal(False)
        web.setWindowTitle(_translate("Face_Verification", "比对结果", None))
        try:
            image = cv2.imread('./card/zp.bmp')
            self.id_image = image.copy()
            self.display_id_image()
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
                web.exec_()
                self.clean_data()
            else:
                pass
        except:
            web.write_result("未检测到身份证信息", 'red')
            web.exec_()


    def read_ID_image(self):
        try:
            image = cv2.imread('./card/zp.bmp')
            self.id_image = image.copy()
            self.display_id_image()
        except:
            pass

    def clean_data(self):
        self.ID_photo.clear()
        self.Probe_photo.clear()
        self.id_image = None
        self.probe_image = None
        try:
            os.remove('./card/zp.bmp')
        except:
            pass


    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_probe_image)
        self.timer.start(1000./24)

    def start_read_ID(self):
        self.timer2 = QtCore.QTimer()
        self.timer.timeout.connect(self.read_ID_image)
        self.timer.start(1)


    def Open_ID_Reader(self):
        # os.system('C:\\Users\\Gehen\\Desktop\\Face_Verify\\card\\ZKIDCardReader.exe')
        subprocess.Popen('C:\\Users\\Gehen\\Desktop\\Face_Verify\\card\\ZKIDCardReader.exe')




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
        QtCore.QTimer.singleShot(2000,self.close)

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







