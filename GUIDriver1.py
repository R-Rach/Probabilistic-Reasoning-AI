"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ComputeProbabity import computeProab
from GenFunctions import *

global queryList
queryList = []
global conditionList
conditionList = []
global bayesNetDict
bayesNetDict = {}


class GUIDriver(QMainWindow):

    def __init__(self):
        super(GUIDriver, self).__init__()
        self.setGeometry(0, 30, 1450, 810)
        self.setWindowTitle("AI Assignment 4")
        self.initGUI1()


    def initGUI1(self):

        ###QUERY BUTTONS
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Select QUERY")
        self.label1.move(70, 0)

        self.bAQ = QtWidgets.QPushButton(self)
        self.bAQ.resize(100, 30)
        self.bAQ.move(10, 30)
        self.bAQ.setText("A")
        self.bAQ.clicked.connect(self.bAQclick)

        self.bNAQ = QtWidgets.QPushButton(self)
        self.bNAQ.resize(100, 30)
        self.bNAQ.move(110, 30)
        self.bNAQ.setText("~A")
        self.bNAQ.clicked.connect(self.bNAQclick)

        self.bBQ = QtWidgets.QPushButton(self)
        self.bBQ.resize(100, 30)
        self.bBQ.move(10, 60)
        self.bBQ.setText("B")
        self.bBQ.clicked.connect(self.bBQclick)

        self.bNBQ = QtWidgets.QPushButton(self)
        self.bNBQ.resize(100, 30)
        self.bNBQ.move(110, 60)
        self.bNBQ.setText("~B")
        self.bNBQ.clicked.connect(self.bNBQclick)

        self.bCQ = QtWidgets.QPushButton(self)
        self.bCQ.resize(100, 30)
        self.bCQ.move(10, 90)
        self.bCQ.setText("C")
        self.bCQ.clicked.connect(self.bCQclick)

        self.bNCQ = QtWidgets.QPushButton(self)
        self.bNCQ.resize(100, 30)
        self.bNCQ.move(110, 90)
        self.bNCQ.setText("~C")
        self.bNCQ.clicked.connect(self.bNCQclick)

        self.bDQ = QtWidgets.QPushButton(self)
        self.bDQ.resize(100, 30)
        self.bDQ.move(10, 120)
        self.bDQ.setText("D")
        self.bDQ.clicked.connect(self.bDQclick)

        self.bNDQ = QtWidgets.QPushButton(self)
        self.bNDQ.resize(100, 30)
        self.bNDQ.move(110, 120)
        self.bNDQ.setText("~D")
        self.bNDQ.clicked.connect(self.bNDQclick)

        self.bFQ = QtWidgets.QPushButton(self)
        self.bFQ.resize(100, 30)
        self.bFQ.move(10, 150)
        self.bFQ.setText("F")
        self.bFQ.clicked.connect(self.bFQclick)

        self.bNFQ = QtWidgets.QPushButton(self)
        self.bNFQ.resize(100, 30)
        self.bNFQ.move(110, 150)
        self.bNFQ.setText("~F")
        self.bNFQ.clicked.connect(self.bNFQclick)

        self.bGQ = QtWidgets.QPushButton(self)
        self.bGQ.resize(100, 30)
        self.bGQ.move(10, 180)
        self.bGQ.setText("G")
        self.bGQ.clicked.connect(self.bGQclick)

        self.bNGQ = QtWidgets.QPushButton(self)
        self.bNGQ.resize(100, 30)
        self.bNGQ.move(110, 180)
        self.bNGQ.setText("~G")
        self.bNGQ.clicked.connect(self.bNGQclick)

        self.bHQ = QtWidgets.QPushButton(self)
        self.bHQ.resize(100, 30)
        self.bHQ.move(10, 210)
        self.bHQ.setText("H")
        self.bHQ.clicked.connect(self.bHQclick)

        self.bNHQ = QtWidgets.QPushButton(self)
        self.bNHQ.resize(100, 30)
        self.bNHQ.move(110, 210)
        self.bNHQ.setText("~H")
        self.bNHQ.clicked.connect(self.bNHQclick)

        self.bLQ = QtWidgets.QPushButton(self)
        self.bLQ.resize(100, 30)
        self.bLQ.move(10, 240)
        self.bLQ.setText("L")
        self.bLQ.clicked.connect(self.bLQclick)

        self.bNLQ = QtWidgets.QPushButton(self)
        self.bNLQ.resize(100, 30)
        self.bNLQ.move(110, 240)
        self.bNLQ.setText("~L")
        self.bNLQ.clicked.connect(self.bNLQclick)

        self.bNQ = QtWidgets.QPushButton(self)
        self.bNQ.resize(100, 30)
        self.bNQ.move(10, 270)
        self.bNQ.setText("N")
        self.bNQ.clicked.connect(self.bNQclick)

        self.bNNQ = QtWidgets.QPushButton(self)
        self.bNNQ.resize(100, 30)
        self.bNNQ.move(110, 270)
        self.bNNQ.setText("~N")
        self.bNNQ.clicked.connect(self.bNNQclick)

        self.bOQ = QtWidgets.QPushButton(self)
        self.bOQ.resize(100, 30)
        self.bOQ.move(10, 300)
        self.bOQ.setText("O")
        self.bOQ.clicked.connect(self.bOQclick)

        self.bNOQ = QtWidgets.QPushButton(self)
        self.bNOQ.resize(100, 30)
        self.bNOQ.move(110, 300)
        self.bNOQ.setText("~O")
        self.bNOQ.clicked.connect(self.bNOQclick)

        self.bPQ = QtWidgets.QPushButton(self)
        self.bPQ.resize(100, 30)
        self.bPQ.move(10, 330)
        self.bPQ.setText("P")
        self.bPQ.clicked.connect(self.bPQclick)

        self.bNPQ = QtWidgets.QPushButton(self)
        self.bNPQ.resize(100, 30)
        self.bNPQ.move(110, 330)
        self.bNPQ.setText("~P")
        self.bNPQ.clicked.connect(self.bNPQclick)

        self.bRQ = QtWidgets.QPushButton(self)
        self.bRQ.resize(100, 30)
        self.bRQ.move(10, 360)
        self.bRQ.setText("R")
        self.bRQ.clicked.connect(self.bRQclick)

        self.bNRQ = QtWidgets.QPushButton(self)
        self.bNRQ.resize(100, 30)
        self.bNRQ.move(110, 360)
        self.bNRQ.setText("~R")
        self.bNRQ.clicked.connect(self.bNRQclick)

        self.bTQ = QtWidgets.QPushButton(self)
        self.bTQ.resize(100, 30)
        self.bTQ.move(10, 390)
        self.bTQ.setText("T")
        self.bTQ.clicked.connect(self.bTQclick)

        self.bNTQ = QtWidgets.QPushButton(self)
        self.bNTQ.resize(100, 30)
        self.bNTQ.move(110, 390)
        self.bNTQ.setText("~T")
        self.bNTQ.clicked.connect(self.bNTQclick)

        self.bXQ = QtWidgets.QPushButton(self)
        self.bXQ.resize(100, 30)
        self.bXQ.move(10, 420)
        self.bXQ.setText("X")
        self.bXQ.clicked.connect(self.bXQclick)

        self.bNXQ = QtWidgets.QPushButton(self)
        self.bNXQ.resize(100, 30)
        self.bNXQ.move(110, 420)
        self.bNXQ.setText("~X")
        self.bNXQ.clicked.connect(self.bNXQclick)

        self.bYQ = QtWidgets.QPushButton(self)
        self.bYQ.resize(100, 30)
        self.bYQ.move(10, 450)
        self.bYQ.setText("Y")
        self.bYQ.clicked.connect(self.bYQclick)

        self.bNYQ = QtWidgets.QPushButton(self)
        self.bNYQ.resize(100, 30)
        self.bNYQ.move(110, 450)
        self.bNYQ.setText("~Y")
        self.bNYQ.clicked.connect(self.bNYQclick)


        #########CONDITION BUTTON
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Select CONDITION")
        self.label2.adjustSize()
        self.label2.move(370, 7)

        self.bAC = QtWidgets.QPushButton(self)
        self.bAC.resize(100, 30)
        self.bAC.move(330, 30)
        self.bAC.setText("A")
        self.bAC.clicked.connect(self.bACclick)

        self.bNAC = QtWidgets.QPushButton(self)
        self.bNAC.resize(100, 30)
        self.bNAC.move(430, 30)
        self.bNAC.setText("~A")
        self.bNAC.clicked.connect(self.bNACclick)

        self.bBC = QtWidgets.QPushButton(self)
        self.bBC.resize(100, 30)
        self.bBC.move(330, 60)
        self.bBC.setText("B")
        self.bBC.clicked.connect(self.bBCclick)

        self.bNBC = QtWidgets.QPushButton(self)
        self.bNBC.resize(100, 30)
        self.bNBC.move(430, 60)
        self.bNBC.setText("~B")
        self.bNBC.clicked.connect(self.bNBCclick)

        self.bCC = QtWidgets.QPushButton(self)
        self.bCC.resize(100, 30)
        self.bCC.move(330, 90)
        self.bCC.setText("C")
        self.bCC.clicked.connect(self.bCCclick)

        self.bNCC = QtWidgets.QPushButton(self)
        self.bNCC.resize(100, 30)
        self.bNCC.move(430, 90)
        self.bNCC.setText("~C")
        self.bNCC.clicked.connect(self.bNCCclick)

        self.bDC = QtWidgets.QPushButton(self)
        self.bDC.resize(100, 30)
        self.bDC.move(330, 120)
        self.bDC.setText("D")
        self.bDC.clicked.connect(self.bDCclick)

        self.bNDC = QtWidgets.QPushButton(self)
        self.bNDC.resize(100, 30)
        self.bNDC.move(430, 120)
        self.bNDC.setText("~D")
        self.bNDC.clicked.connect(self.bNDCclick)

        self.bFC = QtWidgets.QPushButton(self)
        self.bFC.resize(100, 30)
        self.bFC.move(330, 150)
        self.bFC.setText("F")
        self.bFC.clicked.connect(self.bFCclick)

        self.bNFC = QtWidgets.QPushButton(self)
        self.bNFC.resize(100, 30)
        self.bNFC.move(430, 150)
        self.bNFC.setText("~F")
        self.bNFC.clicked.connect(self.bNFCclick)

        self.bGC = QtWidgets.QPushButton(self)
        self.bGC.resize(100, 30)
        self.bGC.move(330, 180)
        self.bGC.setText("G")
        self.bGC.clicked.connect(self.bGCclick)

        self.bNGC = QtWidgets.QPushButton(self)
        self.bNGC.resize(100, 30)
        self.bNGC.move(430, 180)
        self.bNGC.setText("~G")
        self.bNGC.clicked.connect(self.bNGCclick)

        self.bHC = QtWidgets.QPushButton(self)
        self.bHC.resize(100, 30)
        self.bHC.move(330, 210)
        self.bHC.setText("H")
        self.bHC.clicked.connect(self.bHCclick)

        self.bNHC = QtWidgets.QPushButton(self)
        self.bNHC.resize(100, 30)
        self.bNHC.move(430, 210)
        self.bNHC.setText("~H")
        self.bNHC.clicked.connect(self.bNHCclick)

        self.bLC = QtWidgets.QPushButton(self)
        self.bLC.resize(100, 30)
        self.bLC.move(330, 240)
        self.bLC.setText("L")
        self.bLC.clicked.connect(self.bLCclick)

        self.bNLC = QtWidgets.QPushButton(self)
        self.bNLC.resize(100, 30)
        self.bNLC.move(430, 240)
        self.bNLC.setText("~L")
        self.bNLC.clicked.connect(self.bNLCclick)

        self.bNC = QtWidgets.QPushButton(self)
        self.bNC.resize(100, 30)
        self.bNC.move(330, 270)
        self.bNC.setText("N")
        self.bNC.clicked.connect(self.bNCclick)

        self.bNNC = QtWidgets.QPushButton(self)
        self.bNNC.resize(100, 30)
        self.bNNC.move(430, 270)
        self.bNNC.setText("~N")
        self.bNNC.clicked.connect(self.bNNCclick)

        self.bOC = QtWidgets.QPushButton(self)
        self.bOC.resize(100, 30)
        self.bOC.move(330, 300)
        self.bOC.setText("O")
        self.bOC.clicked.connect(self.bOCclick)

        self.bNOC = QtWidgets.QPushButton(self)
        self.bNOC.resize(100, 30)
        self.bNOC.move(430, 300)
        self.bNOC.setText("~O")
        self.bNOC.clicked.connect(self.bNOCclick)

        self.bPC = QtWidgets.QPushButton(self)
        self.bPC.resize(100, 30)
        self.bPC.move(330, 330)
        self.bPC.setText("P")
        self.bPC.clicked.connect(self.bPCclick)

        self.bNPC = QtWidgets.QPushButton(self)
        self.bNPC.resize(100, 30)
        self.bNPC.move(430, 330)
        self.bNPC.setText("~P")
        self.bNPC.clicked.connect(self.bNPCclick)

        self.bRC = QtWidgets.QPushButton(self)
        self.bRC.resize(100, 30)
        self.bRC.move(330, 360)
        self.bRC.setText("R")
        self.bRC.clicked.connect(self.bRCclick)

        self.bNRC = QtWidgets.QPushButton(self)
        self.bNRC.resize(100, 30)
        self.bNRC.move(430, 360)
        self.bNRC.setText("~R")
        self.bNRC.clicked.connect(self.bNRCclick)

        self.bTC = QtWidgets.QPushButton(self)
        self.bTC.resize(100, 30)
        self.bTC.move(330, 390)
        self.bTC.setText("T")
        self.bTC.clicked.connect(self.bTCclick)

        self.bNTC = QtWidgets.QPushButton(self)
        self.bNTC.resize(100, 30)
        self.bNTC.move(430, 390)
        self.bNTC.setText("~T")
        self.bNTC.clicked.connect(self.bNTCclick)

        self.bXC = QtWidgets.QPushButton(self)
        self.bXC.resize(100, 30)
        self.bXC.move(330, 420)
        self.bXC.setText("X")
        self.bXC.clicked.connect(self.bXCclick)

        self.bNXC = QtWidgets.QPushButton(self)
        self.bNXC.resize(100, 30)
        self.bNXC.move(430, 420)
        self.bNXC.setText("~X")
        self.bNXC.clicked.connect(self.bNXCclick)

        self.bYC = QtWidgets.QPushButton(self)
        self.bYC.resize(100, 30)
        self.bYC.move(330, 450)
        self.bYC.setText("Y")
        self.bYC.clicked.connect(self.bYCclick)

        self.bNYC = QtWidgets.QPushButton(self)
        self.bNYC.resize(100, 30)
        self.bNYC.move(430, 450)
        self.bNYC.setText("~Y")
        self.bNYC.clicked.connect(self.bNYCclick)

        ##### PROBAB
        self.genQuery = QtWidgets.QPushButton(self)
        self.genQuery.setText("Generate Query and COMPUTE")
        self.genQuery.resize(250, 40)
        self.genQuery.move(640, 170)
        self.genQuery.clicked.connect(self.genQueryclicked)

        self.labelq = QtWidgets.QLabel(self)
        self.labelq.setText("Query generated: ")
        self.labelq.adjustSize()
        self.labelq.move(560, 240)

        self.showGeneratedQuery = QTextEdit(self)
        self.showGeneratedQuery.move(560, 260)
        self.showGeneratedQuery.resize(400, 50)
        self.showGeneratedQuery.setLineWrapMode(QTextEdit.NoWrap)

        self.labelqans = QtWidgets.QLabel(self)
        self.labelqans.setText("Computed Probability: ")
        self.labelqans.adjustSize()
        self.labelqans.move(560, 350)

        self.showGeneratedQueryResult = QTextEdit(self)
        self.showGeneratedQueryResult.move(560, 370)
        self.showGeneratedQueryResult.resize(400, 30)
        self.showGeneratedQueryResult.setLineWrapMode(QTextEdit.NoWrap)

        ###### MB
        self.labelmb = QtWidgets.QLabel(self)
        self.labelmb.setText("Enter Node Name\n(for markov Blanket)\n(in CAPS)")
        self.labelmb.adjustSize()
        self.labelmb.move(570, 30)

        self.enterNode = QTextEdit(self)
        self.enterNode.move(710, 30)
        self.enterNode.resize(50, 30)
        self.enterNode.setLineWrapMode(QTextEdit.NoWrap)

        self.genMarkovBlanket = QtWidgets.QPushButton(self)
        self.genMarkovBlanket.setText("Generate Markov Blanket")
        self.genMarkovBlanket.resize(200, 40)
        self.genMarkovBlanket.move(770, 25)
        self.genMarkovBlanket.clicked.connect(self.genMarkovBlanketclicked)

        self.labelmbans = QtWidgets.QLabel(self)
        self.labelmbans.setText("ANSWER: ")
        self.labelmbans.adjustSize()
        self.labelmbans.move(570, 90)

        self.showMarkovBlanket = QTextEdit(self)
        self.showMarkovBlanket.move(640, 90)
        self.showMarkovBlanket.resize(320, 50)
        self.showMarkovBlanket.setLineWrapMode(QTextEdit.NoWrap)



        self.resetB = QtWidgets.QPushButton(self)
        self.resetB.setText("RESET ALL")
        self.resetB.resize(150, 50)
        self.resetB.move(680, 440)
        self.resetB.clicked.connect(self.resetBclicked)

        ### ERROR MSG LABEL
        self.labelerr = QTextEdit(self)
        self.labelerr.setText("MESSAGE -->  ")
        self.labelerr.resize(500,30)
        self.labelerr.move(20, 500)



        # instruction
        self.instrtL = QtWidgets.QLabel(self)
        self.instrtL.setText("**** INSTRUCTIONS (INPUT FILE 1)****\n\n"
                             "1.) For Markov Blanket - Enter the correct node name (in uppercase), hit generate on side, the MARKOV BLANKET of corresponding node will appear as a list in ANSWER textbox below.\n"
                             "     (Enter another node name and hit generate as many times as required, this functionality is independent of any other button's functionality, so no need to use RESET ALL button for it.)\n\n"
                             "2.) For selecting QUERY AND CONDITION\n"
                             "      a.) Select desired query and condtion by hitting on its button.\n"
                             "      b.) You'll be able to select max of 10 query or condition, once limit reached buttons will be disabled.\n"
                             "      c.) You also cannot select same query (either positive or negetive) for query and codition, when one of the button is hit, its other corresponding buttons in query and condition are disabled.\n"
                             "      d.) After selecting, hit GENERATE QUERY AND COMPUTE button, selected query and its computed value will be displayed in corresponding textbox.\n"
                             "      e.) RESET ALL button will reset everything.\n\n"
                             "3.) ALL THE ERROR MESSAGE WILL APPEAR IN MESSAGE TEXTBOX")
        self.instrtL.move(10, 550)
        self.instrtL.adjustSize()


    def paintEvent(self, event):
        line = QPainter()
        line.begin(self)
        line.setPen(Qt.black)

        line.drawLine(550, 0, 550, 540)
        line.drawLine(0,540,980,540)
        line.drawLine(550,150,980,150)
        line.drawLine(980,0,980,540)
        line.drawLine(550, 430, 980, 430)

        line.setPen(Qt.red)
        line.drawLine(0,490,550,490)


    def bAQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("A")
            self.bAQ.setStyleSheet("color: red")
            self.bAQ.setEnabled(False)
            self.bNAQ.setEnabled(False)
            self.bAC.setEnabled(False)
            self.bNAC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNAQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~A")
            self.bNAQ.setStyleSheet("color: red")
            self.bAQ.setEnabled(False)
            self.bNAQ.setEnabled(False)
            self.bAC.setEnabled(False)
            self.bNAC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bBQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("B")
            self.bBQ.setStyleSheet("color: red")
            self.bBQ.setEnabled(False)
            self.bNAQ.setEnabled(False)
            self.bBC.setEnabled(False)
            self.bNBC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNBQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~B")
            self.bNBQ.setStyleSheet("color: red")
            self.bBQ.setEnabled(False)
            self.bNAQ.setEnabled(False)
            self.bBC.setEnabled(False)
            self.bNBC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bCQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("C")
            self.bCQ.setStyleSheet("color: red")
            self.bCQ.setEnabled(False)
            self.bNCQ.setEnabled(False)
            self.bCC.setEnabled(False)
            self.bNCC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNCQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~C")
            self.bNCQ.setStyleSheet("color: red")
            self.bCQ.setEnabled(False)
            self.bNCQ.setEnabled(False)
            self.bCC.setEnabled(False)
            self.bNCC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bDQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("D")
            self.bDQ.setStyleSheet("color: red")
            self.bDQ.setEnabled(False)
            self.bNDQ.setEnabled(False)
            self.bDC.setEnabled(False)
            self.bNDC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNDQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~D")
            self.bNDQ.setStyleSheet("color: red")
            self.bDQ.setEnabled(False)
            self.bNDQ.setEnabled(False)
            self.bDC.setEnabled(False)
            self.bNDC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bFQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("F")
            self.bFQ.setStyleSheet("color: red")
            self.bFQ.setEnabled(False)
            self.bNFQ.setEnabled(False)
            self.bFC.setEnabled(False)
            self.bNFC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNFQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~F")
            self.bNFQ.setStyleSheet("color: red")
            self.bFQ.setEnabled(False)
            self.bNFQ.setEnabled(False)
            self.bFC.setEnabled(False)
            self.bNFC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bGQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("G")
            self.bGQ.setStyleSheet("color: red")
            self.bGQ.setEnabled(False)
            self.bNGQ.setEnabled(False)
            self.bGC.setEnabled(False)
            self.bNGC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNGQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~G")
            self.bNGQ.setStyleSheet("color: red")
            self.bGQ.setEnabled(False)
            self.bNGQ.setEnabled(False)
            self.bGC.setEnabled(False)
            self.bNGC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bHQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("H")
            self.bHQ.setStyleSheet("color: red")
            self.bHQ.setEnabled(False)
            self.bNHQ.setEnabled(False)
            self.bHC.setEnabled(False)
            self.bNHC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNHQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~H")
            self.bNHQ.setStyleSheet("color: red")
            self.bHQ.setEnabled(False)
            self.bNHQ.setEnabled(False)
            self.bHC.setEnabled(False)
            self.bNHC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bLQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("L")
            self.bLQ.setStyleSheet("color: red")
            self.bLQ.setEnabled(False)
            self.bNLQ.setEnabled(False)
            self.bLC.setEnabled(False)
            self.bNLC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNLQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~L")
            self.bNLQ.setStyleSheet("color: red")
            self.bLQ.setEnabled(False)
            self.bNLQ.setEnabled(False)
            self.bLC.setEnabled(False)
            self.bNLC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("N")
            self.bNQ.setStyleSheet("color: red")
            self.bNQ.setEnabled(False)
            self.bNNQ.setEnabled(False)
            self.bNC.setEnabled(False)
            self.bNNC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNNQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~N")
            self.bNNQ.setStyleSheet("color: red")
            self.bNQ.setEnabled(False)
            self.bNNQ.setEnabled(False)
            self.bNC.setEnabled(False)
            self.bNNC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bOQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("O")
            self.bOQ.setStyleSheet("color: red")
            self.bOQ.setEnabled(False)
            self.bNOQ.setEnabled(False)
            self.bOC.setEnabled(False)
            self.bNOC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNOQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~O")
            self.bNOQ.setStyleSheet("color: red")
            self.bOQ.setEnabled(False)
            self.bNOQ.setEnabled(False)
            self.bOC.setEnabled(False)
            self.bNOC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bPQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("P")
            self.bPQ.setStyleSheet("color: red")
            self.bPQ.setEnabled(False)
            self.bNPQ.setEnabled(False)
            self.bPC.setEnabled(False)
            self.bNPC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNPQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~P")
            self.bNPQ.setStyleSheet("color: red")
            self.bPQ.setEnabled(False)
            self.bNPQ.setEnabled(False)
            self.bPC.setEnabled(False)
            self.bNPC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bRQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("R")
            self.bRQ.setStyleSheet("color: red")
            self.bRQ.setEnabled(False)
            self.bNRQ.setEnabled(False)
            self.bRC.setEnabled(False)
            self.bNRC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNRQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~R")
            self.bNRQ.setStyleSheet("color: red")
            self.bRQ.setEnabled(False)
            self.bNRQ.setEnabled(False)
            self.bRC.setEnabled(False)
            self.bNRC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bTQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("T")
            self.bTQ.setStyleSheet("color: red")
            self.bTQ.setEnabled(False)
            self.bNTQ.setEnabled(False)
            self.bTC.setEnabled(False)
            self.bNTC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNTQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~T")
            self.bNTQ.setStyleSheet("color: red")
            self.bTQ.setEnabled(False)
            self.bNTQ.setEnabled(False)
            self.bTC.setEnabled(False)
            self.bNTC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bXQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("X")
            self.bXQ.setStyleSheet("color: red")
            self.bXQ.setEnabled(False)
            self.bNXQ.setEnabled(False)
            self.bXC.setEnabled(False)
            self.bNXC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNXQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~X")
            self.bNXQ.setStyleSheet("color: red")
            self.bXQ.setEnabled(False)
            self.bNXQ.setEnabled(False)
            self.bXC.setEnabled(False)
            self.bNXC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bYQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("Y")
            self.bYQ.setStyleSheet("color: red")
            self.bYQ.setEnabled(False)
            self.bNYQ.setEnabled(False)
            self.bYC.setEnabled(False)
            self.bNYC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNYQclick(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~Y")
            self.bNYQ.setStyleSheet("color: red")
            self.bYQ.setEnabled(False)
            self.bNYQ.setEnabled(False)
            self.bYC.setEnabled(False)
            self.bNYC.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()


#### CONDITION

    def bACclick(self):
        global conditionList
        conditionList.append("A")
        self.bAC.setStyleSheet("color: red")
        self.bAQ.setEnabled(False)
        self.bNAQ.setEnabled(False)
        self.bAC.setEnabled(False)
        self.bNAC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNACclick(self):
        global conditionList
        conditionList.append("~A")
        self.bNAC.setStyleSheet("color: red")
        self.bAQ.setEnabled(False)
        self.bNAQ.setEnabled(False)
        self.bAC.setEnabled(False)
        self.bNAC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bBCclick(self):
        global conditionList
        conditionList.append("B")
        self.bBC.setStyleSheet("color: red")
        self.bBQ.setEnabled(False)
        self.bNBQ.setEnabled(False)
        self.bBC.setEnabled(False)
        self.bNBC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNBCclick(self):
        global conditionList
        conditionList.append("~B")
        self.bNBC.setStyleSheet("color: red")
        self.bBQ.setEnabled(False)
        self.bNBQ.setEnabled(False)
        self.bBC.setEnabled(False)
        self.bNBC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bCCclick(self):
        global conditionList
        conditionList.append("C")
        self.bCC.setStyleSheet("color: red")
        self.bCQ.setEnabled(False)
        self.bNCQ.setEnabled(False)
        self.bCC.setEnabled(False)
        self.bNCC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNCCclick(self):
        global conditionList
        conditionList.append("~C")
        self.bNCC.setStyleSheet("color: red")
        self.bCQ.setEnabled(False)
        self.bNCQ.setEnabled(False)
        self.bCC.setEnabled(False)
        self.bNCC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bDCclick(self):
        global conditionList
        conditionList.append("D")
        self.bDC.setStyleSheet("color: red")
        self.bDQ.setEnabled(False)
        self.bNDQ.setEnabled(False)
        self.bDC.setEnabled(False)
        self.bNDC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNDCclick(self):
        global conditionList
        conditionList.append("~D")
        self.bNDC.setStyleSheet("color: red")
        self.bDQ.setEnabled(False)
        self.bNDQ.setEnabled(False)
        self.bDC.setEnabled(False)
        self.bNDC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bFCclick(self):
        global conditionList
        conditionList.append("F")
        self.bFC.setStyleSheet("color: red")
        self.bFQ.setEnabled(False)
        self.bNFQ.setEnabled(False)
        self.bFC.setEnabled(False)
        self.bNFC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNFCclick(self):
        global conditionList
        conditionList.append("~F")
        self.bNFC.setStyleSheet("color: red")
        self.bFQ.setEnabled(False)
        self.bNFQ.setEnabled(False)
        self.bFC.setEnabled(False)
        self.bNFC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bGCclick(self):
        global conditionList
        conditionList.append("G")
        self.bGC.setStyleSheet("color: red")
        self.bGQ.setEnabled(False)
        self.bNGQ.setEnabled(False)
        self.bGC.setEnabled(False)
        self.bNGC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNGCclick(self):
        global conditionList
        conditionList.append("~G")
        self.bNGC.setStyleSheet("color: red")
        self.bGQ.setEnabled(False)
        self.bNGQ.setEnabled(False)
        self.bGC.setEnabled(False)
        self.bNGC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bHCclick(self):
        global conditionList
        conditionList.append("H")
        self.bHC.setStyleSheet("color: red")
        self.bHQ.setEnabled(False)
        self.bNHQ.setEnabled(False)
        self.bHC.setEnabled(False)
        self.bNHC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNHCclick(self):
        global conditionList
        conditionList.append("~H")
        self.bNHC.setStyleSheet("color: red")
        self.bHQ.setEnabled(False)
        self.bNHQ.setEnabled(False)
        self.bHC.setEnabled(False)
        self.bNHC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bLCclick(self):
        global conditionList
        conditionList.append("L")
        self.bLC.setStyleSheet("color: red")
        self.bLQ.setEnabled(False)
        self.bNLQ.setEnabled(False)
        self.bLC.setEnabled(False)
        self.bNLC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNLCclick(self):
        global conditionList
        conditionList.append("~L")
        self.bNLC.setStyleSheet("color: red")
        self.bLQ.setEnabled(False)
        self.bNLQ.setEnabled(False)
        self.bLC.setEnabled(False)
        self.bNLC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNCclick(self):
        global conditionList
        conditionList.append("N")
        self.bNC.setStyleSheet("color: red")
        self.bNQ.setEnabled(False)
        self.bNNQ.setEnabled(False)
        self.bNC.setEnabled(False)
        self.bNNC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNNCclick(self):
        global conditionList
        conditionList.append("~N")
        self.bNNC.setStyleSheet("color: red")
        self.bNQ.setEnabled(False)
        self.bNNQ.setEnabled(False)
        self.bNC.setEnabled(False)
        self.bNNC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bOCclick(self):
        global conditionList
        conditionList.append("O")
        self.bOC.setStyleSheet("color: red")
        self.bOQ.setEnabled(False)
        self.bNOQ.setEnabled(False)
        self.bOC.setEnabled(False)
        self.bNOC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNOCclick(self):
        global conditionList
        conditionList.append("~O")
        self.bNOC.setStyleSheet("color: red")
        self.bOQ.setEnabled(False)
        self.bNOQ.setEnabled(False)
        self.bOC.setEnabled(False)
        self.bNOC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bPCclick(self):
        global conditionList
        conditionList.append("P")
        self.bPC.setStyleSheet("color: red")
        self.bPQ.setEnabled(False)
        self.bNPQ.setEnabled(False)
        self.bPC.setEnabled(False)
        self.bNPC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNPCclick(self):
        global conditionList
        conditionList.append("~P")
        self.bNPC.setStyleSheet("color: red")
        self.bPQ.setEnabled(False)
        self.bNPQ.setEnabled(False)
        self.bPC.setEnabled(False)
        self.bNPC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bRCclick(self):
        global conditionList
        conditionList.append("R")
        self.bRC.setStyleSheet("color: red")
        self.bRQ.setEnabled(False)
        self.bNRQ.setEnabled(False)
        self.bRC.setEnabled(False)
        self.bNRC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNRCclick(self):
        global conditionList
        conditionList.append("~R")
        self.bNRC.setStyleSheet("color: red")
        self.bRQ.setEnabled(False)
        self.bNRQ.setEnabled(False)
        self.bRC.setEnabled(False)
        self.bNRC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bTCclick(self):
        global conditionList
        conditionList.append("T")
        self.bTC.setStyleSheet("color: red")
        self.bTQ.setEnabled(False)
        self.bNTQ.setEnabled(False)
        self.bTC.setEnabled(False)
        self.bNTC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNTCclick(self):
        global conditionList
        conditionList.append("~T")
        self.bNTC.setStyleSheet("color: red")
        self.bTQ.setEnabled(False)
        self.bNTQ.setEnabled(False)
        self.bTC.setEnabled(False)
        self.bNTC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bXCclick(self):
        global conditionList
        conditionList.append("X")
        self.bXC.setStyleSheet("color: red")
        self.bXQ.setEnabled(False)
        self.bNXQ.setEnabled(False)
        self.bXC.setEnabled(False)
        self.bNXC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNXCclick(self):
        global conditionList
        conditionList.append("~X")
        self.bNXC.setStyleSheet("color: red")
        self.bXQ.setEnabled(False)
        self.bNXQ.setEnabled(False)
        self.bXC.setEnabled(False)
        self.bNXC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bYCclick(self):
        global conditionList
        conditionList.append("Y")
        self.bYC.setStyleSheet("color: red")
        self.bYQ.setEnabled(False)
        self.bNYQ.setEnabled(False)
        self.bYC.setEnabled(False)
        self.bNYC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNYCclick(self):
        global conditionList
        conditionList.append("~Y")
        self.bNYC.setStyleSheet("color: red")
        self.bYQ.setEnabled(False)
        self.bNYQ.setEnabled(False)
        self.bYC.setEnabled(False)
        self.bNYC.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()


    def genQueryclicked(self):
        global queryList
        global conditionList

        if len(queryList) < 1:
            self.labelerr.setText("MESSAGE -->  Query variables should be > 1")
            return
        if len(queryList) > 10:
            self.labelerr.setText("MESSAGE -->  Query variables should be < 10")
            return
        if len(conditionList) > 10:
            self.labelerr.setText("MESSAGE -->  Condition variables should be < 10")
            return

        queryInString = createExpression(queryList,conditionList)
        probab = computeProab(bayesNetDict, queryList, conditionList)

        self.showGeneratedQueryResult.setText(str(probab))
        self.showGeneratedQuery.setText(str(queryInString))
        self.disableAllQueryButtons()
        self.disableAllConditionButtons()
        self.genQuery.setEnabled(False)



    def genMarkovBlanketclicked(self):
        node  = self.enterNode.toPlainText()
        # print(node == 'A')
        if not node[0].isalpha() or len(node)>1 or node.islower() or node.isnumeric():
            self.labelerr.setText("MESSAGE -->  PLEASE ENTER VALID NODE")
        elif node == 'A' or node == 'B' or node == 'C' or node == 'D' or node == 'F' or node == 'G' or node == 'H' or node == 'L' or node == 'N' or node == 'O' or node == 'P' or node == 'R' or node == 'T' or node == 'X' or node == 'X':
            global bayesNetDict
            var = markovBlanketGen(bayesNetDict,node)
            # self.genMarkovBlanket.setEnabled(False)
            self.showMarkovBlanket.setText(str(var))
            self.labelerr.setText("MESSAGE -->")
        else:
            self.labelerr.setText("MESSAGE -->  PLEASE ENTER VALID NODE")


    def resetBclicked(self):
        global queryList
        global conditionList
        queryList = []
        conditionList = []

        self.enableAllQueryButtons()
        self.enableAllConditionButtons()
        self.genQuery.setEnabled(True)

        self.labelerr.setText("MESSAGE -->")
        self.enterNode.setText("")
        self.showMarkovBlanket.setText("")
        self.showGeneratedQuery.setText("")
        self.showGeneratedQueryResult.setText("")

    def disableAllQueryButtons(self):
        self.bAQ.setEnabled(False)
        self.bNAQ.setEnabled(False)
        self.bBQ.setEnabled(False)
        self.bNBQ.setEnabled(False)
        self.bCQ.setEnabled(False)
        self.bNCQ.setEnabled(False)
        self.bDQ.setEnabled(False)
        self.bNDQ.setEnabled(False)
        self.bFQ.setEnabled(False)
        self.bNFQ.setEnabled(False)
        self.bGQ.setEnabled(False)
        self.bNGQ.setEnabled(False)
        self.bHQ.setEnabled(False)
        self.bNHQ.setEnabled(False)
        self.bLQ.setEnabled(False)
        self.bNLQ.setEnabled(False)
        self.bNQ.setEnabled(False)
        self.bNNQ.setEnabled(False)
        self.bOQ.setEnabled(False)
        self.bNOQ.setEnabled(False)
        self.bPQ.setEnabled(False)
        self.bNPQ.setEnabled(False)
        self.bRQ.setEnabled(False)
        self.bNRQ.setEnabled(False)
        self.bTQ.setEnabled(False)
        self.bNTQ.setEnabled(False)
        self.bXQ.setEnabled(False)
        self.bNXQ.setEnabled(False)
        self.bYQ.setEnabled(False)
        self.bNYQ.setEnabled(False)

    def disableAllConditionButtons(self):
        #########CONDITION BUTTON
        self.bAC.setEnabled(False)
        self.bNAC.setEnabled(False)
        self.bBC.setEnabled(False)
        self.bNBC.setEnabled(False)
        self.bCC.setEnabled(False)
        self.bNCC.setEnabled(False)
        self.bDC.setEnabled(False)
        self.bNDC.setEnabled(False)
        self.bFC.setEnabled(False)
        self.bNFC.setEnabled(False)
        self.bGC.setEnabled(False)
        self.bNGC.setEnabled(False)
        self.bHC.setEnabled(False)
        self.bNHC.setEnabled(False)
        self.bLC.setEnabled(False)
        self.bNLC.setEnabled(False)
        self.bNC.setEnabled(False)
        self.bNNC.setEnabled(False)
        self.bOC.setEnabled(False)
        self.bNOC.setEnabled(False)
        self.bPC.setEnabled(False)
        self.bNPC.setEnabled(False)
        self.bRC.setEnabled(False)
        self.bNRC.setEnabled(False)
        self.bTC.setEnabled(False)
        self.bNTC.setEnabled(False)
        self.bXC.setEnabled(False)
        self.bNXC.setEnabled(False)
        self.bYC.setEnabled(False)
        self.bNYC.setEnabled(False)

    def enableAllQueryButtons(self):
        self.bAQ.setEnabled(True)
        self.bNAQ.setEnabled(True)
        self.bBQ.setEnabled(True)
        self.bNBQ.setEnabled(True)
        self.bCQ.setEnabled(True)
        self.bNCQ.setEnabled(True)
        self.bDQ.setEnabled(True)
        self.bNDQ.setEnabled(True)
        self.bFQ.setEnabled(True)
        self.bNFQ.setEnabled(True)
        self.bGQ.setEnabled(True)
        self.bNGQ.setEnabled(True)
        self.bHQ.setEnabled(True)
        self.bNHQ.setEnabled(True)
        self.bLQ.setEnabled(True)
        self.bNLQ.setEnabled(True)
        self.bNQ.setEnabled(True)
        self.bNNQ.setEnabled(True)
        self.bOQ.setEnabled(True)
        self.bNOQ.setEnabled(True)
        self.bPQ.setEnabled(True)
        self.bNPQ.setEnabled(True)
        self.bRQ.setEnabled(True)
        self.bNRQ.setEnabled(True)
        self.bTQ.setEnabled(True)
        self.bNTQ.setEnabled(True)
        self.bXQ.setEnabled(True)
        self.bNXQ.setEnabled(True)
        self.bYQ.setEnabled(True)
        self.bNYQ.setEnabled(True)
        ##color
        self.bAQ.setStyleSheet("color: None")
        self.bNAQ.setStyleSheet("color: None")
        self.bBQ.setStyleSheet("color: None")
        self.bNBQ.setStyleSheet("color: None")
        self.bCQ.setStyleSheet("color: None")
        self.bNCQ.setStyleSheet("color: None")
        self.bDQ.setStyleSheet("color: None")
        self.bNDQ.setStyleSheet("color: None")
        self.bFQ.setStyleSheet("color: None")
        self.bNFQ.setStyleSheet("color: None")
        self.bGQ.setStyleSheet("color: None")
        self.bNGQ.setStyleSheet("color: None")
        self.bHQ.setStyleSheet("color: None")
        self.bNHQ.setStyleSheet("color: None")
        self.bLQ.setStyleSheet("color: None")
        self.bNLQ.setStyleSheet("color: None")
        self.bNQ.setStyleSheet("color: None")
        self.bNNQ.setStyleSheet("color: None")
        self.bOQ.setStyleSheet("color: None")
        self.bNOQ.setStyleSheet("color: None")
        self.bPQ.setStyleSheet("color: None")
        self.bNPQ.setStyleSheet("color: None")
        self.bRQ.setStyleSheet("color: None")
        self.bNRQ.setStyleSheet("color: None")
        self.bTQ.setStyleSheet("color: None")
        self.bNTQ.setStyleSheet("color: None")
        self.bXQ.setStyleSheet("color: None")
        self.bNXQ.setStyleSheet("color: None")
        self.bYQ.setStyleSheet("color: None")
        self.bNYQ.setStyleSheet("color: None")

    def enableAllConditionButtons(self):
        #########CONDITION BUTTON
        self.bAC.setEnabled(True)
        self.bNAC.setEnabled(True)
        self.bBC.setEnabled(True)
        self.bNBC.setEnabled(True)
        self.bCC.setEnabled(True)
        self.bNCC.setEnabled(True)
        self.bDC.setEnabled(True)
        self.bNDC.setEnabled(True)
        self.bFC.setEnabled(True)
        self.bNFC.setEnabled(True)
        self.bGC.setEnabled(True)
        self.bNGC.setEnabled(True)
        self.bHC.setEnabled(True)
        self.bNHC.setEnabled(True)
        self.bLC.setEnabled(True)
        self.bNLC.setEnabled(True)
        self.bNC.setEnabled(True)
        self.bNNC.setEnabled(True)
        self.bOC.setEnabled(True)
        self.bNOC.setEnabled(True)
        self.bPC.setEnabled(True)
        self.bNPC.setEnabled(True)
        self.bRC.setEnabled(True)
        self.bNRC.setEnabled(True)
        self.bTC.setEnabled(True)
        self.bNTC.setEnabled(True)
        self.bXC.setEnabled(True)
        self.bNXC.setEnabled(True)
        self.bYC.setEnabled(True)
        self.bNYC.setEnabled(True)
        #color
        self.bAC.setStyleSheet("color: None")
        self.bNAC.setStyleSheet("color: None")
        self.bBC.setStyleSheet("color: None")
        self.bNBC.setStyleSheet("color: None")
        self.bCC.setStyleSheet("color: None")
        self.bNCC.setStyleSheet("color: None")
        self.bDC.setStyleSheet("color: None")
        self.bNDC.setStyleSheet("color: None")
        self.bFC.setStyleSheet("color: None")
        self.bNFC.setStyleSheet("color: None")
        self.bGC.setStyleSheet("color: None")
        self.bNGC.setStyleSheet("color: None")
        self.bHC.setStyleSheet("color: None")
        self.bNHC.setStyleSheet("color: None")
        self.bLC.setStyleSheet("color: None")
        self.bNLC.setStyleSheet("color: None")
        self.bNC.setStyleSheet("color: None")
        self.bNNC.setStyleSheet("color: None")
        self.bOC.setStyleSheet("color: None")
        self.bNOC.setStyleSheet("color: None")
        self.bPC.setStyleSheet("color: None")
        self.bNPC.setStyleSheet("color: None")
        self.bRC.setStyleSheet("color: None")
        self.bNRC.setStyleSheet("color: None")
        self.bTC.setStyleSheet("color: None")
        self.bNTC.setStyleSheet("color: None")
        self.bXC.setStyleSheet("color: None")
        self.bNXC.setStyleSheet("color: None")
        self.bYC.setStyleSheet("color: None")
        self.bNYC.setStyleSheet("color: None")



def window():
    app = QApplication(sys.argv)
    window = GUIDriver()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    bayesNetDict = bayesNetworkGen("input1.txt")
    window()
