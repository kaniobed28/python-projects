from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
from selenium.webdriver.common.keys import Keys


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(902, 542)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.countryheadeerframe = QtWidgets.QFrame(Form)
        self.countryheadeerframe.setMaximumSize(QtCore.QSize(16777215, 83))
        self.countryheadeerframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.countryheadeerframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.countryheadeerframe.setObjectName("countryheadeerframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.countryheadeerframe)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maintitleframe = QtWidgets.QFrame(self.countryheadeerframe)
        self.maintitleframe.setMinimumSize(QtCore.QSize(0, 43))
        self.maintitleframe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.maintitleframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.maintitleframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.maintitleframe.setObjectName("maintitleframe")
        self.Warning = QtWidgets.QLabel(self.maintitleframe)
        self.Warning.setGeometry(QtCore.QRect(10, 10, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Warning.setFont(font)
        self.Warning.setText("")
        self.Warning.setObjectName("Warning")
        self.horizontalLayout.addWidget(self.maintitleframe)
        self.verticalLayout.addWidget(self.countryheadeerframe)
        self.contentheaderframe = QtWidgets.QFrame(Form)
        self.contentheaderframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentheaderframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentheaderframe.setObjectName("contentheaderframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.contentheaderframe)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.contentBody = QtWidgets.QFrame(self.contentheaderframe)
        self.contentBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBody.setObjectName("contentBody")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contentBody)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.contentBody)
        self.frame_2.setMinimumSize(QtCore.QSize(606, 0))
        self.frame_2.setStyleSheet("background-color: rgb(228, 255, 128);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.indexNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.indexNoLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.indexNoLineEdit.setObjectName("indexNoLineEdit")
        self.horizontalLayout_3.addWidget(self.indexNoLineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.examTypeCombo = QtWidgets.QComboBox(self.groupBox)
        self.examTypeCombo.setMinimumSize(QtCore.QSize(0, 0))
        self.examTypeCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.examTypeCombo.setObjectName("examTypeCombo")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.examTypeCombo.addItem("")
        self.horizontalLayout_4.addWidget(self.examTypeCombo)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.examYearCombo = QtWidgets.QComboBox(self.groupBox)
        self.examYearCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.examYearCombo.setObjectName("examYearCombo")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.examYearCombo.addItem("")
        self.horizontalLayout_5.addWidget(self.examYearCombo)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dayCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.dayCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dayCombo.setObjectName("dayCombo")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.dayCombo.addItem("")
        self.horizontalLayout_6.addWidget(self.dayCombo)
        self.monthCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.monthCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.monthCombo.setObjectName("monthCombo")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.monthCombo.addItem("")
        self.horizontalLayout_6.addWidget(self.monthCombo)
        self.yearCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.yearCombo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yearCombo.setObjectName("yearCombo")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.yearCombo.addItem("")
        self.horizontalLayout_6.addWidget(self.yearCombo)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.SerialNolineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.SerialNolineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SerialNolineEdit.setObjectName("SerialNolineEdit")
        self.horizontalLayout_7.addWidget(self.SerialNolineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.PinlineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.PinlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PinlineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.PinlineEdit.setObjectName("PinlineEdit")
        self.horizontalLayout_8.addWidget(self.PinlineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.indexNoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.indexNoLineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.indexNoLineEdit_2.setObjectName("indexNoLineEdit_2")
        self.horizontalLayout_10.addWidget(self.indexNoLineEdit_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.examYear2Combo = QtWidgets.QComboBox(self.groupBox_3)
        self.examYear2Combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.examYear2Combo.setObjectName("examYear2Combo")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.examYear2Combo.addItem("")
        self.horizontalLayout_9.addWidget(self.examYear2Combo)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.clearBtn = QtWidgets.QPushButton(self.frame)
        self.clearBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_11.addWidget(self.clearBtn)
        self.SubmitBtn = QtWidgets.QPushButton(self.frame)
        self.SubmitBtn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "")
        self.SubmitBtn.setObjectName("SubmitBtn")
        self.horizontalLayout_11.addWidget(self.SubmitBtn)
        self.verticalLayout_8.addWidget(self.frame)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.contentBody)
        self.frame_3.setMinimumSize(QtCore.QSize(292, 0))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgb(255, 44, 58);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_15.addWidget(self.textBrowser)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_4.addWidget(self.contentBody)
        self.contentFooter = QtWidgets.QFrame(self.contentheaderframe)
        self.contentFooter.setMaximumSize(QtCore.QSize(16777215, 28))
        self.contentFooter.setStyleSheet("background-color:rgb(255, 44, 58);")
        self.contentFooter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFooter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFooter.setObjectName("contentFooter")
        self.contentFooter_2 = QtWidgets.QFrame(self.contentFooter)
        self.contentFooter_2.setGeometry(QtCore.QRect(0, 0, 966, 10))
        self.contentFooter_2.setMaximumSize(QtCore.QSize(16777215, 28))
        self.contentFooter_2.setStyleSheet("background-color:rgb(255, 44, 58);")
        self.contentFooter_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFooter_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFooter_2.setObjectName("contentFooter_2")
        self.verticalLayout_4.addWidget(self.contentFooter)
        self.verticalLayout.addWidget(self.contentheaderframe)
        self.SubmitBtn.clicked.connect(self.Checker)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Enter your examination information"))
        self.label_3.setText(_translate("Form", "Index Number:      "))
        self.label_4.setText(_translate("Form", "Examination Type:"))
        self.examTypeCombo.setItemText(0, _translate("Form", "--select your exam type--"))
        self.examTypeCombo.setItemText(1, _translate("Form", "W A S S C E (School)"))
        self.examTypeCombo.setItemText(2, _translate("Form", "W A S S C E (Private)"))
        self.examTypeCombo.setItemText(3, _translate("Form", "S S S C E"))
        self.examTypeCombo.setItemText(4, _translate("Form", "G B C E (MAY/JUN)"))
        self.examTypeCombo.setItemText(5, _translate("Form", "G B C E (NOV/DEC)"))
        self.examTypeCombo.setItemText(6, _translate("Form", "A B C E (MAY/JUN)"))
        self.examTypeCombo.setItemText(7, _translate("Form", "A B C E (NOV/DEC)"))
        self.examTypeCombo.setItemText(8, _translate("Form", "B E C E"))
        self.examTypeCombo.setItemText(9, _translate("Form", "B E C E (Private)"))
        self.label_5.setText(_translate("Form", "Examination Year:"))
        self.examYearCombo.setItemText(0, _translate("Form", "-- select year --"))
        self.examYearCombo.setItemText(1, _translate("Form", "2021"))
        self.examYearCombo.setItemText(2, _translate("Form", "2020"))
        self.examYearCombo.setItemText(3, _translate("Form", "2019"))
        self.examYearCombo.setItemText(4, _translate("Form", "2018"))
        self.examYearCombo.setItemText(5, _translate("Form", "2017"))
        self.examYearCombo.setItemText(6, _translate("Form", "2016"))
        self.examYearCombo.setItemText(7, _translate("Form", "2015"))
        self.examYearCombo.setItemText(8, _translate("Form", "2014"))
        self.examYearCombo.setItemText(9, _translate("Form", "2013"))
        self.examYearCombo.setItemText(10, _translate("Form", "2012"))
        self.examYearCombo.setItemText(11, _translate("Form", "2011"))
        self.examYearCombo.setItemText(12, _translate("Form", "2010"))
        self.examYearCombo.setItemText(13, _translate("Form", "2009"))
        self.examYearCombo.setItemText(14, _translate("Form", "2008"))
        self.examYearCombo.setItemText(15, _translate("Form", "2007"))
        self.examYearCombo.setItemText(16, _translate("Form", "2006"))
        self.examYearCombo.setItemText(17, _translate("Form", "2005"))
        self.examYearCombo.setItemText(18, _translate("Form", "2004"))
        self.examYearCombo.setItemText(19, _translate("Form", "2003"))
        self.examYearCombo.setItemText(20, _translate("Form", "2002"))
        self.examYearCombo.setItemText(21, _translate("Form", "2001"))
        self.examYearCombo.setItemText(22, _translate("Form", "2000"))
        self.examYearCombo.setItemText(23, _translate("Form", "1999"))
        self.examYearCombo.setItemText(24, _translate("Form", "1998"))
        self.examYearCombo.setItemText(25, _translate("Form", "1997"))
        self.examYearCombo.setItemText(26, _translate("Form", "1996"))
        self.examYearCombo.setItemText(27, _translate("Form", "1995"))
        self.examYearCombo.setItemText(28, _translate("Form", "1994"))
        self.examYearCombo.setItemText(29, _translate("Form", "1993"))
        self.examYearCombo.setItemText(30, _translate("Form", "1992"))
        self.examYearCombo.setItemText(31, _translate("Form", "1991"))
        self.examYearCombo.setItemText(32, _translate("Form", "1990"))
        self.groupBox_2.setTitle(
            _translate("Form", "Enter Date Of Birth (WASSCE (PRIVATE) and BECE (SCHOOL) results only!) "))
        self.dayCombo.setItemText(0, _translate("Form", "--day--"))
        self.dayCombo.setItemText(1, _translate("Form", "01"))
        self.dayCombo.setItemText(2, _translate("Form", "02"))
        self.dayCombo.setItemText(3, _translate("Form", "03"))
        self.dayCombo.setItemText(4, _translate("Form", "04"))
        self.dayCombo.setItemText(5, _translate("Form", "05"))
        self.dayCombo.setItemText(6, _translate("Form", "06"))
        self.dayCombo.setItemText(7, _translate("Form", "07"))
        self.dayCombo.setItemText(8, _translate("Form", "08"))
        self.dayCombo.setItemText(9, _translate("Form", "09"))
        self.dayCombo.setItemText(10, _translate("Form", "10"))
        self.dayCombo.setItemText(11, _translate("Form", "11"))
        self.dayCombo.setItemText(12, _translate("Form", "12"))
        self.dayCombo.setItemText(13, _translate("Form", "13"))
        self.dayCombo.setItemText(14, _translate("Form", "14"))
        self.dayCombo.setItemText(15, _translate("Form", "15"))
        self.dayCombo.setItemText(16, _translate("Form", "16"))
        self.dayCombo.setItemText(17, _translate("Form", "17"))
        self.dayCombo.setItemText(18, _translate("Form", "18"))
        self.dayCombo.setItemText(19, _translate("Form", "19"))
        self.dayCombo.setItemText(20, _translate("Form", "20"))
        self.dayCombo.setItemText(21, _translate("Form", "21"))
        self.dayCombo.setItemText(22, _translate("Form", "22"))
        self.dayCombo.setItemText(23, _translate("Form", "23"))
        self.dayCombo.setItemText(24, _translate("Form", "24"))
        self.dayCombo.setItemText(25, _translate("Form", "25"))
        self.dayCombo.setItemText(26, _translate("Form", "26"))
        self.dayCombo.setItemText(27, _translate("Form", "27"))
        self.dayCombo.setItemText(28, _translate("Form", "28"))
        self.dayCombo.setItemText(29, _translate("Form", "29"))
        self.dayCombo.setItemText(30, _translate("Form", "30"))
        self.dayCombo.setItemText(31, _translate("Form", "31"))
        self.monthCombo.setItemText(0, _translate("Form", "--month--"))
        self.monthCombo.setItemText(1, _translate("Form", "JAN"))
        self.monthCombo.setItemText(2, _translate("Form", "FEB"))
        self.monthCombo.setItemText(3, _translate("Form", "MAR"))
        self.monthCombo.setItemText(4, _translate("Form", "APR"))
        self.monthCombo.setItemText(5, _translate("Form", "MAY"))
        self.monthCombo.setItemText(6, _translate("Form", "JUN"))
        self.monthCombo.setItemText(7, _translate("Form", "JUL"))
        self.monthCombo.setItemText(8, _translate("Form", "AUG"))
        self.monthCombo.setItemText(9, _translate("Form", "SEP"))
        self.monthCombo.setItemText(10, _translate("Form", "OCT"))
        self.monthCombo.setItemText(11, _translate("Form", "NOV"))
        self.monthCombo.setItemText(12, _translate("Form", "DEC"))
        self.yearCombo.setItemText(0, _translate("Form", "--year--"))
        self.yearCombo.setItemText(1, _translate("Form", "2012"))
        self.yearCombo.setItemText(2, _translate("Form", "2011"))
        self.yearCombo.setItemText(3, _translate("Form", "2010"))
        self.yearCombo.setItemText(4, _translate("Form", "2009"))
        self.yearCombo.setItemText(5, _translate("Form", "2008"))
        self.yearCombo.setItemText(6, _translate("Form", "2007"))
        self.yearCombo.setItemText(7, _translate("Form", "2006"))
        self.yearCombo.setItemText(8, _translate("Form", "2005"))
        self.yearCombo.setItemText(9, _translate("Form", "2004"))
        self.yearCombo.setItemText(10, _translate("Form", "2003"))
        self.yearCombo.setItemText(11, _translate("Form", "2002"))
        self.yearCombo.setItemText(12, _translate("Form", "2001"))
        self.yearCombo.setItemText(13, _translate("Form", "2000"))
        self.yearCombo.setItemText(14, _translate("Form", "1999"))
        self.yearCombo.setItemText(15, _translate("Form", "1998"))
        self.yearCombo.setItemText(16, _translate("Form", "1997"))
        self.yearCombo.setItemText(17, _translate("Form", "1996"))
        self.yearCombo.setItemText(18, _translate("Form", "1995"))
        self.yearCombo.setItemText(19, _translate("Form", "1994"))
        self.yearCombo.setItemText(20, _translate("Form", "1993"))
        self.yearCombo.setItemText(21, _translate("Form", "1992"))
        self.yearCombo.setItemText(22, _translate("Form", "1991"))
        self.yearCombo.setItemText(23, _translate("Form", "1990"))
        self.yearCombo.setItemText(24, _translate("Form", "1989"))
        self.yearCombo.setItemText(25, _translate("Form", "1988"))
        self.yearCombo.setItemText(26, _translate("Form", "1987"))
        self.yearCombo.setItemText(27, _translate("Form", "1986"))
        self.yearCombo.setItemText(28, _translate("Form", "1985"))
        self.yearCombo.setItemText(29, _translate("Form", "1984"))
        self.yearCombo.setItemText(30, _translate("Form", "1983"))
        self.yearCombo.setItemText(31, _translate("Form", "1982"))
        self.yearCombo.setItemText(32, _translate("Form", "1981"))
        self.yearCombo.setItemText(33, _translate("Form", "1980"))
        self.groupBox_4.setTitle(_translate("Form", "Enter The security information "))
        self.label_6.setText(_translate("Form", "Voucher Serial Number:"))
        self.label_7.setText(_translate("Form", "PIN:"))
        self.groupBox_3.setTitle(_translate("Form", "Confirm your examination information "))
        self.label_8.setText(_translate("Form", "Index Number:"))
        self.label_9.setText(_translate("Form", "Examination Year:"))
        self.examYear2Combo.setItemText(0, _translate("Form", "-- select year --"))
        self.examYear2Combo.setItemText(1, _translate("Form", "2021"))
        self.examYear2Combo.setItemText(2, _translate("Form", "2020"))
        self.examYear2Combo.setItemText(3, _translate("Form", "2019"))
        self.examYear2Combo.setItemText(4, _translate("Form", "2018"))
        self.examYear2Combo.setItemText(5, _translate("Form", "2017"))
        self.examYear2Combo.setItemText(6, _translate("Form", "2016"))
        self.examYear2Combo.setItemText(7, _translate("Form", "2015"))
        self.examYear2Combo.setItemText(8, _translate("Form", "2014"))
        self.examYear2Combo.setItemText(9, _translate("Form", "2013"))
        self.examYear2Combo.setItemText(10, _translate("Form", "2012"))
        self.examYear2Combo.setItemText(11, _translate("Form", "2011"))
        self.examYear2Combo.setItemText(12, _translate("Form", "2010"))
        self.examYear2Combo.setItemText(13, _translate("Form", "2009"))
        self.examYear2Combo.setItemText(14, _translate("Form", "2008"))
        self.examYear2Combo.setItemText(15, _translate("Form", "2007"))
        self.examYear2Combo.setItemText(16, _translate("Form", "2006"))
        self.examYear2Combo.setItemText(17, _translate("Form", "2005"))
        self.examYear2Combo.setItemText(18, _translate("Form", "2004"))
        self.examYear2Combo.setItemText(19, _translate("Form", "2003"))
        self.examYear2Combo.setItemText(20, _translate("Form", "2002"))
        self.examYear2Combo.setItemText(21, _translate("Form", "2001"))
        self.examYear2Combo.setItemText(22, _translate("Form", "2000"))
        self.examYear2Combo.setItemText(23, _translate("Form", "1999"))
        self.examYear2Combo.setItemText(24, _translate("Form", "1998"))
        self.examYear2Combo.setItemText(25, _translate("Form", "1997"))
        self.examYear2Combo.setItemText(26, _translate("Form", "1996"))
        self.examYear2Combo.setItemText(27, _translate("Form", "1995"))
        self.examYear2Combo.setItemText(28, _translate("Form", "1994"))
        self.examYear2Combo.setItemText(29, _translate("Form", "1993"))
        self.examYear2Combo.setItemText(30, _translate("Form", "1992"))
        self.examYear2Combo.setItemText(31, _translate("Form", "1991"))
        self.examYear2Combo.setItemText(32, _translate("Form", "1990"))
        self.clearBtn.setText(_translate("Form", "Clear"))
        self.SubmitBtn.setText(_translate("Form", "Submit"))
        self.label_19.setText(_translate("Form", "USING THE RESULT CHECKER VOUCHER"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Enter your Index Number.</span><span style=\" font-size:medium;\"><br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Select the Type of Examination (e.g.  WASSCE).<br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Select your Examination Year eg. 2003.</span><span style=\" font-size:medium;\"><br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Enter the Serial Number found on the Voucher.</span><span style=\" font-size:medium;\"><br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Enter the 12-digit Personal Identification Number (PIN) on your Voucher eg. 012345678912.</span><span style=\" font-size:medium;\"><br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Confirm your Index Number and Examination Year. This is to ensure that your examination information is correct.</span><span style=\" font-size:medium;\"><br /></span></li>\n"
                                            "<li style=\" font-family:\'Geneva,Arial,Helvetica,sans-serif\'; font-size:8pt; color:#000000;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:20px;\"><span style=\" font-family:\'Geneva, Arial, Helvetica, sans-serif\'; font-size:medium; font-weight:600;\">Click on Submit and wait for the display in the popup window.</span><span style=\" font-size:medium; font-weight:600;\"> This may take several minutes.</span></li></ol></body></html>"))

    def Assigners(self):
        self.IndexNo = self.indexNoLineEdit.text()
        self.ExamYear1 = self.examYearCombo.currentText()
        self.ExamType = self.examTypeCombo.currentText()
        self.Bfday = self.dayCombo.currentText()
        self.BfMonth = self.monthCombo.currentText()
        self.BfYear = self.yearCombo.currentText()
        self.VSerialNo = self.SerialNolineEdit.text()
        self.Pin = self.PinlineEdit.text()
        self.IndexNo2 = self.indexNoLineEdit_2.text()
        self.ExamYear2 = self.examYear2Combo.currentText()
    def Getter(self):
        self.web = webdriver.Chrome(binary_path)
        self.web.get('https://ghana.waecdirect.org/')

    def Checker(self):
        self.Assigners()
        self.Getter()
        # Index number
        if self.IndexNo:
            self.WebIndexNo = self.web.find_element_by_xpath('//*[@id="candid"]').send_keys(self.IndexNo)

        # Exam year
        if self.ExamYear1 == "2021":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[2]').click()
        elif self.ExamYear1 == "2020":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[2]').click()
        elif self.ExamYear1 == "2019":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[3]').click()
        elif self.ExamYear1 == "2018":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[4]').click()
        elif self.ExamYear1 == "2017":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[5]').click()
        elif self.ExamYear1 == "2016":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[6]').click()
        elif self.ExamYear1 == "2015":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[7]').click()
        elif self.ExamYear1 == "2014":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[8]').click()
        elif self.ExamYear1 == "2013":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[9]').click()
        elif self.ExamYear1 == "2012":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[10]').click()
        elif self.ExamYear1 == "2011":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[11]').click()
        elif self.ExamYear1 == "2010":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[12]').click()
        elif self.ExamYear1 == "2009":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[13]').click()
        elif self.ExamYear1 == "2008":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[14]').click()
        elif self.ExamYear1 == "2007":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[15]').click()
        elif self.ExamYear1 == "2006":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[16]').click()
        elif self.ExamYear1 == "2005":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[17]').click()
        elif self.ExamYear1 == "2004":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[18]').click()
        elif self.ExamYear1 == "2003":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[19]').click()
        elif self.ExamYear1 == "2002":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[20]').click()
        elif self.ExamYear1 == "2001":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[21]').click()
        elif self.ExamYear1 == "2000":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[22]').click()
        elif self.ExamYear1 == "1999":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[23]').click()
        elif self.ExamYear1 == "1998":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[24]').click()
        elif self.ExamYear1 == "1997":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[25]').click()
        elif self.ExamYear1 == "1996":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[26]').click()
        elif self.ExamYear1 == "1995":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[27]').click()
        elif self.ExamYear1 == "1994":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[28]').click()
        elif self.ExamYear1 == "1993":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[29]').click()
        elif self.ExamYear1 == "1992":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[30]').click()
        elif self.ExamYear1 == "1991":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[31]').click()
        elif self.ExamYear1 == "1990":
            self.WebExamYear = self.web.find_element_by_xpath('//*[@id="examyear"]/option[32]').click()

        if self.ExamType == "--select your exam type--":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[1]').click()
        elif self.ExamType == "W A S S C E (School)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[2]').click()
        elif self.ExamType == "W A S S C E (Private)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[3]').click()
        elif self.ExamType == "S S S C E":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[4]').click()
        elif self.ExamType == "G B C E (MAY/JUN)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[5]').click()
        elif self.ExamType == "G B C E (NOV/DEC)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[6]').click()
        elif self.ExamType == "A B C E (MAY/JUN)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[7]').click()
        elif self.ExamType == "A B C E (NOV/DEC)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[8]').click()
        elif self.ExamType == "B E C E":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[9]').click()
        elif self.ExamType == "B E C E (Private)":
            self.WebExamType = self.web.find_element_by_xpath('//*[@id="examtype"]/option[10]').click()

        if self.Bfday == "--day--":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[1]').click()
        elif self.Bfday == "01":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[2]').click()
        elif self.Bfday == "02":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[3]').click()
        elif self.Bfday == "03":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[4]').click()
        elif self.Bfday == "04":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[5]').click()
        elif self.Bfday == "05":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[6]').click()
        elif self.Bfday == "06":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[7]').click()
        elif self.Bfday == "07":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[8]').click()
        elif self.Bfday == "08":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[9]').click()
        elif self.Bfday == "09":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[10]').click()
        elif self.Bfday == "10":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[11]').click()
        elif self.Bfday == "11":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[12]').click()
        elif self.Bfday == "12":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[13]').click()
        elif self.Bfday == "13":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[14]').click()
        elif self.Bfday == "14":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[15]').click()
        elif self.Bfday == "15":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[16]').click()
        elif self.Bfday == "16":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[17]').click()
        elif self.Bfday == "17":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[18]').click()
        elif self.Bfday == "18":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[19]').click()
        elif self.Bfday == "19":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[20]').click()
        elif self.Bfday == "20":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[21]').click()
        elif self.Bfday == "21":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[22]').click()
        elif self.Bfday == "22":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[23]').click()
        elif self.Bfday == "23":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[24]').click()
        elif self.Bfday == "24":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[25]').click()
        elif self.Bfday == "25":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[26]').click()
        elif self.Bfday == "26":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[27]').click()
        elif self.Bfday == "27":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[28]').click()
        elif self.Bfday == "28":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[29]').click()
        elif self.Bfday == "29":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[30]').click()
        elif self.Bfday == "30":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[31]').click()
        elif self.Bfday == "31":
            self.WebBfDay = self.web.find_element_by_xpath('//*[@id="cday"]/option[32]').click()

        if self.BfMonth == "JAN":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[2]').click()
        elif self.BfMonth == "FEB":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[3]').click()
        elif self.BfMonth == "MAR":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[4]').click()
        elif self.BfMonth == "APR":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[5]').click()
        elif self.BfMonth == "MAY":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[6]').click()
        elif self.BfMonth == "JUN":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[7]').click()
        elif self.BfMonth == "JUL":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[8]').click()
        elif self.BfMonth == "AUG":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[9]').click()
        elif self.BfMonth == "SEP":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[10]').click()
        elif self.BfMonth == "OCT":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[11]').click()
        elif self.BfMonth == "NOV":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[12]').click()
        elif self.BfMonth == "DEC":
            self.WebBfMonth = self.web.find_element_by_xpath('//*[@id="cmonth"]/option[13]').click()


        if self.BfYear == "--year--":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[1]').click()
        elif self.BfYear == "2012":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[2]').click()
        elif self.BfYear == "2011":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[3]').click()
        elif self.BfYear == "2010":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[4]').click()
        elif self.BfYear == "2009":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[5]').click()
        elif self.BfYear == "2008":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[6]').click()
        elif self.BfYear == "2007":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[7]').click()
        elif self.BfYear == "2006":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[8]').click()
        elif self.BfYear == "2005":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[9]').click()
        elif self.BfYear == "2004":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[10]').click()
        elif self.BfYear == "2003":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[11]').click()
        elif self.BfYear == "2002":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[12]').click()
        elif self.BfYear == "2001":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[13]').click()
        elif self.BfYear == "2000":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[14]').click()
        elif self.BfYear == "1999":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[15]').click()
        elif self.BfYear == "1998":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[16]').click()
        elif self.BfYear == "1997":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[17]').click()
        elif self.BfYear == "1996":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[18]').click()
        elif self.BfYear == "1995":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[19]').click()
        elif self.BfYear == "1994":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[20]').click()
        elif self.BfYear == "1993":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[21]').click()
        elif self.BfYear == "1992":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[22]').click()
        elif self.BfYear == "1991":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[23]').click()
        elif self.BfYear == "1990":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[24]').click()
        elif self.BfYear == "1989":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[25]').click()
        elif self.BfYear == "1988":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[26]').click()
        elif self.BfYear == "1987":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[27]').click()
        elif self.BfYear == "1986":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[28]').click()
        elif self.BfYear == "1985":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[29]').click()
        elif self.BfYear == "1984":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[30]').click()
        elif self.BfYear == "1983":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[31]').click()
        elif self.BfYear == "1982":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[32]').click()
        elif self.BfYear == "1981":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[33]').click()
        elif self.BfYear == "1980":
            self.WebBfYear = self.web.find_element_by_xpath('//*[@id="cyear"]/option[34]').click()

        if self.VSerialNo:
            self.WebVSerialNo = self.web.find_element_by_xpath('//*[@id="serial"]').send_keys(self.VSerialNo)

        if self.Pin:
            self.WebPin = self.web.find_element_by_xpath('//*[@id="pin"]').send_keys(self.Pin)

        if self.IndexNo2:
            self.WebIndexNo2 = self.web.find_element_by_xpath('//*[@id="ccandid"]').send_keys(self.IndexNo2)



        if self.ExamYear2 == "2021":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[2]').click()
        elif self.ExamYear2 == "2020":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[2]').click()
        elif self.ExamYear2 == "2019":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[3]').click()
        elif self.ExamYear2 == "2018":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[4]').click()
        elif self.ExamYear2 == "2017":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[5]').click()
        elif self.ExamYear2 == "2016":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[6]').click()
        elif self.ExamYear2 == "2015":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[7]').click()
        elif self.ExamYear2 == "2014":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[8]').click()
        elif self.ExamYear2 == "2013":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[9]').click()
        elif self.ExamYear2 == "2012":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[10]').click()
        elif self.ExamYear2 == "2011":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[11]').click()
        elif self.ExamYear2 == "2010":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[12]').click()
        elif self.ExamYear2 == "2009":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[13]').click()
        elif self.ExamYear2 == "2008":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[14]').click()
        elif self.ExamYear2 == "2007":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[15]').click()
        elif self.ExamYear2 == "2006":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[16]').click()
        elif self.ExamYear2 == "2005":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[17]').click()
        elif self.ExamYear2 == "2004":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[18]').click()
        elif self.ExamYear2 == "2003":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[19]').click()
        elif self.ExamYear2 == "2002":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[20]').click()
        elif self.ExamYear2 == "2001":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[21]').click()
        elif self.ExamYear2 == "2000":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[22]').click()
        elif self.ExamYear2 == "1999":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[23]').click()
        elif self.ExamYear2 == "1998":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[24]').click()
        elif self.ExamYear2 == "1997":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[25]').click()
        elif self.ExamYear2 == "1996":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[26]').click()
        elif self.ExamYear2 == "1995":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[27]').click()
        elif self.ExamYear2 == "1994":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[28]').click()
        elif self.ExamYear2 == "1993":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[29]').click()
        elif self.ExamYear2 == "1992":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[30]').click()
        elif self.ExamYear2 == "1991":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[31]').click()
        elif self.ExamYear2 == "1990":
            self.WebExamYear2 = self.web.find_element_by_xpath('//*[@id="select"]/option[32]').click()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
