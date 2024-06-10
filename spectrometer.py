# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtCore import Signal

import spectrum
import scipy as sp
import numpy as np

class Spectrometer(QtCore.QObject):

    sampleloaded = Signal(spectrum.Spectrum)

    def __init__(self):
        super().__init__()
        self.spectrum=spectrum.Spectrum()

    def LoadSample(self):
        file=open("/Users/armando/spectra_cdcl3.csv","r")
        lines=file.readlines()
        self.spectrum.acblock=np.zeros( (len(lines)),dtype=complex)
        for i in range(len(lines)):
            tk=lines[i].split()
            self.spectrum.acblock[i]=complex(float(tk[1])*1000,float(tk[2])*1000)


        self.sampleloaded.emit(self.spectrum)



    def RemoveSample(self):
        pass

    def InitExperiment(self):
        self.spectrum.acblock=sp.zeros((1,16384),dtype=complex)



