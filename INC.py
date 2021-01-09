
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from model import Model
from print import print_allpdf
import xlsxwriter as xls


class ITaxSlab(QDialog):
    def __init__(self, parent=None):
        super(ITaxSlab, self).__init__(parent)

        self.resize(500, 400)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/incometax.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)
        
        self.setWindowIcon(icon)

        tabWidget = QTabWidget()
        tabWidget.setGeometry(QtCore.QRect(10, 10, 500, 400))
        
        tabWidget.setObjectName("tabWidget")

        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")

        self.comboBox_sel_slab = QtWidgets.QComboBox(self.tab0)
        self.comboBox_sel_slab.setGeometry(QtCore.QRect(20, 30, 200, 31))
        #self.comboBox_sel_slab.setStyleSheet("color: #000000;")
        self.comboBox_sel_slab.setObjectName("comboBox_sel_slab")
        self.comboBox_sel_slab.setToolTip("Please Choose any one.")
        self.itm = ['','Below 60 years','60-80 years','Above 80 years','surcharges']
        self.comboBox_sel_slab.addItems(self.itm)


        
        self.tableWidget = QTableWidget(5, 2,self.tab0)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 400, 200))
        #self.tableWidget.setStyleSheet("color: #000000")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        
        self.comboBox_sel_slab.currentTextChanged.connect(self.combo_changed)
        

        tabWidget.addTab(self.tab0 ,"Slab for fy(2018-19)")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.comboBox_sel_slab1 = QtWidgets.QComboBox(self.tab1)
        self.comboBox_sel_slab1.setGeometry(QtCore.QRect(20, 30, 200, 31))
        self.comboBox_sel_slab1.setStyleSheet("background-color:#ffffff, color: #000000;")
        self.comboBox_sel_slab1.setObjectName("comboBox_sel_slab1")
        self.comboBox_sel_slab1.setToolTip("Please Choose any one.")
        self.itm1 = ['','Below 60 years','60-80 years','Above 80 years','surcharges']
        self.comboBox_sel_slab1.addItems(self.itm1)
        
        self.tableWidget1 = QTableWidget(5, 2,self.tab1)
        self.tableWidget1.setGeometry(QtCore.QRect(20, 100, 400, 200))
        self.tableWidget1.setStyleSheet("background-color:#ffffff, color: #000000")
        self.tableWidget1.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.comboBox_sel_slab1.currentTextChanged.connect(self.combo_changed1)

        tabWidget.addTab(self.tab1 ,"Slab for fy (2019-20)")

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.comboBox_sel_slab2 = QtWidgets.QComboBox(self.tab2)
        self.comboBox_sel_slab2.setGeometry(QtCore.QRect(20, 30, 200, 31))
        self.comboBox_sel_slab2.setStyleSheet("background-color:#ffffff, color: #000000;")
        self.comboBox_sel_slab2.setObjectName("comboBox_sel_slab2")
        self.comboBox_sel_slab2.setToolTip("Please Choose any one.")
        self.itm2 = ['','incometax slabs','surcharges']
        self.comboBox_sel_slab2.addItems(self.itm2)
        
        self.tableWidget2 = QTableWidget(7, 2,self.tab2)
        self.tableWidget2.setGeometry(QtCore.QRect(20, 100, 400, 200))
        self.tableWidget2.setStyleSheet("background-color:#ffffff, color: #000000")
        self.tableWidget2.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.comboBox_sel_slab2.currentTextChanged.connect(self.combo_changed2)
        tabWidget.addTab(self.tab2 ,"Slab for fy (2020-21)")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)

        buttonBox.accepted.connect(self.accept)
        

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Income Tax Slabs")

    
        
    def populateTableWidget(self,tableWidget):

        if self.comboBox_sel_slab.currentText() == 'Below 60 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 2.5 L", "NIL"),
                ("2.5 to 5L", "5% (No tax rebate u/s 87A)"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("",""),
                
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab.currentText() == '60-80 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 3 L", "NIL"),
                ("3 to 5L", "5% (No tax rebate u/s 87A)"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("",""),
                
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab.currentText() == 'Above 80 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 5 L", "NIL"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("",""),
                ("",""),
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab.currentText() == 'surcharges':

            headerLabels = ("Total Income", "Rate of surcharge")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("50 to 1 Cr", "10%  applicable on income tax"),
                ("Exceed 1 Cr", "15%  applicable on income tax"),
                ("1 Cr to 10 Cr", "7%  applicable on income tax"),
                ("Exceed 10 Cr", "12%  applicable on income tax"),
                ("Health & Edu Cess", "4%  applicable on income tax"),
            )

        if self.comboBox_sel_slab.currentText() == '':
            headerLabels = ("", "")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("",""),
                ("",""),
                ("",""),
                ("",""),
                ("",""),
            )

            tableWidget.resizeColumnsToContents()
            tableWidget.show()

        for row, (income ,rate) in enumerate(staticData):
            item0 = QTableWidgetItem(income)
            item1 = QTableWidgetItem(rate)
            
            tableWidget.setItem(row, 0, item0)
            tableWidget.setItem(row, 1, item1)

    def populateTableWidget2(self,tableWidget):

        if self.comboBox_sel_slab2.currentText() == 'incometax slabs':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 2.5 L", "NIL"),
                ("2.5 to 5L", "5% (No tax rebate u/s 87A)"),
                ("5 to 7.5L", "10%"),
                ("7.5 to 10L", "15%"),
                ("10 to 12.5L", "20%"),
                ("12.5 to 15L", "25%"),
                ("Above 15L", "30%"),
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab2.currentText() == 'surcharges':

            headerLabels = ("Total Income", "Rate of surcharge")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("50 to 1 Cr", "10%  applicable on income tax"),
                ("1 to 2 Cr", "15%  applicable on income tax"),
                ("2 Cr to 5 Cr", "25%  applicable on income tax"),
                ("Exceed 5 Cr", "37%  applicable on income tax"),
                ("Health & Edu Cess", "4%  applicable on income tax"),
                ("",""),
                ("",""),
            )

        if self.comboBox_sel_slab2.currentText() == '':
            headerLabels = ("", "")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("",""),
                ("",""),
                ("",""),
                ("",""),
                ("",""),
                ("",""),
                ("",""),
            )

            tableWidget.resizeColumnsToContents()
            tableWidget.show()

        for row, (income ,rate) in enumerate(staticData):
            item0 = QTableWidgetItem(income)
            item1 = QTableWidgetItem(rate)
            
            tableWidget.setItem(row, 0, item0)
            tableWidget.setItem(row, 1, item1)

    def populateTableWidget1(self,tableWidget):

        if self.comboBox_sel_slab1.currentText() == 'Below 60 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 2.5 L", "NIL"),
                ("2.5 to 5L", "5% (No tax rebate u/s 87A)"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("","")
                
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab1.currentText() == '60-80 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 3 L", "NIL"),
                ("3 to 5L", "5% (No tax rebate u/s 87A)"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("",""),
                ("","")
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab1.currentText() == 'Above 80 years':

            headerLabels = ("Income in (Lakhs)", "Tax Rate")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("upto 5 L", "NIL"),
                ("5 to 10L", "20%"),
                ("Above 10L", "30%"),
                ("",""),
                ("","")
            )
            tableWidget.resizeColumnsToContents()
            tableWidget.show()


        if self.comboBox_sel_slab1.currentText() == 'surcharges':

            headerLabels = ("Total Income", "Rate of surcharge")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("50 to 1 Cr", "10%  applicable on income tax"),
                ("1 to 2 Cr", "15%  applicable on income tax"),
                ("2 Cr to 5 Cr", "25%  applicable on income tax"),
                ("Exceed 5 Cr", "37%  applicable on income tax"),
                ("Health & Edu Cess", "4%  applicable on income tax"),
            )

        if self.comboBox_sel_slab1.currentText() == '':
            headerLabels = ("", "")
            tableWidget.setHorizontalHeaderLabels(headerLabels)

            staticData = (
                ("",""),
                ("",""),
                ("",""),
                ("",""),
                ("","")
                
            )

            tableWidget.resizeColumnsToContents()
            tableWidget.show()

        for row, (income ,rate) in enumerate(staticData):
            item0 = QTableWidgetItem(income)
            item1 = QTableWidgetItem(rate)
            
            tableWidget.setItem(row, 0, item0)
            tableWidget.setItem(row, 1, item1)

    def combo_changed(self):
        self.populateTableWidget(self.tableWidget)

    def combo_changed1(self):
        self.populateTableWidget1(self.tableWidget1)

    def combo_changed2(self):
        self.populateTableWidget2(self.tableWidget2)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 586)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/incometax.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        MainWindow.setStyleSheet(style)
        MainWindow.setWindowIcon(icon)
        MainWindow.setMinimumSize(QtCore.QSize(844, 586))
        MainWindow.setMaximumSize(QtCore.QSize(844, 586))

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.vLay = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vLay.setObjectName("vLay")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 824, 576))
        self.tabWidget.setObjectName("tabWidget")

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// Start  tab ///////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////

        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")

        self.label_inc = QtWidgets.QLabel(self.tab0)
        self.label_inc.setGeometry(QtCore.QRect(200, 100, 451, 30))
        font0 = QtGui.QFont()
        font0.setPointSize(20)
        font0.setFamily("Arial Black")
        self.label_inc.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_inc.setFont(font0)
        self.label_inc.setObjectName("label_inc")

        self.label_inc2 = QtWidgets.QLabel(self.tab0)
        self.label_inc2.setGeometry(QtCore.QRect(200, 135, 451, 200))
        font1 = QtGui.QFont()
        font1.setPointSize(12)
        font1.setFamily("Arial")
        self.label_inc2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_inc2.setFont(font1)
        self.label_inc2.setObjectName("label_inc2")

        self.pushButton_Sr = QtWidgets.QPushButton(self.tab0)
        self.pushButton_Sr.setGeometry(QtCore.QRect(300, 300, 199, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sr.setFont(font)
        self.pushButton_Sr.clicked.connect(self.Start)
        self.pushButton_Sr.setObjectName("pushButton_Sr")

        self.tabWidget.addTab(self.tab0, "")

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// Login tab ///////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.groupBox_L1 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_L1.setGeometry(QtCore.QRect(40, 10, 251, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_L1.setFont(font)
        #self.groupBox.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.groupBox_L1.setObjectName("groupBox_L1")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_L1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 201, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.label_Username_L1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Username_L1.setFont(font)
        self.label_Username_L1.setObjectName("label_Username_L1")
        self.verticalLayout.addWidget(self.label_Username_L1)

        self.lineEdit_Username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Username.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-color: rgb(255, 255, 255);")
        self.lineEdit_Username.setObjectName("lineEdit_Username")
        self.lineEdit_Username.setToolTip("Enter valid username atleast 5 characters.")
        self.verticalLayout.addWidget(self.lineEdit_Username)

        self.label_Password = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Password.setFont(font)
        self.label_Password.setObjectName("label_Password")
        self.verticalLayout.addWidget(self.label_Password)

        self.lineEdit_Password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_Password.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-color: rgb(255, 255, 255);")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setToolTip("Enter valid password atleast 8 characters & 1 alphabet is reqiured.")
        self.verticalLayout.addWidget(self.lineEdit_Password)

        self.checkBox_L = QtWidgets.QCheckBox(self.groupBox_L1)
        self.checkBox_L.setGeometry(QtCore.QRect(20, 120, 106, 16))
        self.checkBox_L.setObjectName("checkBox_L")
        self.checkBox_L.setText("Show Password")
        self.checkBox_L.setStyleSheet("color: #ffffff;")
        self.checkBox_L.setChecked(False)
        self.checkBox_L.toggled.connect(self.checkbox_toggled)
        self.checkBox_L.setToolTip("click on it for show & hide password.")


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.pushButton_Login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Login.setFont(font)
        #self.pushButton_Login.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton_Login.setObjectName("pushButton")
        

        self.verticalLayout.addWidget(self.pushButton_Login)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)


        #////////////////////////////////////////////////////////////////


        self.groupBox_L2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_L2.setGeometry(QtCore.QRect(380, 10, 401, 491))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_L2.setFont(font)
        #self.groupBox_2.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255);")
        self.groupBox_L2.setObjectName("groupBox_L2")



        self.label_Firstname = QtWidgets.QLabel(self.groupBox_L2)
        self.label_Firstname.setGeometry(QtCore.QRect(20, 30, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Firstname.setFont(font)
        self.label_Firstname.setObjectName("label_Firstname")


        self.label_Lastname = QtWidgets.QLabel(self.groupBox_L2)
        self.label_Lastname.setGeometry(QtCore.QRect(210, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Lastname.setFont(font)
        self.label_Lastname.setObjectName("label_Lastname")


        self.lineEdit_Firstname = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_Firstname.setGeometry(QtCore.QRect(20, 50, 161, 20))
        self.lineEdit_Firstname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-color: rgb(255, 255, 255);")
        self.lineEdit_Firstname.setObjectName("lineEdit_Firstname")
        self.lineEdit_Firstname.setToolTip("Please enter your First Name")

        self.lineEdit_LastName = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(210, 50, 171, 20))
        self.lineEdit_LastName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-color: rgb(255, 255, 255);")
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.lineEdit_LastName.setToolTip("Please enter your Last Name")


        self.label_UserN = QtWidgets.QLabel(self.groupBox_L2)
        self.label_UserN.setGeometry(QtCore.QRect(20, 90, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_UserN.setFont(font)

        self.label_UserN.setObjectName("label_UserN")


        self.lineEdit_UserN = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_UserN.setGeometry(QtCore.QRect(20, 110, 161, 20))
        self.lineEdit_UserN.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_UserN.setObjectName("lineEdit_UserN")
        self.lineEdit_UserN.setToolTip("Please enter unique Username atleast 5 characters.")

        self.label_Passd = QtWidgets.QLabel(self.groupBox_L2)
        self.label_Passd.setGeometry(QtCore.QRect(20, 150, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Passd.setFont(font)
        self.label_Passd.setObjectName("label_Passd")


        self.lineEdit_Passd = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_Passd.setGeometry(QtCore.QRect(20, 170, 161, 20))
        self.lineEdit_Passd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_Passd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Passd.setObjectName("lineEdit_Passd")
        self.lineEdit_Passd.setToolTip("Please enter unique password atleast 8 characters and one alphabet is reqiured.")

        self.checkBox_S1 = QtWidgets.QCheckBox(self.groupBox_L2)
        self.checkBox_S1.setGeometry(QtCore.QRect(20, 192, 106, 16))
        self.checkBox_S1.setObjectName("checkBox_S1")
        self.checkBox_S1.setChecked(False)
        self.checkBox_S1.setText("Show Password")
        self.checkBox_S1.setStyleSheet("color: #ffffff;")
        self.checkBox_S1.toggled.connect(self.checkbox_toggled)
        self.checkBox_S1.setToolTip("click on it for show & hide password.")


        self.label_Repassd = QtWidgets.QLabel(self.groupBox_L2)
        self.label_Repassd.setGeometry(QtCore.QRect(210, 150, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Repassd.setFont(font)
        self.label_Repassd.setObjectName("label_Repassd")


        self.lineEdit_Repassd = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_Repassd.setGeometry(QtCore.QRect(210, 170, 171, 20))
        self.lineEdit_Repassd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_Repassd.setFrame(True)
        self.lineEdit_Repassd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Repassd.setObjectName("lineEdit_Repassd")
        self.lineEdit_Repassd.setToolTip("Re-type your password.")


        self.checkBox_S2 = QtWidgets.QCheckBox(self.groupBox_L2)
        self.checkBox_S2.setGeometry(QtCore.QRect(210, 193, 106, 16))
        self.checkBox_S2.setObjectName("checkBox_S2")
        self.checkBox_S2.setChecked(False)
        self.checkBox_S2.setText("Show Password")
        self.checkBox_S2.setStyleSheet("color: #ffffff;")
        self.checkBox_S2.toggled.connect(self.checkbox_toggled)
        self.checkBox_S2.setToolTip("click on it for show & hide password.")



        self.label_DOB = QtWidgets.QLabel(self.groupBox_L2)
        self.label_DOB.setGeometry(QtCore.QRect(20, 222, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_DOB.setFont(font)
        self.label_DOB.setObjectName("label_DOB")


        self.comboBox_date = QtWidgets.QComboBox(self.groupBox_L2)
        self.comboBox_date.setGeometry(QtCore.QRect(140, 222, 61, 21))
        self.comboBox_date.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.494591, y1:1, x2:0.545727, y2:0.285, stop:0 rgba(191, 121, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.comboBox_date.setObjectName("comboBox_date")
        self.comboBox_date.setToolTip("Please Choose Date of your DOB.")


        self.comboBox_month = QtWidgets.QComboBox(self.groupBox_L2)
        self.comboBox_month.setGeometry(QtCore.QRect(210, 222, 61, 21))
        self.comboBox_month.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.494591, y1:1, x2:0.545727, y2:0.285, stop:0 rgba(191, 121, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.comboBox_month.setObjectName("comboBox_month")
        self.comboBox_month.setToolTip("Please Choose Month of your DOB.")



        self.comboBox_year = QtWidgets.QComboBox(self.groupBox_L2)
        self.comboBox_year.setGeometry(QtCore.QRect(280, 222, 101, 21))
        self.comboBox_year.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.494591, y1:1, x2:0.545727, y2:0.285, stop:0 rgba(191, 121, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.comboBox_year.setObjectName("comboBox_year")
        self.comboBox_year.setToolTip("Please Choose Year of your DOB.")


        self.label_SQ = QtWidgets.QLabel(self.groupBox_L2)
        self.label_SQ.setGeometry(QtCore.QRect(20, 250, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SQ.setFont(font)
        self.label_SQ.setObjectName("label_SQ")
        

        self.lineEdit_SA = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_SA.setGeometry(QtCore.QRect(20, 340, 361, 20))
        self.lineEdit_SA.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_SA.setObjectName("lineEdit_SA")
        self.lineEdit_SA.setToolTip("Please Enter your Answer of selected Security Question.")


        self.label_SA = QtWidgets.QLabel(self.groupBox_L2)
        self.label_SA.setGeometry(QtCore.QRect(20, 320, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SA.setFont(font)
        self.label_SA.setObjectName("label_SA")


        self.label_PAN_L = QtWidgets.QLabel(self.groupBox_L2)
        self.label_PAN_L.setGeometry(QtCore.QRect(20, 380, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PAN_L.setFont(font)
        self.label_PAN_L.setObjectName("label_PAN_L")


        self.label_MOB = QtWidgets.QLabel(self.groupBox_L2)
        self.label_MOB.setGeometry(QtCore.QRect(200, 380, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_MOB.setFont(font)
        self.label_MOB.setObjectName("label_MOB")


        self.lineEdit_PAN_Inc = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_PAN_Inc.setGeometry(QtCore.QRect(20, 410, 161, 20))
        self.lineEdit_PAN_Inc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_PAN_Inc.setObjectName("lineEdit_PAN_Inc")
        self.lineEdit_PAN_Inc.setToolTip("Please enter your PAN Card Number.")


        self.lineEdit_MOB = QtWidgets.QLineEdit(self.groupBox_L2)
        self.lineEdit_MOB.setGeometry(QtCore.QRect(200, 410, 181, 20))
        self.lineEdit_MOB.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);")
        self.lineEdit_MOB.setObjectName("lineEdit_MOB")
        self.lineEdit_MOB.setToolTip("Please enter your Mobile Number.")


        self.comboBox_SQ = QtWidgets.QComboBox(self.groupBox_L2)
        self.comboBox_SQ.setGeometry(QtCore.QRect(20, 280, 361, 21))
        self.comboBox_SQ.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.494591, y1:1, x2:0.545727, y2:0.285, stop:0 rgba(191, 121, 79, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.comboBox_SQ.setObjectName("comboBox_SQ")
        self.comboBox_SQ.setToolTip("Please Choose any Security Question.")


        self.pushButton_Signup = QtWidgets.QPushButton(self.groupBox_L2)
        self.pushButton_Signup.setGeometry(QtCore.QRect(90, 450, 199, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Signup.setFont(font)
        #self.pushButton_Signup.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton_Signup.setObjectName("pushButton_Signup")


        self.groupBox_L3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_L3.setGeometry(QtCore.QRect(40, 220, 251, 281))
        self.groupBox_L3.setStyleSheet("color: #000000; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.groupBox_L3.setTitle("")
        self.groupBox_L3.setObjectName("groupBox_L3")


        self.label_3 = QtWidgets.QLabel(self.groupBox_L3)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")


        self.label_14 = QtWidgets.QLabel(self.groupBox_L3)
        self.label_14.setGeometry(QtCore.QRect(30, 70, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")


        #////////////////////////////////////////////////////////////////

       
        self.question = ['what is your childhood nickname?',
        'what is your first teacher name?', 
        'what is your school name?',
        'what is your first friend name?',
        'what is your favourite place in the world?']
        self.comboBox_SQ.addItems(self.question)

        self.date = ['01','02','03','04','05','06','07','08','09','10',
        '11','12','13','14','15','16','17','18','19','20',
        '21','22','23','24','25','26','27','28','29','30',
        '31']
        self.comboBox_date.addItems(self.date)

        self.month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11','12']
        self.comboBox_month.addItems(self.month)

        self.year = ['1931','1932','1933','1934','1935','1936','1937','1938','1939','1940',
        '1941','1942','1943','1944','1945','1946','1947','1948','1949','1950',
        '1951','1952','1953','1954','1955','1956','1957','1958','1959','1960',
        '1961','1962','1963','1964','1965','1966','1967','1968','1969','1970',
        '1971','1972','1973','1974','1975','1976','1977','1978','1979','1980',
        '1981','1982','1983','1984','1985','1986','1987','1988','1989','1990',
        '1991','1992','1993','1994','1995','1996','1997','1998','1999','2000',
        '2001', '2002']
        self.comboBox_year.addItems(self.year)

        
        self.tabWidget.addTab(self.tab, "")
        
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #//////////////////////////////////////  INCOME tax tab   ////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 801, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")

        self.label_User = QtWidgets.QLabel(self.groupBox)
        self.label_User.setGeometry(QtCore.QRect(10, 50, 171, 41))
        self.label_User.setFrameShape(QtWidgets.QFrame.Box)
        self.label_User.setText("")
        self.label_User.setAlignment(QtCore.Qt.AlignCenter)
        self.label_User.setObjectName("label_User")


        self.label_Username = QtWidgets.QLabel(self.groupBox)
        self.label_Username.setGeometry(QtCore.QRect(10, 30, 171, 21))
        self.label_Username.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Username.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Username.setObjectName("label_Username")


        self.label_Name = QtWidgets.QLabel(self.groupBox)
        self.label_Name.setGeometry(QtCore.QRect(190, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_Name.setFont(font)
        self.label_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Name.setObjectName("label_Name")

        self.label_PAN = QtWidgets.QLabel(self.groupBox)
        self.label_PAN.setGeometry(QtCore.QRect(450, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_PAN.setFont(font)
        self.label_PAN.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PAN.setObjectName("label_PAN")


        self.lineEdit_Name = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Name.setGeometry(QtCore.QRect(240, 24, 201, 25))
        self.lineEdit_Name.setAutoFillBackground(True)
        self.lineEdit_Name.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.lineEdit_Name.setFrame(True)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.lineEdit_Name.setToolTip("Please enter verified Name by the PAN card.")

        self.lineEdit_PAN = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_PAN.setGeometry(QtCore.QRect(590, 24, 191, 25))
        self.lineEdit_PAN.setAutoFillBackground(True)
        self.lineEdit_PAN.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.lineEdit_PAN.setFrame(True)
        self.lineEdit_PAN.setObjectName("lineEdit_PAN")
        self.lineEdit_PAN.setToolTip("Please enter verified PAN card Number.")

        self.label_Age = QtWidgets.QLabel(self.groupBox)
        self.label_Age.setGeometry(QtCore.QRect(180, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_Age.setFont(font)
        self.label_Age.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Age.setObjectName("label_Age")

        self.lineEdit_Age = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Age.setGeometry(QtCore.QRect(240, 64, 201, 25))
        self.lineEdit_Age.setAutoFillBackground(True)
        self.lineEdit_Age.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(0, 0, 0);")
        self.lineEdit_Age.setFrame(True)
        self.lineEdit_Age.setObjectName("lineEdit_Age")
        self.lineEdit_Age.setToolTip("Please enter verified Age by the PAN card.")

        self.label_FY = QtWidgets.QLabel(self.groupBox)
        self.label_FY.setGeometry(QtCore.QRect(470, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_FY.setFont(font)
        self.label_FY.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FY.setObjectName("label_FY")


        self.comboBox_FY = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_FY.setGeometry(QtCore.QRect(591, 66, 191, 21))
        self.comboBox_FY.setStyleSheet("color: rgb(0,0,0);\n"
"background-color: qlineargradient(spread:reflect, x1:0.494591, y1:1, x2:0.545727, y2:0.285, stop:0 rgba(191, 121, 79, 255), stop:1 rgba(255, 255, 255, 255));")
        self.comboBox_FY.setObjectName("comboBox_FY")
        self.comboBox_FY.setToolTip("Choose any Financial Year.")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")


        self.lineEdit_i1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i1.setGeometry(QtCore.QRect(240, 24, 141, 25))
        self.lineEdit_i1.setAutoFillBackground(False)
        self.lineEdit_i1.setFrame(True)
        self.lineEdit_i1.setObjectName("lineEdit_i1")
        self.lineEdit_i1.setToolTip("Please Enter the Annual Salary\n if it's have else enter 0.")


        self.lineEdit_i2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i2.setGeometry(QtCore.QRect(240, 50, 141, 25))
        self.lineEdit_i2.setAutoFillBackground(False)
        self.lineEdit_i2.setFrame(True)
        self.lineEdit_i2.setObjectName("lineEdit_i2")
        self.lineEdit_i2.setToolTip("Please Enter all the Exemption from Salary\n if it's have else enter 0.")


        self.lineEdit_i3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i3.setGeometry(QtCore.QRect(240, 80, 141, 25))
        self.lineEdit_i3.setAutoFillBackground(False)
        self.lineEdit_i3.setFrame(True)
        self.lineEdit_i3.setObjectName("lineEdit_i3")
        self.lineEdit_i3.setToolTip("Please Enter the Intrest from Salary\n if it's have else enter 0.")

        self.lineEdit_i4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i4.setGeometry(QtCore.QRect(240, 110, 141, 25))
        self.lineEdit_i4.setAutoFillBackground(False)
        self.lineEdit_i4.setFrame(True)
        self.lineEdit_i4.setObjectName("lineEdit_i4")
        self.lineEdit_i4.setToolTip("Please Enter all Annual incomes\n if it's have else enter 0.")

        self.lineEdit_i5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i5.setGeometry(QtCore.QRect(240, 140, 141, 25))
        self.lineEdit_i5.setAutoFillBackground(False)
        self.lineEdit_i5.setFrame(True)
        self.lineEdit_i5.setObjectName("lineEdit_i5")
        self.lineEdit_i5.setToolTip("Please Enter the Intrest paid at home loan in the given finnancial year\n if it's have else enter 0.")

        self.lineEdit_i6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i6.setGeometry(QtCore.QRect(240, 170, 141, 25))
        self.lineEdit_i6.setAutoFillBackground(False)
        self.lineEdit_i6.setFrame(True)
        self.lineEdit_i6.setObjectName("lineEdit_i6")
        self.lineEdit_i6.setToolTip("Please Enter all rental incomes during finnancial year\n if it's have else enter 0.")


        self.lineEdit_i7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_i7.setGeometry(QtCore.QRect(240, 200, 141, 25))
        self.lineEdit_i7.setAutoFillBackground(False)
        self.lineEdit_i7.setFrame(True)
        self.lineEdit_i7.setObjectName("lineEdit_i7")
        self.lineEdit_i7.setToolTip("Please Enter Income paid on Bank Loan\n except Home Loan\n if it's have else enter 0.")

        self.label_i1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i1.setGeometry(QtCore.QRect(10, 24, 221, 20))
        self.label_i1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i1.setObjectName("label_i1")


        self.label_i2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i2.setGeometry(QtCore.QRect(10, 50, 221, 21))
        self.label_i2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i2.setObjectName("label_i2")


        self.label_i3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i3.setGeometry(QtCore.QRect(10, 80, 221, 21))
        self.label_i3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i3.setObjectName("label_i3")


        self.label_i4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i4.setGeometry(QtCore.QRect(10, 110, 221, 21))
        self.label_i4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i4.setObjectName("label_i4")


        self.label_i5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i5.setGeometry(QtCore.QRect(10, 140, 221, 21))
        self.label_i5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i5.setObjectName("label_i5")


        self.label_i6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i6.setGeometry(QtCore.QRect(10, 170, 221, 21))
        self.label_i6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i6.setObjectName("label_i6")


        self.label_i7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_i7.setGeometry(QtCore.QRect(10, 200, 221, 21))
        self.label_i7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_i7.setObjectName("label_i7")


        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 110, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")

        self.lineEdit_d1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d1.setGeometry(QtCore.QRect(240, 24, 141, 25))
        self.lineEdit_d1.setAutoFillBackground(False)
        self.lineEdit_d1.setFrame(True)
        self.lineEdit_d1.setObjectName("lineEdit_d1")
        self.lineEdit_d1.setToolTip("Please Enter value of Deductions on Investment in PPF\n Life Insurance Premium\n Children's Tution fees \n if it's have else enter 0.")

        self.lineEdit_d2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d2.setGeometry(QtCore.QRect(240, 50, 141, 25))
        self.lineEdit_d2.setAutoFillBackground(False)
        self.lineEdit_d2.setFrame(True)
        self.lineEdit_d2.setObjectName("lineEdit_d2")
        self.lineEdit_d2.setToolTip("Please Enter value of Intrest income from saving Account\n if it's have else enter 0.")

        self.lineEdit_d3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d3.setGeometry(QtCore.QRect(240, 80, 141, 25))
        self.lineEdit_d3.setAutoFillBackground(False)
        self.lineEdit_d3.setFrame(True)
        self.lineEdit_d3.setObjectName("lineEdit_d3")
        self.lineEdit_d3.setToolTip("Please Enter value of Medical Insurance- self, spouce, Children,\n Parents more than 60 years \n if it's have else enter 0.")

        self.lineEdit_d4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d4.setGeometry(QtCore.QRect(240, 110, 141, 25))
        self.lineEdit_d4.setAutoFillBackground(False)
        self.lineEdit_d4.setFrame(True)
        self.lineEdit_d4.setObjectName("lineEdit_d4")
        self.lineEdit_d4.setToolTip("Please Enter value of Deduction for\n Donations towards social causes \n if it's have else enter 0.")


        self.lineEdit_d5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d5.setGeometry(QtCore.QRect(240, 140, 141, 25))
        self.lineEdit_d5.setAutoFillBackground(False)
        self.lineEdit_d5.setFrame(True)
        self.lineEdit_d5.setObjectName("lineEdit_d5")
        self.lineEdit_d5.setToolTip("Please Enter value of Deduction for the Intrest on Education Loan\n if it's have else enter 0.")

        self.lineEdit_d6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d6.setGeometry(QtCore.QRect(240, 170, 141, 25))
        self.lineEdit_d6.setAutoFillBackground(False)
        self.lineEdit_d6.setFrame(True)
        self.lineEdit_d6.setObjectName("lineEdit_d6")
        self.lineEdit_d6.setToolTip("Please Enter the Deduction for Intrest on Home loan\n if it's have else enter 0.")

        self.lineEdit_d7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_d7.setGeometry(QtCore.QRect(240, 200, 141, 25))
        self.lineEdit_d7.setAutoFillBackground(False)
        self.lineEdit_d7.setFrame(True)
        self.lineEdit_d7.setObjectName("lineEdit_d7")
        self.lineEdit_d7.setToolTip("Please Enter value of Deduction for \n Employee's contribution to NPS Account \n if it's have else enter 0.")

        self.label_d1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d1.setGeometry(QtCore.QRect(10, 24, 221, 21))
        self.label_d1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d1.setObjectName("label_d1")

        self.label_d2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d2.setGeometry(QtCore.QRect(10, 50, 221, 21))
        self.label_d2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d2.setObjectName("label_d2")

        self.label_d3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d3.setGeometry(QtCore.QRect(10, 80, 221, 21))
        self.label_d3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d3.setObjectName("label_d3")

        self.label_d4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d4.setGeometry(QtCore.QRect(10, 110, 221, 21))
        self.label_d4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d4.setObjectName("label_d4")

        self.label_d5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d5.setGeometry(QtCore.QRect(10, 140, 221, 21))
        self.label_d5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d5.setObjectName("label_d5")

        self.label_d6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d6.setGeometry(QtCore.QRect(10, 170, 221, 21))
        self.label_d6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d6.setObjectName("label_d6")

        self.label_d7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_d7.setGeometry(QtCore.QRect(10, 200, 221, 21))
        self.label_d7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_d7.setObjectName("label_d7")


        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 360, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")


        

        self.label_disp1 = QtWidgets.QLabel(self.groupBox_4)
        self.label_disp1.setGeometry(QtCore.QRect(220, 30, 151, 31))
        self.label_disp1.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_disp1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_disp1.setText("")
        self.label_disp1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp1.setObjectName("label_disp1")
        self.label_disp1.setToolTip("Display for total given Incomes")

        self.label_disp2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_disp2.setGeometry(QtCore.QRect(220, 60, 151, 31))
        self.label_disp2.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_disp2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_disp2.setText("")
        self.label_disp2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp2.setObjectName("label_disp2")
        self.label_disp2.setToolTip("Display for total given Deductions")

        self.label_disp3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_disp3.setGeometry(QtCore.QRect(220, 90, 151, 31))
        self.label_disp3.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_disp3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_disp3.setText("")
        self.label_disp3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp3.setObjectName("label_disp3")
        self.label_disp3.setToolTip("Display for Gross total Income after subtract total Deduction from total incomes")

        self.label_disp4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_disp4.setGeometry(QtCore.QRect(220, 120, 151, 31))
        self.label_disp4.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);")
        self.label_disp4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_disp4.setText("")
        self.label_disp4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_disp4.setObjectName("label_disp4")
        self.label_disp4.setToolTip("Display for Payable income tax")


        self.label_PITax = QtWidgets.QLabel(self.groupBox_4)
        self.label_PITax.setGeometry(QtCore.QRect(10, 120, 201, 31))
        self.label_PITax.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_PITax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_PITax.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PITax.setObjectName("label_PITax")

        self.label_ttl_Income = QtWidgets.QLabel(self.groupBox_4)
        self.label_ttl_Income.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.label_ttl_Income.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_ttl_Income.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_ttl_Income.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ttl_Income.setObjectName("label_ttl_Income")

        self.label_GTIncome = QtWidgets.QLabel(self.groupBox_4)
        self.label_GTIncome.setGeometry(QtCore.QRect(10, 90, 201, 31))
        self.label_GTIncome.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_GTIncome.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_GTIncome.setAlignment(QtCore.Qt.AlignCenter)
        self.label_GTIncome.setObjectName("label_GTIncome")

        self.label_ttl_Deduction = QtWidgets.QLabel(self.groupBox_4)
        self.label_ttl_Deduction.setGeometry(QtCore.QRect(10, 60, 201, 31))
        self.label_ttl_Deduction.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_ttl_Deduction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_ttl_Deduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ttl_Deduction.setObjectName("label_ttl_Deduction")

        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(420, 370, 391, 151))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")

        self.pushButton_CAL = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_CAL.setGeometry(QtCore.QRect(130, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CAL.setFont(font)
        self.pushButton_CAL.setAutoFillBackground(False)
        self.pushButton_CAL.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton_CAL.setCheckable(False)
        self.pushButton_CAL.setAutoDefault(False)
        self.pushButton_CAL.setDefault(False)
        self.pushButton_CAL.setFlat(False)
        self.pushButton_CAL.setObjectName("pushButton_CAL")


        self.pushButton_CLR = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_CLR.setGeometry(QtCore.QRect(130, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_CLR.setFont(font)
        self.pushButton_CLR.setAutoFillBackground(False)
        self.pushButton_CLR.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.pushButton_CLR.setCheckable(False)
        self.pushButton_CLR.setAutoDefault(False)
        self.pushButton_CLR.setDefault(False)
        self.pushButton_CLR.setFlat(False)
        self.pushButton_CLR.setObjectName("pushButton_CLR")

        self.menuBar = QtWidgets.QMenuBar()
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 824, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("background-color: #000000")
        self.menuBar.setObjectName("menuBar")
        

        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        
        self.menuHelp.setEnabled(True)
        self.menuHelp.setGeometry(QtCore.QRect(360, 124, 135, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuHelp.sizePolicy().hasHeightForWidth())
        self.menuHelp.setSizePolicy(sizePolicy)
        self.menuHelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuHelp.setObjectName("menuHelp")
        
        self.menuTheme = QtWidgets.QMenu(self.menuBar)
        
        self.menuTheme.setEnabled(True)
        self.menuTheme.setGeometry(QtCore.QRect(360, 124, 135, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuTheme.sizePolicy().hasHeightForWidth())
        self.menuTheme.setSizePolicy(sizePolicy)
        self.menuTheme.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuTheme.setObjectName("menuTheme")

        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSetting.setIcon(icon2)
        self.menuSetting.setObjectName("menuSetting")
        
        self.menuPrint = QtWidgets.QMenu(self.menuBar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/print_property.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPrint.setIcon(icon3)
        self.menuPrint.setObjectName("menuPrint")
        self.menuPrint.setStyleSheet("color: #ffffff")
        self.menuPrint.setToolTip("Print all data in Excel File (save as .xlsx)")
        
        self.menuLogout = QtWidgets.QMenu(self.menuBar)
        self.menuLogout.setEnabled(True)
        self.menuLogout.setGeometry(QtCore.QRect(216, 124, 135, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuLogout.sizePolicy().hasHeightForWidth())
        self.menuLogout.setSizePolicy(sizePolicy)
        self.menuLogout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuLogout.setObjectName("menuLogout")




        self.actionHistory = QtWidgets.QAction()
        self.actionHistory.setObjectName("actionHistory")
        self.actionHistory.triggered.connect(self.History)

        self.actionUpdate_Password = QtWidgets.QAction()
        self.actionUpdate_Password.setObjectName("actionUpdate_Password")
        self.actionUpdate_Password.triggered.connect(self.Update_P)
        
        self.actionUpdate_Question = QtWidgets.QAction()
        self.actionUpdate_Question.setObjectName("actionUpdate_Question")
        self.actionUpdate_Question.triggered.connect(self.Update_Q)

        self.actionUpdate_Mobile_No = QtWidgets.QAction()
        self.actionUpdate_Mobile_No.setObjectName("actionUpdate_Mobile_No")
        self.actionUpdate_Mobile_No.triggered.connect(self.Update_M)

        self.menuSetting.addAction(self.actionHistory)
        self.menuSetting.addAction(self.actionUpdate_Password)
        self.menuSetting.addAction(self.actionUpdate_Question)
        self.menuSetting.addAction(self.actionUpdate_Mobile_No)

        self.darkblue = QtWidgets.QAction()
        self.darkblue.setObjectName("darkblue")
        self.darkblue.triggered.connect(self.Apply_QDarkBlue_Style)

        self.darkorange = QtWidgets.QAction()
        self.darkorange.setObjectName("darkorange")
        self.darkorange.triggered.connect(self.Apply_DarkOrange_Style)
        
        self.qdark = QtWidgets.QAction()
        self.qdark.setObjectName("qdark")
        self.qdark.triggered.connect(self.Apply_QDark_Style)

        self.qdarkgrey = QtWidgets.QAction()
        self.qdarkgrey.setObjectName("qdarkgrey")
        self.qdarkgrey.triggered.connect(self.Apply_DarkGray_Style)

        self.menuTheme.addAction(self.darkblue)
        self.menuTheme.addAction(self.darkorange)
        self.menuTheme.addAction(self.qdark)
        self.menuTheme.addAction(self.qdarkgrey)


        self.actionLogout = QtWidgets.QAction()
        self.actionLogout.setObjectName("actionLogout")

        self.menuLogout.addAction(self.actionLogout)
        self.actionLogout.triggered.connect(self.logout)

        self.actionPrint = QtWidgets.QAction()
        self.actionPrint.setObjectName("actionPrint")

        self.menuPrint.addAction(self.actionPrint)
        self.actionPrint.triggered.connect(self.i_print)

        self.actionAbout = QtWidgets.QAction()
        self.actionAbout.setObjectName("actionAbout")

        self.actionIslab = QtWidgets.QAction()
        self.actionIslab.setObjectName("actionIslab")

        
        self.menuHelp.addAction(self.actionIslab)
        self.actionIslab.triggered.connect(self.Islab)
        self.menuHelp.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.about)

        
        self.menuBar.addAction(self.menuLogout.menuAction())
        self.menuBar.addAction(self.menuPrint.menuAction())
        self.menuBar.addAction(self.menuSetting.menuAction())
        self.menuBar.addAction(self.menuTheme.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())


        self.pushButton_CAL.clicked.connect(self.Calculate)
        self.pushButton_CLR.clicked.connect(self.clear)

        
        self.comboBox_FY.addItems(['2018-19', '2019-20', '2020-21'])


        self.exp1 = ""
        self.exp2 = ""
        self.exp12 = ""
        self.exp3 = ""
        self.fy = ""
        self.inc_tax = 0

        MainWindow.setMenuBar(self.menuBar)

        self.tabWidget.addTab(self.tab_2, "")

        
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// HISTORY tab /////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
        self.pushButton_BACK1 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_BACK1.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.pushButton_BACK1.setObjectName("pushButton_BACK1")
        
        self.pushButton_PRALL = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_PRALL.setGeometry(QtCore.QRect(330, 20, 101, 41))
        self.pushButton_PRALL.setObjectName("pushButton_PRALL")
        
        self.pushButton_DEL = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_DEL.setGeometry(QtCore.QRect(580, 20, 111, 41))
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        
        self.label_H = QtWidgets.QLabel(self.tab_3)
        self.label_H.setGeometry(QtCore.QRect(70, 79, 651, 31))
        self.label_H.setObjectName("label")
        
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(70, 110, 681, 411))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 661, 411))
        self.listWidget.setObjectName("listWidget")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.tabWidget.addTab(self.tab_3, "")
        
        self.pushButton_BACK1.clicked.connect(self.back)

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// Update_Password tab /////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.pushButton_BACK2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_BACK2.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.pushButton_BACK2.setObjectName("pushButton_BACK2")
        self.pushButton_BACK2.clicked.connect(self.back)

        self.pushButton_Up = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Up.setGeometry(QtCore.QRect(320, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Up.setFont(font)
        self.pushButton_Up.setStyleSheet("color: #ffffff;")
        self.pushButton_Up.setObjectName("pushButton")
        
        self.label_up1 = QtWidgets.QLabel(self.tab_4)
        self.label_up1.setGeometry(QtCore.QRect(220, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_up1.setFont(font)
        self.label_up1.setStyleSheet("color: #ffffff;")
        self.label_up1.setObjectName("label")
        
        self.label_up2 = QtWidgets.QLabel(self.tab_4)
        self.label_up2.setGeometry(QtCore.QRect(220, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_up2.setFont(font)
        self.label_up2.setStyleSheet("color: #ffffff;")
        self.label_up2.setObjectName("label_2")
        
        self.label_up3 = QtWidgets.QLabel(self.tab_4)
        self.label_up3.setGeometry(QtCore.QRect(220, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_up3.setFont(font)
        self.label_up3.setStyleSheet("color: #ffffff;")
        self.label_up3.setObjectName("label_3")
        
        self.lineEdit_up1 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_up1.setGeometry(QtCore.QRect(420, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_up1.setFont(font)
        self.lineEdit_up1.setStyleSheet("color: #ffffff;")
        self.lineEdit_up1.setObjectName("lineEdit")
        self.lineEdit_up1.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.checkBox_UP1 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_UP1.setGeometry(QtCore.QRect(605, 167, 106, 16))
        self.checkBox_UP1.setObjectName("checkBox_UP1")
        self.checkBox_UP1.setText("Show Password")
        self.checkBox_UP1.setStyleSheet("color: #ffffff;")
        self.checkBox_UP1.setChecked(False)
        self.checkBox_UP1.toggled.connect(self.checkbox_toggled)
        self.checkBox_UP1.setToolTip("click on it for show & hide password.")




        self.lineEdit_up2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_up2.setGeometry(QtCore.QRect(420, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_up2.setFont(font)
        self.lineEdit_up2.setStyleSheet("color: #ffffff;")
        self.lineEdit_up2.setObjectName("lineEdit_2")
        self.lineEdit_up2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.checkBox_UP2 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_UP2.setGeometry(QtCore.QRect(605, 207, 106, 16))
        self.checkBox_UP2.setObjectName("checkBox_UP2")
        self.checkBox_UP2.setText("Show Password")
        self.checkBox_UP2.setStyleSheet("color: #ffffff;")
        self.checkBox_UP2.setChecked(False)
        self.checkBox_UP2.toggled.connect(self.checkbox_toggled)
        self.checkBox_UP2.setToolTip("click on it for show & hide password.")

        self.lineEdit_up3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_up3.setGeometry(QtCore.QRect(420, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_up3.setFont(font)
        self.lineEdit_up3.setStyleSheet("color: #ffffff;")
        self.lineEdit_up3.setObjectName("lineEdit_3")
        self.lineEdit_up3.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.checkBox_UP3 = QtWidgets.QCheckBox(self.tab_4)
        self.checkBox_UP3.setGeometry(QtCore.QRect(605, 247, 106, 16))
        self.checkBox_UP3.setObjectName("checkBox_UP3")
        self.checkBox_UP3.setText("Show Password")
        self.checkBox_UP3.setStyleSheet("color: #ffffff;")
        self.checkBox_UP3.setChecked(False)
        self.checkBox_UP3.toggled.connect(self.checkbox_toggled)
        self.checkBox_UP3.setToolTip("click on it for show & hide password.")

        self.tabWidget.addTab(self.tab_4, "")

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// Update_Question tab /////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.pushButton_BACK3 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_BACK3.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.pushButton_BACK3.setObjectName("pushButton_BACK3")
        self.pushButton_BACK3.clicked.connect(self.back)
        
        self.label_uq3 = QtWidgets.QLabel(self.tab_5)
        self.label_uq3.setGeometry(QtCore.QRect(220, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uq3.setFont(font)
        self.label_uq3.setStyleSheet("color: #ffffff;")
        self.label_uq3.setObjectName("label_3")
        
        self.lineEdit_uq3 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_uq3.setGeometry(QtCore.QRect(420, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_uq3.setFont(font)
        self.lineEdit_uq3.setStyleSheet("color: #ffffff;")
        self.lineEdit_uq3.setObjectName("lineEdit_3")
        
        self.label_uq1 = QtWidgets.QLabel(self.tab_5)
        self.label_uq1.setGeometry(QtCore.QRect(220, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uq1.setFont(font)
        self.label_uq1.setStyleSheet("color: #ffffff;")
        self.label_uq1.setObjectName("label")
        
        self.label_uq2 = QtWidgets.QLabel(self.tab_5)
        self.label_uq2.setGeometry(QtCore.QRect(220, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_uq2.setFont(font)
        self.label_uq2.setStyleSheet("color: #ffffff;")
        self.label_uq2.setObjectName("label_2")
        
        self.pushButton_uq = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_uq.setGeometry(QtCore.QRect(350, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_uq.setFont(font)
        self.pushButton_uq.setStyleSheet("color: #ffffff;")
        self.pushButton_uq.setObjectName("pushButton")
        
        self.lineEdit_uq1 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_uq1.setGeometry(QtCore.QRect(420, 160, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_uq1.setFont(font)
        self.lineEdit_uq1.setStyleSheet("color: #ffffff;")
        self.lineEdit_uq1.setObjectName("lineEdit")
        self.lineEdit_uq1.setEchoMode(QtWidgets.QLineEdit.Password)

        self.checkBox_Uq = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_Uq.setGeometry(QtCore.QRect(665, 167, 106, 16))
        self.checkBox_Uq.setObjectName("checkBox_Uq")
        self.checkBox_Uq.setText("Show Password")
        self.checkBox_Uq.setStyleSheet("color: #ffffff;")
        self.checkBox_Uq.setChecked(False)
        self.checkBox_Uq.toggled.connect(self.checkbox_toggled)
        self.checkBox_Uq.setToolTip("click on it for show & hide password.")
        
        self.comboBox_uq = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_uq.setGeometry(QtCore.QRect(420, 200, 241, 31))
        self.comboBox_uq.setObjectName("comboBox")
        
        self.question = ['what is your childhood nickname?',
        'what is your first teacher name?', 
        'what is your school name?',
        'what is your first friend name?',
        'what is your favourite place in the world?']

        self.comboBox_uq.addItems(self.question)
        
        self.tabWidget.addTab(self.tab_5, "")

        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////// actionUpdate_Mobile_No tab //////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        
        self.pushButton_BACK4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_BACK4.setGeometry(QtCore.QRect(100, 20, 101, 41))
        self.pushButton_BACK4.setObjectName("pushButton_BACK3")
        self.pushButton_BACK4.clicked.connect(self.back)

        self.lineEdit_um3 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_um3.setGeometry(QtCore.QRect(420, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_um3.setFont(font)
        self.lineEdit_um3.setStyleSheet("color: #ffffff;")
        self.lineEdit_um3.setObjectName("lineEdit_3")
        
        self.lineEdit_um1 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_um1.setGeometry(QtCore.QRect(420, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_um1.setFont(font)
        self.lineEdit_um1.setStyleSheet("color: #ffffff;")
        self.lineEdit_um1.setObjectName("lineEdit")
        
        self.label_um3 = QtWidgets.QLabel(self.tab_6)
        self.label_um3.setGeometry(QtCore.QRect(220, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_um3.setFont(font)
        self.label_um3.setStyleSheet("color: #ffffff;")
        self.label_um3.setObjectName("label_3")
        
        self.label_um2 = QtWidgets.QLabel(self.tab_6)
        self.label_um2.setGeometry(QtCore.QRect(220, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_um2.setFont(font)
        self.label_um2.setStyleSheet("color: #ffffff;")
        self.label_um2.setObjectName("label_2")
        
        self.pushButton_um = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_um.setGeometry(QtCore.QRect(330, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_um.setFont(font)
        self.pushButton_um.setStyleSheet("color: #ffffff;")
        self.pushButton_um.setObjectName("pushButton")
        
        self.label_um1 = QtWidgets.QLabel(self.tab_6)
        self.label_um1.setGeometry(QtCore.QRect(220, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_um1.setFont(font)
        self.label_um1.setStyleSheet("color: #ffffff;")
        self.label_um1.setObjectName("label")
        
        self.lineEdit_um2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_um2.setGeometry(QtCore.QRect(420, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_um2.setFont(font)
        self.lineEdit_um2.setStyleSheet("color: #ffffff;")
        self.lineEdit_um2.setObjectName("lineEdit_2")

        self.tabWidget.addTab(self.tab_6, "")

        self.vLay.addWidget(self.tabWidget)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.tabBar().setVisible(0)
        self.menuBar.setVisible(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setup()

        self.pushButton_Up.clicked.connect(self.update_pass)
        self.pushButton_uq.clicked.connect(self.change_ans)
        self.pushButton_um.clicked.connect(self.change_mob)



    #////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////  retranslateUi   ///////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////////////////////////////////////////////////////////////////////////


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INCOME TAX CALCULATOR"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), _translate("MainWindow", "Start Tab"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))

        self.label_inc.setText(_translate("MainWindow", "INCOME TAX CALCULATOR"))
        self.label_inc2.setText(_translate("MainWindow", "   Welcome to INCOME TAX CALCULATOR !!!!!!!!!!\n   Click on Start button and use it."))
        self.pushButton_Sr.setText(_translate("MainWindow", "Start"))

        self.groupBox_L1.setTitle(_translate("MainWindow", "SIGN IN"))
        self.label_Username_L1.setText(_translate("MainWindow", "Username"))
        self.label_Password.setText(_translate("MainWindow", "Password"))
        
        self.pushButton_Login.setText(_translate("MainWindow", "Login"))
        
        self.groupBox_L2.setTitle(_translate("MainWindow", "SIGN UP"))
        
        self.label_Passd.setText(_translate("MainWindow", "Password"))
        self.label_SA.setText(_translate("MainWindow", "Security Answer"))
        self.label_Repassd.setText(_translate("MainWindow", "Re-type Password"))
        self.label_Lastname.setText(_translate("MainWindow", "Last Name"))
        self.label_UserN.setText(_translate("MainWindow", "Username"))
        self.label_PAN_L.setText(_translate("MainWindow", "PAN Card Number"))
        self.label_SQ.setText(_translate("MainWindow", "Security Question"))
        self.label_DOB.setText(_translate("MainWindow", "Date of Birth"))
        self.label_Firstname.setText(_translate("MainWindow", "First Name"))
        self.pushButton_Signup.setText(_translate("MainWindow", "SignUp"))
        self.label_MOB.setText(_translate("MainWindow", "Mobile Number"))

        self.label_3.setText(_translate("MainWindow", "TAX"))
        self.label_14.setText(_translate("MainWindow", "INCOME"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.label_Name.setText(_translate("MainWindow", "Name"))
        self.label_Username.setText(_translate("MainWindow", "Username"))
        self.label_PAN.setText(_translate("MainWindow", "PAN Card No."))
        self.label_Age.setText(_translate("MainWindow", "Age"))
        
        self.groupBox.setTitle(_translate("MainWindow", "BASIC DETAILS"))
        self.label_FY.setText(_translate("MainWindow", "Financial Year"))
        
        self.groupBox_2.setTitle(_translate("MainWindow", "iNCOME TAB"))
        self.label_i1.setText(_translate("MainWindow", "Gross Salary"))
        self.lineEdit_i1.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i1.setText('0')
        self.label_i2.setText(_translate("MainWindow", "Exemption from Salary"))
        self.lineEdit_i2.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i2.setText('0')
        self.label_i3.setText(_translate("MainWindow", "Income from Interest"))
        self.lineEdit_i3.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i3.setText('0')

        self.groupBox_3.setTitle(_translate("MainWindow", "DEDUCTION TAB"))
        self.groupBox_4.setTitle(_translate("MainWindow", "PAYABLE INCOME TAX "))


        self.label_i4.setText(_translate("MainWindow", "Other Income"))
        self.lineEdit_i4.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i4.setText('0')
        self.label_i5.setText(_translate("MainWindow", "Intrest paid on Home Loan"))
        self.lineEdit_i5.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i5.setText('0')
        self.label_i6.setText(_translate("MainWindow", "Rental Income Received"))
        self.lineEdit_i6.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i6.setText('0')
        self.label_i7.setText(_translate("MainWindow", "Income paid on Loan"))
        self.lineEdit_i7.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_i7.setText('0')
        
        self.label_d1.setText(_translate("MainWindow", "Basic Deduction u/s 80C"))
        self.lineEdit_d1.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d1.setText('0')
        self.label_d2.setText(_translate("MainWindow", "Intrest from deposit u/s 80TTA"))
        self.lineEdit_d2.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d2.setText('0')
        self.label_d3.setText(_translate("MainWindow", "Medical Insurance u/s 80D"))
        self.lineEdit_d3.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d3.setText('0')
        self.label_d4.setText(_translate("MainWindow", "Donation on Charity u/s 80G"))
        self.lineEdit_d4.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d4.setText('0')
        self.label_d5.setText(_translate("MainWindow", "Intrest on Education Loan u/s 80E"))
        self.lineEdit_d5.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d5.setText('0')
        self.label_d6.setText(_translate("MainWindow", "Intrest on Housing Loan u/s 80EEA"))
        self.lineEdit_d6.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d6.setText('0')
        self.label_d7.setText(_translate("MainWindow", "Employee\'s contribution to NPS u/s 80CCD"))
        self.lineEdit_d7.setPlaceholderText(_translate("MainWindow", "0"))
        self.lineEdit_d7.setText('0')

        self.label_ttl_Income.setText(_translate("MainWindow", "Total Income"))
        self.label_ttl_Deduction.setText(_translate("MainWindow", "Total Deduction "))
        self.label_GTIncome.setText(_translate("MainWindow", "Gross Total Income"))
        self.label_PITax.setText(_translate("MainWindow", "Payable Income Tax"))
        self.pushButton_CAL.setText(_translate("MainWindow", "CALCULATE"))
        self.pushButton_CLR.setText(_translate("MainWindow", "CLEAR"))
        
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuPrint.setTitle(_translate("MainWindow", "Print"))
        self.menuLogout.setTitle(_translate("MainWindow", "Logout"))
        self.menuTheme.setTitle(_translate("MainWindow", "Themes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        self.qdarkgrey.setText(_translate("MainWindow", "DARK GERY"))
        self.qdark.setText(_translate("MainWindow", "Q DARK"))
        self.darkorange.setText(_translate("MainWindow", "DARK ORANGE"))
        self.darkblue.setText(_translate("MainWindow", "DARK BLUE"))


        
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionUpdate_Password.setText(_translate("MainWindow", "Update Password"))
        self.actionUpdate_Question.setText(_translate("MainWindow", "Update Question"))
        self.actionUpdate_Mobile_No.setText(_translate("MainWindow", "Update Mobile No."))
        self.actionPrint.setText(_translate("MainWindow", "Print on Excel file"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionIslab.setText(_translate("MainWindow", "Income Tax Slab"))
        

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.pushButton_PRALL.setText(_translate("MainWindow", "Print"))
        
        self.pushButton_BACK1.setText(_translate("MainWindow", "Back"))
        self.pushButton_BACK2.setText(_translate("MainWindow", "Back"))
        self.pushButton_BACK3.setText(_translate("MainWindow", "Back"))
        self.pushButton_BACK4.setText(_translate("MainWindow", "Back"))
        
        self.pushButton_DEL.setText(_translate("MainWindow", "Delete"))
        self.label_H.setText(_translate("MainWindow", "  Name                       PAN No.                      Age           Gross Total Income      Payable Income Tax              Date            Time "))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.pushButton_Up.setText(_translate("MainWindow", "UPDATE"))
        self.label_up1.setText(_translate("MainWindow", "CURRENT PASSWORD"))
        self.label_up2.setText(_translate("MainWindow", "NEW PASSWORD"))
        self.label_up3.setText(_translate("MainWindow", "RE-TYPE NEW PASSWORD"))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.label_uq3.setText(_translate("MainWindow", "NEW ANSWER"))
        self.label_uq1.setText(_translate("MainWindow", "ENTER PASSWORD"))
        self.label_uq2.setText(_translate("MainWindow", "NEW QUESTION"))
        self.pushButton_uq.setText(_translate("MainWindow", "UPDATE"))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.label_um3.setText(_translate("MainWindow", "RE-TYPE NEW MOBILE No."))
        self.label_um2.setText(_translate("MainWindow", "NEW MOBILE No."))
        self.pushButton_um.setText(_translate("MainWindow", "UPDATE"))
        self.label_um1.setText(_translate("MainWindow", "CURRENT MOBILE No."))

    
    def setup(self):
        try:
            self.my_model=Model.Model()
            if self.my_model.get_db_status():
                print("succesfully connect to db")
            else:
                raise Exception("Sorry! database not connected")
        except Exception as ex:
            print("DB Error:",ex)
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!","Check your DB Error!",QtWidgets.QMessageBox.Ok)
            
        self.pushButton_Login.clicked.connect(self.login)
        self.pushButton_Signup.clicked.connect(self.signup)


    def login(self):
        
        self.user=self.lineEdit_Username.text()
        self.passw=self.lineEdit_Password.text()

        if len(self.user)<=5:
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!","Please enter username atleast 5 character",QtWidgets.QMessageBox.Ok)

        if len(self.passw)<=7:
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!","Please enter Password atleast 8 character",QtWidgets.QMessageBox.Ok)
            
        else:
            login=self.my_model.log_in(self.user,self.passw)

            if login[0]==True:
                self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"succesfully","login succesfully",QtWidgets.QMessageBox.Ok)
                self.my_model.user_update(self.user)
                
                self.tabWidget.setCurrentIndex(2)
                self.menuBar.setVisible(1)
                self.setup_inc()
                self.clearall()

            else:
                self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!",login[1],QtWidgets.QMessageBox.Ok)
                
    
    def signup(self):
        
        first=self.lineEdit_Firstname.text()
        last=self.lineEdit_LastName.text()
        user=self.lineEdit_UserN.text()
        passw=self.lineEdit_Passd.text()
        r_pass=self.lineEdit_Repassd.text()
        pan=self.lineEdit_PAN_Inc.text()
        mob=self.lineEdit_MOB.text()
        dob=self.comboBox_date.currentText()+self.comboBox_month.currentText()+self.comboBox_year.currentText()
        ques=self.comboBox_SQ.currentText()
        ans=self.lineEdit_SA.text()

        print(first,last,user,passw,pan,mob,dob,ques,ans)

        if first.isalpha()==True and last.isalpha()==True and len(user)>=0 and len(pan)==10 and len(mob)==10 and mob.isdigit()==True and len(ques)>=5 and len(ans)>=1 and len(dob)==8 and len(passw)>=7 and len(passw)<=16 and passw==r_pass :
        
            if ques=='what is your childhood nickname?':
                ques='age'
            elif ques=='what is your first teacher name?':
                ques='first_pet'
            elif ques=='what is your first school name?':
                ques='school_name'
            elif ques=='what is your first friend name?':
                ques='first_friend_name'
            elif ques=='what is your favourite place in the world?':
                ques='favourite_place'
        
            result=self.my_model.ragistration(first,last,user,passw,pan,mob,dob,ques,ans)    
        
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"succesfully","login succesfully",QtWidgets.QMessageBox.Ok)        
            self.my_model.user_update(user)
            
            self.tabWidget.setCurrentIndex(2)
            self.menuBar.setVisible(1)
            self.setup_inc()
            self.clearall()
        
        else:
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error","enter valid detail",QtWidgets.QMessageBox.Ok)
    
    
    def setup_inc(self):
        try:
            self.my_model=Model.Model()
            if self.my_model.get_db_status():                
                self.user=self.my_model.get_user()
                self.label_User.setText(str(self.user))
                print("succesfully connect to db")
            else:
                raise Exception("Sorry! database not connected")
        except Exception as ex:
            print("DB Error:",ex)
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!","Check your DB Error!",QtWidgets.QMessageBox.Ok)
            

    def income(self):
        self.inc = 0
        self.inc = self.inc + int(self.lineEdit_i1.text()) + int(self.lineEdit_i2.text())+int(self.lineEdit_i3.text())+int(self.lineEdit_i4.text())+int(self.lineEdit_i5.text())+int(self.lineEdit_i6.text())+int(self.lineEdit_i7.text())        
        return self.inc

    def deduct(self):
        self.dec = 0
        self.dec = self.dec + int(self.lineEdit_d1.text()) + int(self.lineEdit_d2.text())+int(self.lineEdit_d3.text())+int(self.lineEdit_d4.text())+int(self.lineEdit_d5.text())+int(self.lineEdit_d6.text())+int(self.lineEdit_d7.text())
        return self.dec

    def ttl_income(self):
        self.ttl_inc = self.income() - self.deduct()
        return self.ttl_inc

    def fy201819(self):
        def less_rebate():
            print(self.inc_tax)
            #Less Rebate u/s 87A
            if self.inc_tax <= 2500:
                self.inc_tax = self.inc_tax*0
                return self.inc_tax

        def surcharge():

            cess = sur50 = sur1c = 0
            cess = cess + int(self.inc_tax*4/100)

            if 5000000<self.ttl_income():

                if 5000000 < self.ttl_income() <= 10000000:
                    sur50 = sur50 + int(self.inc_tax*10/100)

                if self.ttl_income()>10000000:
                    sur50 = sur50 + int(self.inc_tax*15/100)

            if 10000000<self.ttl_income():

                if 10000000 < self.ttl_income() <= 100000000:
                    sur1c = sur1c + int(self.inc_tax*7/100)

                if self.ttl_income()>100000000:
                    sur1c = sur1c + int(self.inc_tax*12/100)

            sur = cess + sur50 + sur1c
            return sur

        if int(self.lineEdit_Age.text()) < 60:
            #inc_b2 = inc_b5 = inc_b10 = inc_b11 = 0

            if (self.ttl_income()<=250000):
                self.inc_tax = self.inc_tax + 0 #inc_b2

            if ((250000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)) :
                #inc_b5 = inc_b5+int((self.ttl_income()-250000)*5/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-250000)*5/100) #inc_b5
                

            if((500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)):
    #            inc_b10 = inc_b10 + int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-500000)*20/100) #inc_b10
                

            if(self.ttl_income()>1000000):
                #inc_b11 = inc_b11 + int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-1000000)*30/100) #inc_b11
                

            less_rebate()

            self.inc_tax += surcharge()
            return self.inc_tax

            
        if 60 <= int(self.lineEdit_Age.text()) < 80:


            if (self.ttl_income()<=300000):
                inc_a3 = 0
                self.inc_tax = self.inc_tax + inc_a3
                

            if(300000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a5 = int((self.ttl_income()-300000)*5/100)
                self.inc_tax = self.inc_tax + inc_a5
                

            if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a10 = int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + inc_a10
                

            if(self.ttl_income()>1000000):
                inc_a11 = int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + inc_a11
                

            less_rebate()
            

            self.inc_tax += surcharge()
            return self.inc_tax

        if int(self.lineEdit_Age.text()) >= 80:


            if (self.ttl_income()<=500000):
                inc_a83 = 0
                self.inc_tax = self.inc_tax + inc_a83
                

            if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a810 = int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + inc_a810
                

            if(self.ttl_income()>1000000):
                inc_a811 = int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + inc_a811
                

            self.inc_tax += surcharge()
            return self.inc_tax

    def fy201920(self):
        
        def less_rebate1():
            print(self.inc_tax)
            #Less Rebate u/s 87A
            if self.inc_tax <= 12500:
                self.inc_tax = self.inc_tax*0
                return self.inc_tax

        def surcharge1():

            cess = sur50 = sur1c = sur2c = sur5c = 0
            cess = cess + int(self.inc_tax*4/100)

            if 5000000 < self.ttl_income() <= 10000000:
                sur50 = sur50 + int(self.inc_tax*10/100)   

            elif 10000000 < self.ttl_income() <= 20000000:
                sur1c = sur1c + int(self.inc_tax*15/100)

            elif 20000000 < self.ttl_income() <= 50000000:
                sur2c = sur2c + int(self.inc_tax*25/100)

            elif self.ttl_income()>50000000:
                sur5c = sur5c + int(self.inc_tax*37/100)

            sur = cess + sur50 + sur1c
            return sur

        if int(self.lineEdit_Age.text()) < 60:

            if (self.ttl_income()<=250000):
                self.inc_tax = self.inc_tax + 0 #inc_b2

            if ((250000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)) :
                #inc_b5 = inc_b5+int((self.ttl_income()-250000)*5/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-250000)*5/100) #inc_b5
                

            if((500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000)):
    #            inc_b10 = inc_b10 + int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-500000)*20/100) #inc_b10
                

            if(self.ttl_income()>1000000):
                #inc_b11 = inc_b11 + int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + int((self.ttl_income()-1000000)*30/100) #inc_b11
                

            less_rebate1()

            self.inc_tax += surcharge1()
            return self.inc_tax

            
        if 60 <= int(self.lineEdit_Age.text()) < 80:


            if (self.ttl_income()<=300000):
                inc_a3 = 0
                self.inc_tax = self.inc_tax + inc_a3
                

            if(300000<self.ttl_income()<=500000) or (500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a5 = int((self.ttl_income()-300000)*5/100)
                self.inc_tax = self.inc_tax + inc_a5
                

            if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a10 = int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + inc_a10
                

            if(self.ttl_income()>1000000):
                inc_a11 = int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + inc_a11
                
            less_rebate1()

            self.inc_tax += surcharge1()
            return self.inc_tax

        if int(self.lineEdit_Age.text()) > 80:

            if (self.ttl_income()<=500000):
                inc_a83 = 0
                self.inc_tax = self.inc_tax + inc_a83
                

            if(500000<self.ttl_income()<=1000000) or (self.ttl_income()>1000000):
                inc_a810 = int((self.ttl_income()-500000)*20/100)
                self.inc_tax = self.inc_tax + inc_a810
                

            if(self.ttl_income()>1000000):
                inc_a811 = int((self.ttl_income()-1000000)*30/100)
                self.inc_tax = self.inc_tax + inc_a811
                

            self.inc_tax += surcharge1()
            return self.inc_tax

    def fy202021(self):
        
        def less_rebate2():
            print(self.inc_tax)
            #Less Rebate u/s 87A
            if self.inc_tax <= 12500:
                self.inc_tax = self.inc_tax*0
                return self.inc_tax

        def surcharge2():

            cess = sur50 = sur1c = sur2c = sur5c = 0
            cess = cess + int(self.inc_tax*4/100)

            if 5000000 < self.ttl_income() <= 10000000:
                sur50 = sur50 + int(self.inc_tax*10/100)   

            elif 10000000 < self.ttl_income() <= 20000000:
                sur1c = sur1c + int(self.inc_tax*15/100)

            elif 20000000 < self.ttl_income() <= 50000000:
                sur2c = sur2c + int(self.inc_tax*25/100)

            elif self.ttl_income()>50000000:
                sur5c = sur5c + int(self.inc_tax*37/100)

            sur = cess + sur50 + sur1c + sur2c + sur5c
            return sur

        if 0 < int(self.lineEdit_Age.text()) < 80 or int(self.lineEdit_Age.text()) >= 80:

            inc1 = 0
            inc2 = 12500
            inc3 = 25000
            inc4 = 37500
            inc5 = 50000
            inc6 = 62500
            inc7 = 75000
            
            if (self.ttl_income()<=250000):
                self.inc_tax = self.inc_tax + 0

            if (250000<self.ttl_income()<=500000):
                self.inc_tax = self.inc_tax + int((self.ttl_income()-250000)*5/100)

            if(500000<self.ttl_income()<=750000):
                self.inc_tax = self.inc_tax + inc2 + int((self.ttl_income()-500000)*10/100)

            if(750000<self.ttl_income()<=1000000):
                self.inc_tax = self.inc_tax + inc2 + inc3 + int((self.ttl_income()-750000)*15/100)

            if(1000000<self.ttl_income()<=1250000):
                self.inc_tax = self.inc_tax + inc2 + inc3 + inc4 + int((self.ttl_income()-1000000)*20/100)

            if(1250000<self.ttl_income()<=1500000):
                self.inc_tax = self.inc_tax + inc2 + inc3 + inc4 +inc5 + int((self.ttl_income()-1250000)*25/100)

            if (self.ttl_income()>1500000):
                if (self.ttl_income()>1750000):
                    self.inc_tax = self.inc_tax + inc2 + inc3 + inc4 +inc5 + inc6 + inc7
                else:    
                    self.inc_tax = self.inc_tax + inc2 + inc3 + inc4 +inc5 + inc6 + int((self.ttl_income()-1500000)*30/100) 
                
            less_rebate2()

            self.inc_tax += surcharge2()
            return self.inc_tax


    def Calculate(self):
        name = self.lineEdit_Name.text()
        PAN = self.lineEdit_PAN.text()
        age = self.lineEdit_Age.text()
        fy = self.comboBox_FY.currentText()

        i1 = self.lineEdit_i1.text()
        i2 = self.lineEdit_i2.text()
        i3 = self.lineEdit_i3.text()
        i4 = self.lineEdit_i4.text()
        i5 = self.lineEdit_i5.text()
        i6 = self.lineEdit_i6.text()
        i7 = self.lineEdit_i7.text()

        d1 = self.lineEdit_d1.text()
        d2 = self.lineEdit_d2.text()
        d3 = self.lineEdit_d3.text()
        d4 = self.lineEdit_d4.text()
        d5 = self.lineEdit_d5.text()
        d6 = self.lineEdit_d6.text()
        d7 = self.lineEdit_d7.text()

        inc = str(self.income())
        dec = str(self.deduct())
        ttl = str(self.ttl_income())

        if len(name)==0 or len(PAN) ==0 or len(age) == 0:
            QtWidgets.QMessageBox.information(MainWindow,"Error!","Please enter valid details",QtWidgets.QMessageBox.Ok)            

        else:
            self.fy = self.fy + self.comboBox_FY.currentText()
            
            self.exp1 = self.exp1 + str(self.income())
            self.label_disp1.setText(self.exp1)

            self.exp2 = self.exp2 + str(self.deduct())
            self.label_disp2.setText(self.exp2)

            self.exp12 = self.exp12 + str(self.ttl_income())
            self.label_disp3.setText(self.exp12)


            if self.comboBox_FY.currentText() == '2018-19':
                self.exp3 = self.exp3 + str(self.fy201819())
                self.label_disp4.setText(self.exp3)        
            
            if self.comboBox_FY.currentText() == '2019-20':
                self.exp3 = self.exp3 + str(self.fy201920())
                self.label_disp4.setText(self.exp3)

            if self.comboBox_FY.currentText() == '2020-21':
                self.exp3 = self.exp3 + str(self.fy202021())
                self.label_disp4.setText(self.exp3)

            print(self.user,name,PAN,age,fy,i1,i2,i3,i4,i5,i6,i7,d1,d2,d3,d4,d5,d6,d7,inc,dec,ttl,self.exp3)
            
            self.my_model.add_history(self.user,name,PAN,age,fy,i1,i2,i3,i4,i5,i6,i7,d1,d2,d3,d4,d5,d6,d7,inc,dec,ttl,self.exp3)


    def i_print(self):
        try:

            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            files, _ = QtWidgets.QFileDialog.getSaveFileName(MainWindow,"QtWidgets.QFileDialog.getSaveFileName()","","Excel File (*.xlsx)", options=options)
            if files:
                print(files)

        except xls.exceptions.FileCreateError:
            QtWidgets.QMessageBox.information(MainWindow,"","",QtWidgets.QMessageBox.Ok)
            self.tabWidget.setCurrentIndex(2)

        
        # Create an new Excel file and add a worksheet.
        self.workbook = xls.Workbook(files)
        self.worksheet = self.workbook.add_worksheet()

         # Add a bold format to use to highlight cells.
        bold = self.workbook.add_format({'bold': True})

        self.worksheet.set_column('D:F', 25)

        self.worksheet.write('E2', 'INCOME TAX CALCULATOR',bold)

        # Write some simple text.
        self.worksheet.write('D3','Name:' ,bold)
        self.worksheet.write('E3',str(self.lineEdit_Name.text()))
        self.worksheet.write('D4', 'Financial year:',bold)
        self.worksheet.write('E4', self.comboBox_FY.currentText(), bold)

        self.worksheet.write('D5', 'PAN No.:', bold)
        self.worksheet.write('E5', str(self.lineEdit_PAN.text()), bold)
        self.worksheet.write('F5', self.lineEdit_Age.text(), bold)

        self.worksheet.write('D7', 'Sr.No.', bold)
        self.worksheet.write('E7', 'Description', bold)
        self.worksheet.write('F7', 'Amount (in ₹)', bold)

        self.worksheet.write('D8', '1.')
        self.worksheet.write('D9', '2.')
        self.worksheet.write('D10', '3.')

        self.worksheet.write('E8', 'Total Income:')
        self.worksheet.write('E9', 'Total Deduction:')
        self.worksheet.write('E10', 'Gross Total Income:')
        self.worksheet.write('E11', 'Payable Income Tax:')

        self.worksheet.write(7, 5, self.exp1)
        self.worksheet.write(8, 5, self.exp2)
        self.worksheet.write(9, 5, self.exp12)
        self.worksheet.write(10, 5, self.exp3)

        self.workbook.close()


    def clear(self):
        self.inc_tax = 0
        self.exp1=self.exp2=self.exp3=self.exp12=""
        self.label_disp1.setText("")
        self.label_disp2.setText("")
        self.label_disp3.setText("")
        self.label_disp4.setText("")          
        self.fy = ""


    def logout(self):
        self.tabWidget.setCurrentIndex(1)
        self.menuBar.setVisible(0)
        self.clearall()


    def History(self):
        self.tabWidget.setCurrentIndex(3)
        self.setup_His()
        self.clearall()


    def setup_His(self):
        self.my_model=Model.Model()
        self.user=self.my_model.get_user()
        self.inser_list()
        self.pushButton_PRALL.clicked.connect(self.printal)
        self.pushButton_DEL.clicked.connect(self.remove_history)
        


    def printal(self):
        data = self.data
        print_allpdf.pdfw(MainWindow, data)


    def inser_list(self):
        self.history=self.my_model.get_history(self.user)
        if self.history==False:
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error","history is empty",QtWidgets.QMessageBox.Ok)
        else:
            lis=self.list_show(self.history)
            self.listWidget.addItems(lis)


    def list_show(self,his):
        lis=[]
        self.data=[['Name','Pan No.','Age','Gross Total Income','Payable Income Tax','Date','Time']]
        for h in tuple(his):
            n=str(h[0])
            p=str(h[1])
            a=str(h[2])
            inc=str(h[3])
            t=str(h[4])
            dt=str(h[5])
            li=[h[0],h[1],h[2],h[3],h[4]]
            if len(n)<=13:
                l=13-len(n)
                for i in range(0,l):
                    n=n+' '
            if len(p)<=13:
                l=13-len(p)
                for i in range(0,l):
                    p=p+' '
            if len(a)<=7:
                l=7-len(a)
                for i in range(0,l):
                    a=a+' '
            if len(inc)<=16:
                l=16-len(inc)
                for i in range(0,l):
                    inc=inc+' '
            if len(t)<=13:
                l=13-len(t)
                for i in range(0,l):
                    t=t+' '

            date=dt[0:4]+'/'+dt[4:6]+'/'+dt[6:8]+" "+dt[8:10]+":"+dt[10:12]+':'+dt[12:14]

            pp=n+p+a+inc+t+date
            li.append(dt[0:4]+'-'+dt[4:6]+'-'+dt[6:8])
            li.append(dt[8:10]+":"+dt[10:12]+':'+dt[12:14])
            self.data.append(li)
            lis.append(pp)
        return lis


    def remove_history(self):
        sel_item = self.listWidget.currentItem()
        print(sel_item)

        try:
            if sel_item.text()=="":
                print(sel_item.text())
                raise Exception

            else:
                value=sel_item.text()
                print(value)
                ti=value[62:81]
                time=ti[0:4]+ti[5:7]+ti[8:10]+ti[11:13]+ti[14:16]+ti[17:19]
                self.my_model.remove_history(self.user,time)
                self.listWidget.takeItem(self.listWidget.row(sel_item))

        except Exception as ex1:
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"Error!","",QtWidgets.QMessageBox.Ok)
       
                
    def Update_P(self):
        self.tabWidget.setCurrentIndex(4)
        self.clearall()

    def update_pass(self):
        my_model=Model.Model()
        user=my_model.get_user()
        curent=self.lineEdit_up1.text()
        new=self.lineEdit_up2.text()
        rnew=self.lineEdit_up3.text()
        print(new)
        passw=my_model.get_pass(user)
        if new==rnew and curent==passw and len(new)<=16 and len(new)>=7:
            my_model.update_pass(user,new)
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"succesfully","Password Update!",QtWidgets.QMessageBox.Ok)
            self.tabWidget.setCurrentIndex(2)

        if new != '':
            pass
        else:
            QtWidgets.QMessageBox.information(MainWindow,"error","enter valid Password ",QtWidgets.QMessageBox.Ok)


    def Update_Q(self):
        self.tabWidget.setCurrentIndex(5)
        self.clearall()
    
    def change_ans(self):
            my_model=Model.Model()
            user=my_model.get_user()
            epassw=str(self.lineEdit_uq1.text())
            quess=str(self.comboBox_uq.currentText())
            ans=str(self.lineEdit_uq3.text())

            passw=my_model.get_pass(user)
            if passw==epassw:
                if len(quess)>=5 and len(ans)>=1:
                    quess=ques1(quess)
                    my_model.update_ques(user,quess)
                    my_model.update_ans(user,ans)

                    self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"succesfully","Succesfully change",QtWidgets.QMessageBox.Ok)
                    self.tabWidget.setCurrentIndex(2)

                else:
                    QtWidgets.QMessageBox.information(MainWindow,"error","Choose Question and enter Answer.",QtWidgets.QMessageBox.Ok)
                    

            if epassw!='':
                pass
            else:
                QtWidgets.QMessageBox.information(MainWindow,"error","enter password",QtWidgets.QMessageBox.Ok)

    def back(self):
        self.tabWidget.setCurrentIndex(2)
        self.clearall()


    def Update_M(self):
        self.tabWidget.setCurrentIndex(6)
        self.clearall()

    def change_mob(self):
        my_model=Model.Model()
        user=my_model.get_user()
        curr=self.lineEdit_um1.text()
        new=self.lineEdit_um2.text()
        rnew=self.lineEdit_um3.text()
        mob=my_model.get_mob(user)
        if mob==curr and new==rnew and len(str(new))==10:
            my_model.update_mob(user,new)
            self.messagebox = QtWidgets.QMessageBox.information(MainWindow,"succesfully","Mobile No. succesfully change",QtWidgets.QMessageBox.Ok)            
            self.tabWidget.setCurrentIndex(2)

        if curr != '':
            pass
        else:
            QtWidgets.QMessageBox.information(MainWindow,"error","enter valid Mobile No.",QtWidgets.QMessageBox.Ok)
    
    def Start(self):
        self.tabWidget.setCurrentIndex(1)


    def clearall(self):
        self.lineEdit_Username.setText("")
        self.lineEdit_Password.setText("")

        self.lineEdit_Firstname.setText("")
        self.lineEdit_LastName.setText("")
        self.lineEdit_Passd.setText("")
        self.lineEdit_Repassd.setText("")
        self.lineEdit_UserN.setText("")
        self.lineEdit_PAN_Inc.setText("")
        self.lineEdit_MOB.setText("")
        self.lineEdit_SA.setText("")
        
        self.lineEdit_Name.setText("")
        self.lineEdit_Age.setText("")
        self.lineEdit_PAN.setText("")
        
        self.lineEdit_up1.setText("")
        self.lineEdit_up2.setText("")
        self.lineEdit_up3.setText("")

        self.lineEdit_uq1.setText("")
        self.lineEdit_uq3.setText("")

        self.lineEdit_um1.setText("")
        self.lineEdit_um2.setText("")
        self.lineEdit_um3.setText("")


    def checkbox_toggled(self):
        
        if self.checkBox_L.isChecked():
            self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_L.setText("Hide Password")
        else:
            self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.checkBox_L.setText("Show Password")


        if self.checkBox_S1.isChecked():
            self.lineEdit_Passd.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_S1.setText("Hide Password")
        else:
            self.lineEdit_Passd.setEchoMode(QtWidgets.QLineEdit.Password)
            self.checkBox_S1.setText("Show Password")


        if self.checkBox_S2.isChecked():
            self.lineEdit_Repassd.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_S2.setText("Hide Password")
        else:
            self.lineEdit_Repassd.setEchoMode(QtWidgets.QLineEdit.Password)
            self.checkBox_S2.setText("Show Password")


        if self.checkBox_UP1.isChecked():
            self.lineEdit_up1.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_UP1.setText("Hide Password")
        else:
            self.lineEdit_up1.setEchoMode(QtWidgets.QLineEdit.Password)
            self.checkBox_UP1.setText("Show Password")
        

        if self.checkBox_UP2.isChecked():
            self.lineEdit_up2.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_UP2.setText("Hide Password")
        else:
            self.lineEdit_up2.setEchoMode(QtWidgets.QLineEdit.Password)
            self.checkBox_UP2.setText("Show Password")


        if self.checkBox_UP3.isChecked():
            self.lineEdit_up3.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_UP3.setText("Hide Password")
        else:
            self.lineEdit_up3.setEchoMode(QtWidgets.QLineEdit.Password)  
            self.checkBox_UP3.setText("Show Password")  

        if self.checkBox_Uq.isChecked():
            self.lineEdit_uq1.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.checkBox_Uq.setText("Hide Password")
        else:
            self.lineEdit_uq1.setEchoMode(QtWidgets.QLineEdit.Password)  
            self.checkBox_Uq.setText("Show Password")  

    ################################################
    ################# App Themes ###################

    def Apply_DarkOrange_Style(self):
        style = open('themes/darkorange.css' , 'r')
        style = style.read()
        MainWindow.setStyleSheet(style)


    def Apply_QDark_Style(self):
        style = open('themes/qdark.css' , 'r')
        style = style.read()
        MainWindow.setStyleSheet(style)


    def Apply_DarkGray_Style(self):
        style = open('themes/qdarkgray.css' , 'r')
        style = style.read()
        MainWindow.setStyleSheet(style)

    def Apply_QDarkBlue_Style(self):
        style = open('themes/darkblu.css' , 'r')
        style = style.read()
        MainWindow.setStyleSheet(style)

    def about(self):
        QtWidgets.QMessageBox.about(MainWindow, "About Income Tax Calculator",
                "<h1><b>INCOME TAX CALCULATOR</b></h1>" \
                "<p>This <b>Application</b> is implemented by Qt version 5.13.0 ." \
                "This <b>Application</b> is build with the help of <b>PyQt5</b>" \
                " modules of python.</p>" \
                "<p>It's a Modern GUI application using Qt designer, with a menubar," \
                "tooltips, and many more features of Qt designer.</p>" \
                "<p>In this Application we used Login and SignUp authentication wih" \
                "the help of sqlite database.</p>" \
                "<p>Some Creative features are shown in this Application such as show &." \
                "hide password features, tooltips for basic knowledge of any tool," \
                "some different themes.</p>" \
                "<p>Income Tax Calculator used for Calculator income tax by the given" \
                "three different Financial Years such as 2018-19, 2019-20,2020-21.</p>" \
                "<p>After Calculate all the data will be automatically saved into DB.</p>") 

    def Islab(self):
    	
    	self.tabdialog = ITaxSlab()
    	self.tabdialog.show()
    	

def ques1(ques):
    if ques=='what is your childhood nickname?':
        q='age'
    elif ques=='what is your first teacher name?':
        q='first_pet'
    elif ques=='what is your school name?':
        q='school_name'
    elif ques=='what is your first friend name?':
        q='first_friend_name'
    elif ques=='what is your favourite place in the world?':
        q='favourite_place'
    return q



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
