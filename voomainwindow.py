# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QSplitter, QTabWidget

import spectralwidget as spw
import vooapplication as vooapp
import samplewidget

class VooMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        split=QSplitter(self)
        tabs=QTabWidget(self)
        tabsw=samplewidget.SampleWidget(tabs)
        tabs.addTab(tabsw,"Sample")
        sw=spw.SpectralWidget(self)
        split.addWidget(tabs)
        split.addWidget(sw)
        self.setCentralWidget(split)

        #connections
        spectrometer=qApp.spectrometer
        tabsw.ui._liftOnButton.clicked.connect(spectrometer.LoadSample)
        spectrometer.sampleloaded.connect(sw.SetSpectrum)


if __name__ == "__main__":
    app = vooapp.VooApplication([])
    window = VooMainWindow()
    window.show()
    sys.exit(app.exec())
