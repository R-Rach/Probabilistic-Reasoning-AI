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


class GUIDriver2(QMainWindow):

    def __init__(self):
        super(GUIDriver2, self).__init__()
        self.setGeometry(0, 30, 1450, 810)
        self.setWindowTitle("AI Assignment 6")

        self.initGUI2()


    def initGUI2(self):
        # QUERY B
        self.bAQ2 = QtWidgets.QPushButton(self)
        self.bNAQ2 = QtWidgets.QPushButton(self)
        self.bBQ2 = QtWidgets.QPushButton(self)
        self.bNBQ2 = QtWidgets.QPushButton(self)
        self.bEQ2 = QtWidgets.QPushButton(self)
        self.bNEQ2 = QtWidgets.QPushButton(self)
        self.bJQ2 = QtWidgets.QPushButton(self)
        self.bNJQ2 = QtWidgets.QPushButton(self)
        self.bMQ2 = QtWidgets.QPushButton(self)
        self.bNMQ2 = QtWidgets.QPushButton(self)
        # COND B
        self.bAC2 = QtWidgets.QPushButton(self)
        self.bNAC2 = QtWidgets.QPushButton(self)
        self.bBC2 = QtWidgets.QPushButton(self)
        self.bNBC2 = QtWidgets.QPushButton(self)
        self.bEC2 = QtWidgets.QPushButton(self)
        self.bNEC2 = QtWidgets.QPushButton(self)
        self.bJC2 = QtWidgets.QPushButton(self)
        self.bNJC2 = QtWidgets.QPushButton(self)
        self.bMC2 = QtWidgets.QPushButton(self)
        self.bNMC2 = QtWidgets.QPushButton(self)

        #QUERY B
        self.bAQ2.resize(100, 30)
        self.bAQ2.move(10, 30)
        self.bAQ2.setText("A")
        self.bAQ2.clicked.connect(self.bAQ2click)

        self.bNAQ2.resize(100, 30)
        self.bNAQ2.move(110, 30)
        self.bNAQ2.setText("~A")
        self.bNAQ2.clicked.connect(self.bNAQ2click)

        self.bBQ2.resize(100, 30)
        self.bBQ2.move(10, 60)
        self.bBQ2.setText("B")
        self.bBQ2.clicked.connect(self.bBQ2click)

        self.bNBQ2.resize(100, 30)
        self.bNBQ2.move(110, 60)
        self.bNBQ2.setText("~B")
        self.bNBQ2.clicked.connect(self.bNBQ2click)

        self.bEQ2.resize(100, 30)
        self.bEQ2.move(10, 90)
        self.bEQ2.setText("E")
        self.bEQ2.clicked.connect(self.bEQ2click)

        self.bNEQ2.resize(100, 30)
        self.bNEQ2.move(110, 90)
        self.bNEQ2.setText("~E")
        self.bNEQ2.clicked.connect(self.bNEQ2click)

        self.bJQ2.resize(100, 30)
        self.bJQ2.move(10, 120)
        self.bJQ2.setText("J")
        self.bJQ2.clicked.connect(self.bJQ2click)

        self.bNJQ2.resize(100, 30)
        self.bNJQ2.move(110, 120)
        self.bNJQ2.setText("~J")
        self.bNJQ2.clicked.connect(self.bNJQ2click)

        self.bMQ2.resize(100, 30)
        self.bMQ2.move(10, 150)
        self.bMQ2.setText("M")
        self.bMQ2.clicked.connect(self.bMQ2click)

        self.bNMQ2.resize(100, 30)
        self.bNMQ2.move(110, 150)
        self.bNMQ2.setText("~M")
        self.bNMQ2.clicked.connect(self.bNMQ2click)

        #COND B
        self.bAC2.resize(100, 30)
        self.bAC2.move(330, 30)
        self.bAC2.setText("A")
        self.bAC2.clicked.connect(self.bAC2click)

        self.bNAC2.resize(100, 30)
        self.bNAC2.move(430, 30)
        self.bNAC2.setText("~A")
        self.bNAC2.clicked.connect(self.bNAC2click)

        self.bBC2.resize(100, 30)
        self.bBC2.move(330, 60)
        self.bBC2.setText("B")
        self.bBC2.clicked.connect(self.bBC2click)

        self.bNBC2.resize(100, 30)
        self.bNBC2.move(430, 60)
        self.bNBC2.setText("~B")
        self.bNBC2.clicked.connect(self.bNBC2click)

        self.bEC2.resize(100, 30)
        self.bEC2.move(330, 90)
        self.bEC2.setText("E")
        self.bEC2.clicked.connect(self.bEC2click)

        self.bNEC2.resize(100, 30)
        self.bNEC2.move(430, 90)
        self.bNEC2.setText("~E")
        self.bNEC2.clicked.connect(self.bNEC2click)

        self.bJC2.resize(100, 30)
        self.bJC2.move(330, 120)
        self.bJC2.setText("J")
        self.bJC2.clicked.connect(self.bJC2click)

        self.bNJC2.resize(100, 30)
        self.bNJC2.move(430, 120)
        self.bNJC2.setText("~J")
        self.bNJC2.clicked.connect(self.bNJC2click)

        self.bMC2.resize(100, 30)
        self.bMC2.move(330, 150)
        self.bMC2.setText("M")
        self.bMC2.clicked.connect(self.bMC2click)

        self.bNMC2.resize(100, 30)
        self.bNMC2.move(430, 150)
        self.bNMC2.setText("~M")
        self.bNMC2.clicked.connect(self.bNMC2click)

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
        self.instrtL.setText("**** INSTRUCTIONS (INPUT FILE 2)****\n\n"
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


    ############# FOR INPUT 2

    def bAQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("A")
            self.bAQ2.setStyleSheet("color: red")
            self.bAQ2.setEnabled(False)
            self.bNAQ2.setEnabled(False)
            self.bAC2.setEnabled(False)
            self.bNAC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNAQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~A")
            self.bNAQ2.setStyleSheet("color: red")
            self.bAQ2.setEnabled(False)
            self.bNAQ2.setEnabled(False)
            self.bAC2.setEnabled(False)
            self.bNAC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bBQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("B")
            self.bBQ2.setStyleSheet("color: red")
            self.bBQ2.setEnabled(False)
            self.bNBQ2.setEnabled(False)
            self.bBC2.setEnabled(False)
            self.bNBC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNBQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~B")
            self.bNBQ2.setStyleSheet("color: red")
            self.bBQ2.setEnabled(False)
            self.bNBQ2.setEnabled(False)
            self.bBC2.setEnabled(False)
            self.bNBC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bEQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("E")
            self.bEQ2.setStyleSheet("color: red")
            self.bEQ2.setEnabled(False)
            self.bNEQ2.setEnabled(False)
            self.bEC2.setEnabled(False)
            self.bNEC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNEQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~E")
            self.bNEQ2.setStyleSheet("color: red")
            self.bEQ2.setEnabled(False)
            self.bNEQ2.setEnabled(False)
            self.bEC2.setEnabled(False)
            self.bNEC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bJQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("J")
            self.bJQ2.setStyleSheet("color: red")
            self.bJQ2.setEnabled(False)
            self.bNJQ2.setEnabled(False)
            self.bJC2.setEnabled(False)
            self.bNJC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNJQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~J")
            self.bNJQ2.setStyleSheet("color: red")
            self.bJQ2.setEnabled(False)
            self.bNJQ2.setEnabled(False)
            self.bJC2.setEnabled(False)
            self.bNJC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bMQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("M")
            self.bMQ2.setStyleSheet("color: red")
            self.bMQ2.setEnabled(False)
            self.bNMQ2.setEnabled(False)
            self.bMC2.setEnabled(False)
            self.bNMC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    def bNMQ2click(self):
        global queryList
        if len(queryList) == 10:
            self.disableAllQueryButtons()
        else:
            queryList.append("~M")
            self.bNMQ2.setStyleSheet("color: red")
            self.bMQ2.setEnabled(False)
            self.bNMQ2.setEnabled(False)
            self.bMC2.setEnabled(False)
            self.bNMC2.setEnabled(False)
        if len(queryList) == 10:
            self.disableAllQueryButtons()

    #cond
    def bAC2click(self):
        global conditionList
        conditionList.append("A")
        self.bAC2.setStyleSheet("color: red")
        self.bAQ2.setEnabled(False)
        self.bNAQ2.setEnabled(False)
        self.bAC2.setEnabled(False)
        self.bNAC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNAC2click(self):
        global conditionList
        conditionList.append("~A")
        self.bNAC2.setStyleSheet("color: red")
        self.bAQ2.setEnabled(False)
        self.bNAQ2.setEnabled(False)
        self.bAC2.setEnabled(False)
        self.bNAC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bBC2click(self):
        global conditionList
        conditionList.append("B")
        self.bBC2.setStyleSheet("color: red")
        self.bBQ2.setEnabled(False)
        self.bNBQ2.setEnabled(False)
        self.bBC2.setEnabled(False)
        self.bNBC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNBC2click(self):
        global conditionList
        conditionList.append("~B")
        self.bNBC2.setStyleSheet("color: red")
        self.bBQ2.setEnabled(False)
        self.bNBQ2.setEnabled(False)
        self.bBC2.setEnabled(False)
        self.bNBC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bEC2click(self):
        global conditionList
        conditionList.append("E")
        self.bEC2.setStyleSheet("color: red")
        self.bEQ2.setEnabled(False)
        self.bNEQ2.setEnabled(False)
        self.bEC2.setEnabled(False)
        self.bNEC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNEC2click(self):
        global conditionList
        conditionList.append("~E")
        self.bNEC2.setStyleSheet("color: red")
        self.bEQ2.setEnabled(False)
        self.bNEQ2.setEnabled(False)
        self.bEC2.setEnabled(False)
        self.bNEC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bJC2click(self):
        global conditionList
        conditionList.append("J")
        self.bJC2.setStyleSheet("color: red")
        self.bJQ2.setEnabled(False)
        self.bNJQ2.setEnabled(False)
        self.bJC2.setEnabled(False)
        self.bNJC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNJC2click(self):
        global conditionList
        conditionList.append("~J")
        self.bNJC2.setStyleSheet("color: red")
        self.bJQ2.setEnabled(False)
        self.bNJQ2.setEnabled(False)
        self.bJC2.setEnabled(False)
        self.bNJC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bMC2click(self):
        global conditionList
        conditionList.append("M")
        self.bMC2.setStyleSheet("color: red")
        self.bMQ2.setEnabled(False)
        self.bNMQ2.setEnabled(False)
        self.bMC2.setEnabled(False)
        self.bNMC2.setEnabled(False)
        if len(conditionList) == 10:
            self.disableAllConditionButtons()

    def bNMC2click(self):
        global conditionList
        conditionList.append("~M")
        self.bNMC2.setStyleSheet("color: red")
        self.bMQ2.setEnabled(False)
        self.bNMQ2.setEnabled(False)
        self.bMC2.setEnabled(False)
        self.bNMC2.setEnabled(False)
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
        elif node == 'A' or node == 'B' or node == 'E' or node == 'J' or node == 'M' :
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

        self.bAQ2.setEnabled(False)
        self.bNAQ2.setEnabled(False)
        self.bBQ2.setEnabled(False)
        self.bNBQ2.setEnabled(False)
        self.bEQ2.setEnabled(False)
        self.bNEQ2.setEnabled(False)
        self.bJQ2.setEnabled(False)
        self.bNJQ2.setEnabled(False)
        self.bMQ2.setEnabled(False)
        self.bNMQ2.setEnabled(False)

    def disableAllConditionButtons(self):

        self.bAC2.setEnabled(False)
        self.bNAC2.setEnabled(False)
        self.bBC2.setEnabled(False)
        self.bNBC2.setEnabled(False)
        self.bEC2.setEnabled(False)
        self.bNEC2.setEnabled(False)
        self.bJC2.setEnabled(False)
        self.bNJC2.setEnabled(False)
        self.bMC2.setEnabled(False)
        self.bNMC2.setEnabled(False)



    def enableAllQueryButtons(self):

        self.bAQ2.setEnabled(True)
        self.bNAQ2.setEnabled(True)
        self.bBQ2.setEnabled(True)
        self.bNBQ2.setEnabled(True)
        self.bEQ2.setEnabled(True)
        self.bNEQ2.setEnabled(True)
        self.bJQ2.setEnabled(True)
        self.bNJQ2.setEnabled(True)
        self.bMQ2.setEnabled(True)
        self.bNMQ2.setEnabled(True)

        self.bAQ2.setStyleSheet("color: None")
        self.bNAQ2.setStyleSheet("color: None")
        self.bBQ2.setStyleSheet("color: None")
        self.bNBQ2.setStyleSheet("color: None")
        self.bEQ2.setStyleSheet("color: None")
        self.bNEQ2.setStyleSheet("color: None")
        self.bJQ2.setStyleSheet("color: None")
        self.bNJQ2.setStyleSheet("color: None")
        self.bMQ2.setStyleSheet("color: None")
        self.bNMQ2.setStyleSheet("color: None")



    def enableAllConditionButtons(self):

        self.bAC2.setEnabled(True)
        self.bNAC2.setEnabled(True)
        self.bBC2.setEnabled(True)
        self.bNBC2.setEnabled(True)
        self.bEC2.setEnabled(True)
        self.bNEC2.setEnabled(True)
        self.bJC2.setEnabled(True)
        self.bNJC2.setEnabled(True)
        self.bMC2.setEnabled(True)
        self.bNMC2.setEnabled(True)

        self.bAC2.setStyleSheet("color: None")
        self.bNAC2.setStyleSheet("color: None")
        self.bBC2.setStyleSheet("color: None")
        self.bNBC2.setStyleSheet("color: None")
        self.bEC2.setStyleSheet("color: None")
        self.bNEC2.setStyleSheet("color: None")
        self.bJC2.setStyleSheet("color: None")
        self.bNJC2.setStyleSheet("color: None")
        self.bMC2.setStyleSheet("color: None")
        self.bNMC2.setStyleSheet("color: None")



def window():
    app = QApplication(sys.argv)
    window = GUIDriver2()

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    bayesNetDict = bayesNetworkGen("input2.txt")
    window()
