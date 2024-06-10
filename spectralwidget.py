# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QRect, QPoint, QPointList, QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QBrush, QColor, QPen

import scipy as sp
import numpy as np

class SpectralWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.screenpoints=QPointList()
        self.spectrum=None
        self.baseline=0.8
        self.showreal=True
        self.showimag=False

    def sizeHint(self):
        return QSize(800,600)

    def SetSpectrum(self,s):
        self.spectrum=s
        self.Update()

    def paintEvent(self,event):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor("black"))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)
        self.DrawSpectrum(painter)
        painter.end()

    def resizeEvent(self,event):
        super().resizeEvent(event)
        self.Update()

    def Update(self):
        if self.spectrum == None:
            return
        #number o screen points
        screenwidth=self.rect().right()-self.rect().left()
        self.screenpoints.clear()
        self.screenpoints.reserve(screenwidth)
        npoints=len(self.spectrum.acblock)

        rblock=self.spectrum.acblock.real
        #vmax=sp.max(rblock)
        #vmim=sp.min(rblock)
        max=0
        sidx=0
        print("npoints=",npoints)
        #print(
        for i in range(npoints):
            if self.XToScreen(i) == sidx:
                re=self.spectrum.acblock[i].real
                if  abs(re) > max:
                    max = re
            else:
                #print("append",sidx,self.YToScreen(max))
                self.screenpoints.append(QPoint(sidx,self.YToScreen(max)))
                sidx+=1
                max=0

        self.update()

    def XToScreen(self,i):
        return int(i*self.rect().width()/len(self.spectrum.acblock))

    def YToScreen(self,y):
        max=np.max(self.spectrum.acblock.real)
        min=np.min(self.spectrum.acblock.real)
        #print("max-min",max,min)
        dyscreen=0.8*self.rect().height()
        scy=self.rect().top()+self.rect().height()*0.1+int((max-y)*dyscreen/(max-min))
        return scy


    def DrawSpectrum(self,p):
        #if self.screenpoints.isEmpty():
        #    return

        #print("drawing spectrum:",len(self.screenpoints))
        p.setPen(QPen(QColor("green")))

        p.drawPolyline(self.screenpoints)

    def ShowRealValues(self,b):
        self.showreal=b
        self.Update()

    def ShowImagValues(self,b):
        self.showimag=b
        self.Update()


