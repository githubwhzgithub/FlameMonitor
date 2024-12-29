# -*- coding: utf-8 -*-

import argparse
import csv
import os
import platform
import sys
import time
from pathlib import Path
import torch
from PySide6.QtGui import QImage, QPixmap

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

global FPS
FPS = 1
global FireNumber
FireNumber = 0
global im0

from ultralytics.utils.plotting import Annotator, colors, save_one_box

from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams
from utils.general import (
    LOGGER,
    Profile,
    check_file,
    check_img_size,
    check_imshow,
    check_requirements,
    colorstr,
    cv2,
    increment_path,
    non_max_suppression,
    print_args,
    scale_boxes,
    strip_optimizer,
    xyxy2xywh,
)
from utils.torch_utils import select_device, smart_inference_mode

import cv2
################################################################################
## Form generated from reading UI file 'FireUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLCDNumber, QLabel, QLayout, QProgressBar,
                               QPushButton, QSizePolicy, QSlider, QSpacerItem,
                               QVBoxLayout, QWidget, QFileDialog)
from qt_material import apply_stylesheet
import uiResource_rc

class Ui_FireUI(QWidget):
    def setupUi(self, FireUI):
        if not FireUI.objectName():
            FireUI.setObjectName(u"FireUI")
        FireUI.resize(1020, 711)
        FireUI.setStyleSheet(u"background-color: rgb(28, 27, 51);")
        self.horizontalLayout_2 = QHBoxLayout(FireUI)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.Menu = QFrame(FireUI)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(36, 36, 64);")
        self.Menu.setFrameShape(QFrame.Shape.Box)
        self.Menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 0, 2, 10)
        self.HUSTimage = QLabel(self.Menu)
        self.HUSTimage.setObjectName(u"HUSTimage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HUSTimage.sizePolicy().hasHeightForWidth())
        self.HUSTimage.setSizePolicy(sizePolicy)
        self.HUSTimage.setMinimumSize(QSize(0, 10))
        self.HUSTimage.setMaximumSize(QSize(200, 200))
        self.HUSTimage.setFrameShape(QFrame.Shape.Box)
        self.HUSTimage.setPixmap(QPixmap(u":/all/UI_image/huazhongkejidaxue.png"))
        self.HUSTimage.setScaledContents(True)
        self.HUSTimage.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.HUSTimage)

        self.FILE = Path(__file__).resolve()
        self.ROOT = self.FILE.parents[0]  # YOLOv5 root directory
        if str(self.ROOT) not in sys.path:
            sys.path.append(str(self.ROOT))  # add ROOT to PATH
        self.ROOT = Path(os.path.relpath(self.ROOT, Path.cwd()))  # relative

        self.image = QPushButton(self.Menu)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u5b8b\u4f53"])
        font.setPointSize(14)
        self.image.setFont(font)
        self.image.setStyleSheet(u"color:rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/all/UI_image/\u56fe\u7247.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.image.setIcon(icon)
        self.image.setIconSize(QSize(45, 45))
        self.image.setCheckable(False)
        self.image.clicked.connect(self.detectImage)

        self.verticalLayout_2.addWidget(self.image)

        self.vedio = QPushButton(self.Menu)
        self.vedio.setObjectName(u"vedio")
        self.vedio.setMinimumSize(QSize(0, 50))
        self.vedio.setFont(font)
        self.vedio.setStyleSheet(u"color:rgb(255, 255, 255);qproperty - iconAlignment: 'AlignLeft';")
        icon1 = QIcon()
        icon1.addFile(u":/all/UI_image/\u89c6\u9891.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.vedio.setIcon(icon1)
        self.vedio.setIconSize(QSize(45, 45))
        self.vedio.clicked.connect(self.detectVideo)

        self.verticalLayout_2.addWidget(self.vedio)

        self.realTime = QPushButton(self.Menu)
        self.realTime.setObjectName(u"realTime")
        self.realTime.setMinimumSize(QSize(0, 50))
        self.realTime.setFont(font)
        self.realTime.setStyleSheet(u"color:rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/all/UI_image/\u5f55\u50cf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.realTime.setIcon(icon2)
        self.realTime.setIconSize(QSize(45, 45))
        self.realTime.clicked.connect(self.detectRealTime)

        self.verticalLayout_2.addWidget(self.realTime)

        self.line = QFrame(self.Menu)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(99, 93, 222);")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.model = QLabel(self.Menu)
        self.model.setObjectName(u"model")
        self.model.setMaximumSize(QSize(45, 45))
        self.model.setPixmap(QPixmap(u":/all/UI_image/model.png"))
        self.model.setScaledContents(True)
        self.model.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.model)

        self.modelChoose = QComboBox(self.Menu)
        self.modelChoose.addItems(['YOLOv5s', 'YOLOv5m', 'YOLOv5l'])
        self.modelChoose.setObjectName(u"modelChoose")
        self.modelChoose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.modelChoose.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.modelChoose.currentTextChanged.connect(self.update_model)


        self.verticalLayout_2.addWidget(self.modelChoose)


        self.horizontalLayout_2.addWidget(self.Menu)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.welcome = QLabel(FireUI)
        self.welcome.setObjectName(u"welcome")
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5988\u5988\u6570\u9ed1\u4f53"])
        font1.setPointSize(26)
        self.welcome.setFont(font1)
        self.welcome.setStyleSheet(u"color: rgb(255, 255, 255);font-size:26px;!important;")
        self.welcome.setLineWidth(0)
        self.welcome.setIndent(-4)

        self.verticalLayout.addWidget(self.welcome)

        self.state = QLabel(FireUI)
        self.state.setObjectName(u"state")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(8)
        font2.setItalic(True)
        self.state.setFont(font2)
        self.state.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.state.setLineWidth(0)
        self.state.setIndent(-4)

        self.verticalLayout.addWidget(self.state)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.frame_4 = QFrame(FireUI)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 500))
        self.frame_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.frame_4.setStyleSheet(u"background-color: rgb(36, 36, 64);\n"
"border-radius: 20px;")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/all/UI_image/\u7f6e\u4fe1\u5ea6\u9608\u503c.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.conf = QLabel(self.frame_4)
        self.conf.setObjectName(u"conf")
        self.conf.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_3.addWidget(self.conf)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.confSlider = QSlider(self.frame_4)
        self.confSlider.setObjectName(u"confSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.confSlider.sizePolicy().hasHeightForWidth())
        self.confSlider.setSizePolicy(sizePolicy1)
        self.confSlider.setMaximumSize(QSize(16777215, 30))
        self.confSlider.setMaximum(100)
        self.confSlider.setOrientation(Qt.Orientation.Horizontal)
        self.confSlider.valueChanged.connect(self.update_conf)
        self.confvalue = 0.25

        self.verticalLayout_3.addWidget(self.confSlider)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(FireUI)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 500))
        self.frame_5.setStyleSheet(u"background-color: rgb(36, 36, 64);\n"
"border-radius: 20px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setPixmap(QPixmap(u":/all/UI_image/\u6a21\u578b\u8bc4\u4f30_\u5e73\u5747\u4ea4\u5e76\u6bd4\u8bc4\u4f30.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.IOU = QLabel(self.frame_5)
        self.IOU.setObjectName(u"conf_2")
        self.IOU.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.IOU)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.IOUSlider = QSlider(self.frame_5)
        self.IOUSlider.setObjectName(u"confSlider_2")
        sizePolicy1.setHeightForWidth(self.IOUSlider.sizePolicy().hasHeightForWidth())
        self.IOUSlider.setSizePolicy(sizePolicy1)
        self.IOUSlider.setMaximumSize(QSize(16777215, 30))
        self.IOUSlider.setStyleSheet(u"color: rgb(255, 255, 127);")
        self.IOUSlider.setMaximum(100)
        self.IOUSlider.setOrientation(Qt.Orientation.Horizontal)
        self.IOUSlider.valueChanged.connect(self.update_IOU)
        self.IOUvalue = 0.45


        self.verticalLayout_4.addWidget(self.IOUSlider)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)

        self.horizontalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.frame_5)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.imageShow = QLabel(FireUI)
        self.imageShow.setObjectName(u"imageShow")
        self.imageShow.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(36, 36, 64);")
        self.imageShow.setFrameShape(QFrame.Shape.Box)
        self.imageShow.setFrameShadow(QFrame.Shadow.Plain)
        self.imageShow.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.imageShow.setPixmap(QPixmap(u":/all/UI_image/火.png"))
        #self.imageShow.setScaledContents(True)

        self.verticalLayout.addWidget(self.imageShow)

        self.switchButton = QPushButton(FireUI)
        self.switchButton.setObjectName(u"switchButton")
        self.switchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.switchButton.setStyleSheet(u"color: rgb(255, 255, 255);background-color: rgb(36, 36, 64);")
        self.switchButton.setText("显示图像")
        self.imagecount = -1
        self.switchButton.clicked.connect(self.switchImage)

        self.verticalLayout.addWidget(self.switchButton)

        self.frame_2 = QFrame(FireUI)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(36, 36, 64);\n"
"border-radius: 20px;\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(45, 45))
        self.label_5.setPixmap(QPixmap(u":/all/UI_image/\u706b.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lcdNumber = QLCDNumber(self.frame_2)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout_7.addWidget(self.lcdNumber)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(45, 45))
        self.label_6.setPixmap(QPixmap(u":/all/UI_image/FPS.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.fpsNumber = QLCDNumber(self.frame_2)
        self.fpsNumber.setObjectName(u"FPS_number")

        self.horizontalLayout_7.addWidget(self.fpsNumber)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 4)
        self.horizontalLayout_7.setStretch(2, 6)
        self.horizontalLayout_7.setStretch(3, 2)
        self.horizontalLayout_7.setStretch(4, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_5.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 10)
        self.verticalLayout.setStretch(4, 3)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(1, 60)

        self.retranslateUi(FireUI)

        self.imageData = []

        QMetaObject.connectSlotsByName(FireUI)
    # setupUi

    def update_conf(self):
        value = self.confSlider.value()
        percentage_value1 = value / 100  # 计算滑条数值的百分之一
        self.conf.setText(f"{percentage_value1:.2f}")  # 设置标签文本并保留两位小数
        self.confvalue = percentage_value1

    def update_model(self):
        self.YOLOmodel = "runs/train/" + self.modelChoose.currentText() + "/weights/last.pt"

    def update_IOU(self):
        value = self.IOUSlider.value()
        percentage_value2 = value / 100  # 计算滑条数值的百分之一
        self.IOU.setText(f"{percentage_value2:.2f}")  # 设置标签文本并保留两位小数
        self.IOUvalue = percentage_value2

    def retranslateUi(self, FireUI):
        FireUI.setWindowTitle(QCoreApplication.translate("FireUI", u"Form", None))
        self.HUSTimage.setText("")
        self.image.setText(QCoreApplication.translate("FireUI", u"\u56fe\u50cf", None))
        self.vedio.setText(QCoreApplication.translate("FireUI", u"\u89c6\u9891", None))
        self.realTime.setText(QCoreApplication.translate("FireUI", u"\u5b9e\u65f6\u76d1\u6d4b", None))
        self.model.setText("")
        self.modelChoose.setItemText(0, QCoreApplication.translate("FireUI", u"YOLOv5s", None))
        self.modelChoose.setItemText(1, QCoreApplication.translate("FireUI", u"YOLOv5m", None))
        self.modelChoose.setItemText(2, QCoreApplication.translate("FireUI", u"YOLOv5l", None))

        self.welcome.setText(QCoreApplication.translate("FireUI", u"Welcome!", None))
        self.state.setText(QCoreApplication.translate("FireUI", u"Here's WangHaozhen and LiuXiaoxu's FireMonitor", None))
        self.label.setText("")
        self.label_3.setText("置信度阈值")
        self.conf.setText(QCoreApplication.translate("FireUI", u"\u6570\u503c", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("FireUI", u"\u4ea4\u5e76\u6bd4", None))
        self.IOU.setText(QCoreApplication.translate("FireUI", u"\u6570\u503c", None))
        self.imageShow.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
    # retranslateUi

    def detectImage(self):
        # 打开文件选择对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        if file_dialog.exec_():
            # 获取选择的文件路径
            file_path = file_dialog.selectedFiles()[0]
            # 调用检测函数
            print(self.ROOT)
            self.run(source=file_path,weights=self.ROOT /self.YOLOmodel,conf_thres=self.confvalue,
                       iou_thres=self.IOUvalue,device='0')
            self.fpsNumber.display(self.FPS)
            self.lcdNumber.display(self.FireNumber)



    def detectVideo(self):
        # 打开文件选择对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Videos (*.mp4 *.avi *.mov)")
        if file_dialog.exec_():
            # 获取选择的文件路径
            file_path = file_dialog.selectedFiles()[0]
            # 调用检测函数
            self.run(source=file_path,weights=self.ROOT / self.YOLOmodel,conf_thres=self.confvalue,
                       iou_thres=self.IOUvalue,device='0',view_img=True)



    def switchImage(self):
        self.imagecount += 1
        self.display(self.imageShow,self.ROOT,self.imagecount)

    @staticmethod
    def display(label,ROOT,i):
        try:
            image_extensions = ['.jpg', '.png', '.gif']
            image_paths = []
            folder = Path(ROOT /'runs/detect/result')
            for file in folder.iterdir():
                if file.is_file():
                    file_extension = file.suffix
                    if file_extension in image_extensions:
                        image_paths.append(str(file))



            # 将图片显示在标签(label)上
            label.setPixmap(QPixmap.fromImage(QImage(str(image_paths[i % image_paths.__len__() - 1]))))

        except Exception as e:
            # 处理异常，印出错误信息
            print(repr(e))

    def detectRealTime(self):
        # 调用检测函数
        self.run(source='0', weights=self.ROOT / self.YOLOmodel, conf_thres=self.confvalue,
                 iou_thres=self.IOUvalue, device='0',view_img=True)


    def run(
        self,
        weights=ROOT / "yolov5s.pt",  # model path or triton URL runs/train/YOLOv5m
        source="data/images",  # file/dir/URL/glob/screen/0(webcam)
        data=ROOT / "data/fire_data.yaml",  # dataset.yaml path
        imgsz=(640, 640),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device="0",  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=False,  # save results to *.txt
        save_format=0,  # save boxes coordinates in YOLO format or Pascal-VOC format (0 for YOLO and 1 for Pascal-VOC)
        save_csv=False,  # save results in CSV format
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes=None,  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project=ROOT / "runs/detect",  # save results to project/name
        name="result",  # save results to project/name
        exist_ok=True,  # existing project/name ok, do not increment
        line_thickness=3,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        vid_stride=1,  # video frame-rate stride
    ):
        """
        Runs YOLOv5 detection inference on various sources like images, videos, directories, streams, etc.

        Args:
            weights (str | Path): Path to the model weights file or a Triton URL. Default is 'yolov5s.pt'.
            source (str | Path): Input source, which can be a file, directory, URL, glob pattern, screen capture, or webcam
                index. Default is 'data/images'.
            data (str | Path): Path to the dataset YAML file. Default is 'data/coco128.yaml'.
            imgsz (tuple[int, int]): Inference image size as a tuple (height, width). Default is (640, 640).
            conf_thres (float): Confidence threshold for detections. Default is 0.25.
            iou_thres (float): Intersection Over Union (IOU) threshold for non-max suppression. Default is 0.45.
            max_det (int): Maximum number of detections per image. Default is 1000.
            device (str): CUDA device identifier (e.g., '0' or '0,1,2,3') or 'cpu'. Default is an empty string, which uses the
                best available device.
            view_img (bool): If True, display inference results using OpenCV. Default is False.
            save_txt (bool): If True, save results in a text file. Default is False.
            save_csv (bool): If True, save results in a CSV file. Default is False.
            save_conf (bool): If True, include confidence scores in the saved results. Default is False.
            save_crop (bool): If True, save cropped prediction boxes. Default is False.
            nosave (bool): If True, do not save inference images or videos. Default is False.
            classes (list[int]): List of class indices to filter detections by. Default is None.
            agnostic_nms (bool): If True, perform class-agnostic non-max suppression. Default is False.
            augment (bool): If True, use augmented inference. Default is False.
            visualize (bool): If True, visualize feature maps. Default is False.
            update (bool): If True, update all models' weights. Default is False.
            project (str | Path): Directory to save results. Default is 'runs/detect'.
            name (str): Name of the current experiment; used to create a subdirectory within 'project'. Default is 'exp'.
            exist_ok (bool): If True, existing directories with the same name are reused instead of being incremented. Default is
                False.
            line_thickness (int): Thickness of bounding box lines in pixels. Default is 3.
            hide_labels (bool): If True, do not display labels on bounding boxes. Default is False.
            hide_conf (bool): If True, do not display confidence scores on bounding boxes. Default is False.
            half (bool): If True, use FP16 half-precision inference. Default is False.
            dnn (bool): If True, use OpenCV DNN backend for ONNX inference. Default is False.
            vid_stride (int): Stride for processing video frames, to skip frames between processing. Default is 1.

        Returns:
            None

        Examples:
            ```python
            from ultralytics import run

            # Run inference on an image
            run(source='data/images/example.jpg', weights='yolov5s.pt', device='0')

            # Run inference on a video with specific confidence threshold
            run(source='data/videos/example.mp4', weights='yolov5s.pt', conf_thres=0.4, device='0')
            ```
        """

        source = str(source)
        save_img = not nosave and not source.endswith(".txt")  # save inference images
        is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        is_url = source.lower().startswith(("rtsp://", "rtmp://", "http://", "https://"))
        webcam = source.isnumeric() or source.endswith(".streams") or (is_url and not is_file)
        screenshot = source.lower().startswith("screen")
        if is_url and is_file:
            source = check_file(source)  # download

        # Directories
        save_dir = increment_path(Path(project) / name, exist_ok=exist_ok)  # increment run
        (save_dir / "labels" if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

        # Load model
        device = select_device(device)
        model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data, fp16=half)
        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(imgsz, s=stride)  # check image size
        cap = cv2.VideoCapture(source)
        frameNumber = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        # Dataloader
        bs = 1  # batch_size
        if webcam:
            view_img = check_imshow(warn=True)
            dataset = LoadStreams(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
            bs = len(dataset)
        elif screenshot:
            dataset = LoadScreenshots(source, img_size=imgsz, stride=stride, auto=pt)
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=vid_stride)
        vid_path, vid_writer = [None] * bs, [None] * bs

        # Run inference
        model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(device=device), Profile(device=device), Profile(device=device))
        for path, im, im0s, vid_cap, s in dataset:
            with dt[0]:
                im = torch.from_numpy(im).to(model.device)
                im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim
                if model.xml and im.shape[0] > 1:
                    ims = torch.chunk(im, im.shape[0], 0)

            # Inference
            with dt[1]:
                visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if visualize else False
                if model.xml and im.shape[0] > 1:
                    pred = None
                    for image in ims:
                        if pred is None:
                            pred = model(image, augment=augment, visualize=visualize).unsqueeze(0)
                        else:
                            pred = torch.cat((pred, model(image, augment=augment, visualize=visualize).unsqueeze(0)), dim=0)
                    pred = [pred, None]
                else:
                    pred = model(im, augment=augment, visualize=visualize)
            # NMS
            with dt[2]:
                pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)

            # Second-stage classifier (optional)
            # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

            # Define the path for the CSV file
            csv_path = save_dir / "predictions.csv"

            # Create or append to the CSV file
            def write_to_csv(image_name, prediction, confidence):
                """Writes prediction data for an image to a CSV file, appending if the file exists."""
                data = {"Image Name": image_name, "Prediction": prediction, "Confidence": confidence}
                with open(csv_path, mode="a", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=data.keys())
                    if not csv_path.is_file():
                        writer.writeheader()
                    writer.writerow(data)

            # Process predictions
            for i, det in enumerate(pred):  # per image
                seen += 1
                if webcam:  # batch_size >= 1
                    p, im0, frame = path[i], im0s[i].copy(), dataset.count
                    s += f"{i}: "
                else:
                    p, im0, frame = path, im0s.copy(), getattr(dataset, "frame", 0)

                p = Path(p)  # to Path
                save_path = str(save_dir / p.name)  # im.jpg
                txt_path = str(save_dir / "labels" / p.stem) + ("" if dataset.mode == "image" else f"_{frame}")  # im.txt
                s += "{:g}x{:g} ".format(*im.shape[2:])  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                imc = im0.copy() if save_crop else im0  # for save_crop
                annotator = Annotator(im0, line_width=line_thickness, example=str(names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        c = int(cls)  # integer class
                        label = names[c] if hide_conf else f"{names[c]}"
                        confidence = float(conf)
                        confidence_str = f"{confidence:.2f}"

                        if save_csv:
                            write_to_csv(p.name, label, confidence_str)

                        if save_txt:  # Write to file
                            if save_format == 0:
                                coords = (
                                    (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                                )  # normalized xywh
                            else:
                                coords = (torch.tensor(xyxy).view(1, 4) / gn).view(-1).tolist()  # xyxy
                            line = (cls, *coords, conf) if save_conf else (cls, *coords)  # label format
                            with open(f"{txt_path}.txt", "a") as f:
                                f.write(("%g " * len(line)).rstrip() % line + "\n")

                        if save_img or save_crop or view_img:  # Add bbox to image
                            c = int(cls)  # integer class
                            label = None if hide_labels else (names[c] if hide_conf else f"{names[c]} {conf:.2f}")
                            annotator.box_label(xyxy, label, color=colors(c, True))
                        if save_crop:
                            save_one_box(xyxy, imc, file=save_dir / "crops" / names[c] / f"{p.stem}.jpg", BGR=True)

                im0 = annotator.result()
                if view_img:
                    if platform.system() == "Linux" and p not in windows:
                        windows.append(p)
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                    cv2.imshow(str(p), im0)
                    cv2.waitKey(1)  # 1 millisecond

                 #Save results (image with detections)
                if save_img:
                    if dataset.mode == "image":
                        cv2.imwrite(save_path, im0)
                    else:  # 'video' or 'stream'
                        if vid_path[i] != save_path:  # new video
                            vid_path[i] = save_path
                            if isinstance(vid_writer[i], cv2.VideoWriter):
                                vid_writer[i].release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path = str(Path(save_path).with_suffix(".mp4"))  # force *.mp4 suffix on results videos
                            vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
                        vid_writer[i].write(im0)

            # Print time (inference-only)
            LOGGER.info(f"{s}{'' if len(det) else '(no detections), '}{dt[1].dt * 1E3:.1f}ms")
            self.progressBar.setValue(seen/frameNumber*100)
            self.lcdNumber.display(len(det))
            self.fpsNumber.display(1000 / (dt[1].dt))

        # Print results
        t = tuple(x.t / seen * 1e3 for x in dt)  # speeds per image
        LOGGER.info(f"Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *imgsz)}" % t)
        self.FPS = 1000 / t[1]
        self.FireNumber = len(det)

        if save_txt or save_img:
            s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ""
            LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
        if update:
            strip_optimizer(weights[0])  # update model (to fix SourceChangeWarning)




if __name__ == '__main__':
    app = QApplication()
    window = Ui_FireUI()
    window.setupUi(window)
    apply_stylesheet(app, theme='dark_blue.xml')
    window.show()
    app.exec()