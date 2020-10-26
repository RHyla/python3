#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout,QLineEdit,QPushButton,QHBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QEvent
import sys

app=QApplication(sys.argv)
window=QWidget()




def Div(tmpList):
        solve=0
        tmp3=[]
        solvePlus=0
        tmp=[]
        tmp2=[]
        for j in range(0,len(tmpList)):
                Z2=tmpList[j]

                if Z2[0] == '/':
                        newZ2=Z2[1:]
                        tmp3.append(newZ2)


                if Z2[0] == '-' or Z2[0] == '+' or Z2[0].isdecimal() == True:
                        tmp3.append(Z2)

        

        
        for i in range(0,len(tmp3)):
                newT=tmp3[i]
                if newT[0] == '+' or newT[0] == '-':
                        tmp.append(newT)
                        if '+' not in tmp3[i-1] or '-' not in tmp3[i-1]:
                                tmp.append(tmp3[i-1])


             
        
        for i in tmp3:
                if i.isdecimal() == True:
                        tmp.insert(0,i)
        
        newS=" ".join(tmp).strip()
        newL=newS.split()
        print(newL)
        if len(newL) > 2:
                x=newL.pop(0)
                newL.append(x)
        #else:
        #        newL.reverse()
        print(newL)      
        newL.append(" ")
        
        solve=int(newL.pop(0))
        if len(newL) <= 3:
                for k in range(0, len(newL)):

                        if newL[k].isspace() == False:
                                solve=solve/int(newL[k])
                        if k == len(newL)-1:
                                tmp2.append(solve)


        else:
                for k in range(0, len(newL)):

                        tmpL=newL[k+1]
                        if newL[k].isspace() == False:

                                solve=solve/int(newL[k])
                                



                        if tmpL[0] == '+' or tmpL[0] == '-':
                                tmp2.append(solve)
                        if newL[k][0] == '+' or newL[k][0] == '-':
                                solve=int(newL[k])

                        if tmpL.isspace() == True:
                                tmp2.append(solve)
                                break



        for q in range(0,len(tmp2)):
                solvePlus=float(tmp2[q])+solvePlus
    
        return solvePlus







def Multiplication(tmpList):
        solvePlus=0
        solve=1
        tmp=[]
        tmp2=[]
        tmp3=[]
        
        for j in range(0,len(tmpList)):
                Z2=tmpList[j]

                if Z2[0] == '*':
                        newZ2=Z2[1:]
                        tmp3.append(newZ2)
                if Z2[0] == '-' or Z2[0] == '+' or Z2[0].isdecimal() == True:
                        tmp3.append(Z2)

        for i in range(0,len(tmp3)):
                newT=tmp3[i]
                if newT[0] == '+' or newT[0] == '-':
                        tmp.append(newT)
                        if '+' not in tmp3[i-1] or '-' not in tmp3[i-1]:
                                tmp.append(tmp3[i-1])

        for i in tmp3:
                if len(tmp3) != len(tmp):
                        tmp.insert(0,i)

        newS=" ".join(tmp).strip()
        newL=newS.split()
       # if multilist != []:
        #        if (tmp[0] != newL[0] and multiList[1] != newL[1]) and (multiList[0] != newL[1] and multiList[1] != newL[0]):
         #               firstChar=newL.pop(0)
          #              newL.append(firstChar)

        newL.append(" ")
    
        if len(newL) <= 3:
            for k in range(0, len(newL)):
                        if newL[k].isspace() == False:
                                solve=int(newL[k])*solve
                        if k == 2:
                                tmp2.append(solve)
        else:
                for k in range(0, len(newL)):
                        tmpL=newL[k+1]
                        if newL[k].isspace() == False:
                                solve=int(newL[k])*solve
            
                        if tmpL[0] == '+' or tmpL[0] == '-':
                                tmp2.append(solve)
                                solve=1
                        if tmpL.isspace() == True:
                                tmp2.append(solve)
                                solve=1
                                break


        for q in range(0,len(tmp2)):
                solvePlus=float(tmp2[q])+solvePlus

        return solvePlus



def makeListMulti(newListOfEntry):
        tmpMulti=[]
        tmpDiv=[]
        for i in range(0,len(newListOfEntry)):
                newZ=newListOfEntry[i]
                if newZ[0] == '*':
                        tmpMulti.append(newZ)
                        if '*' not in newListOfEntry[i-1]:
                                tmpMulti.append(newListOfEntry[i-1])
                if newZ[0] == '/':
                        tmpDiv.append(newZ)
                        if '/' not in newListOfEntry[i-1]:
                                tmpDiv.append(newListOfEntry[i-1])


        return tmpMulti,tmpDiv





def givChar():
    solve=0
    newNumbers=[]
    newLIST=[]
    char=window.line.text()
    sub=window.sender()
    if sub.text() == "&+":
        window.line.setText(char + "+")
    if sub.text() == "&-":
        window.line.setText(char + "-")
    if sub.text() == "&*":
        window.line.setText(char + "*")
    if sub.text() == "&/":
        window.line.setText(char + "/")
    if sub.text() == "&=":
        for i in char:
            if i.isdecimal() == True:
                newNumbers.append(i)
            if i == '-':
                newNumbers.append(" -")
            if i == '+':
                newNumbers.append(" +")
            if i == '*':
                newNumbers.append(" *")
            if i == '/':
                newNumbers.append(" /")

        
        newStringOfEntry="".join(newNumbers).strip()
        newListOfEntry=newStringOfEntry.split()
        multiList,divList=makeListMulti(newListOfEntry)
        #multiList=makeListMulti(newListOfEntry)

        if divList != []:
                y=Div(divList)
                newLIST.append(y)
        if multiList != []:
                x=Multiplication(multiList)
                newLIST.append(x)
                
        for i in newListOfEntry:
                if i not in multiList and i not in divList:
                        newLIST.append(i)
        
        for j in range(0,len(newLIST)):
                solve=float(newLIST[j])+solve


        window.lineSolve.setText(str(solve))
    
def givNumber():
    number=window.line.text()
    nadawca=window.sender()
    if nadawca.text() == "&0":
        window.line.setText(number + "0")
    if nadawca.text() == "&1":
        window.line.setText(number + "1")
    if nadawca.text() == "&2":
        window.line.setText(number + "2")
    if nadawca.text() == "&3":
        window.line.setText(number + "3")
    if nadawca.text() == "&4":
        window.line.setText(number + "4")
    if nadawca.text() == "&5":
        window.line.setText(number + "5")
    if nadawca.text() == "&6":
        window.line.setText(number + "6")
    if nadawca.text() == "&7":
        window.line.setText(number + "7")
    if nadawca.text() == "&8":
        window.line.setText(number + "8")
    if nadawca.text() == "&9":
        window.line.setText(number + "9")

def closeEvent():

    odp = QMessageBox.question(
    window,'Komunikat',
    "Czy na pewno koniec?",
    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if odp == QMessageBox.Yes:
        sys.exit()
        window.close()

    

#etykiety
label =QLabel("Podaj liczby:")
label2=QLabel("Wynik:")
#przypisanie widgetów do uładu tabelarycznego
layout=QGridLayout()
layout.addWidget(label,0,0)
layout.addWidget(label2,0,2)

window.line=QLineEdit()
window.lineSolve=QLineEdit()
window.lineSolve.readonly = True
window.lineSolve.setToolTip('Wpisz <b>liczby</b> i wpisz działanie')
layout.addWidget(window.line,1,0)
layout.addWidget(window.lineSolve,1,2)

plusBtn=QPushButton("&+")
minusBtn=QPushButton("&-")
multiBtn=QPushButton("&*")
divBtn=QPushButton("&/")
eqBtn=QPushButton("&=")
zeroBtn=QPushButton("&0")
oneBtn=QPushButton("&1")
twoBtn=QPushButton("&2")
threeBtn=QPushButton("&3")
fourBtn=QPushButton("&4")
fiveBtn=QPushButton("&5")
sixBtn=QPushButton("&6")
sevenBtn=QPushButton("&7")
eightBtn=QPushButton("&8")
nineBtn=QPushButton("&9")
endBtn=QPushButton("&Koniec")
endBtn.resize(endBtn.sizeHint())


layoutH=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH.addWidget(plusBtn)
layoutH.addWidget(minusBtn)
layoutH.addWidget(multiBtn)
layoutH.addWidget(divBtn)
layoutH.addWidget(eqBtn)
layoutH2.addWidget(zeroBtn)
layoutH2.addWidget(oneBtn)
layoutH2.addWidget(twoBtn)
layoutH2.addWidget(threeBtn)
layoutH2.addWidget(fourBtn)
layoutH2.addWidget(fiveBtn)
layoutH2.addWidget(sixBtn)
layoutH2.addWidget(sevenBtn)
layoutH2.addWidget(eightBtn)
layoutH2.addWidget(nineBtn)

layout.addLayout(layoutH,2,0,1,3)
layout.addLayout(layoutH2,3,0,1,3)
layout.addWidget(endBtn,4,0,1,3)


#przypisanie utworzonego układu
window.setLayout(layout)
endBtn.clicked.connect(closeEvent)
zeroBtn.clicked.connect(givNumber)
oneBtn.clicked.connect(givNumber)
twoBtn.clicked.connect(givNumber)
threeBtn.clicked.connect(givNumber)
fourBtn.clicked.connect(givNumber)
fiveBtn.clicked.connect(givNumber)
sixBtn.clicked.connect(givNumber)
sevenBtn.clicked.connect(givNumber)
eightBtn.clicked.connect(givNumber)
nineBtn.clicked.connect(givNumber)
plusBtn.clicked.connect(givChar)
minusBtn.clicked.connect(givChar)
multiBtn.clicked.connect(givChar)
divBtn.clicked.connect(givChar)
eqBtn.clicked.connect(givChar)

window.resize(300,300)
window.setGeometry(20,20,300,100)
window.setWindowIcon(QIcon('calculator.png'))
window.setWindowTitle("Kalkulator")

window.show()
app.exec_()
