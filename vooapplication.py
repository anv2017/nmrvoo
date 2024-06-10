# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication

import spectrometer
class VooApplication(QApplication):
    def __init__(self,args):
        super().__init__(args)
        self.spectrometer=spectrometer.Spectrometer()

