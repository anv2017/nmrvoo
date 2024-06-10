# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QSplitter, QTabWidget, QToolBar
from PySide6.QtGui import QAction

import spectralwidget as spw
import vooapplication as vooapp
import samplewidget

class VooMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        split=QSplitter(self)
        #group tabs in student and teacher
        gtab=QTabWidget(self)
        studentabs=QTabWidget(gtab)
        teachertabs=QTabWidget(gtab)
        tabsw=samplewidget.SampleWidget(studentabs)
        studentabs.addTab(tabsw,"Sample")
        gtab.addTab(studentabs,"Student")
        gtab.addTab(teachertabs,"Teacher")
        self.spectral_widget=spw.SpectralWidget(self)
        split.addWidget(gtab)
        split.addWidget(self.spectral_widget)
        self.setCentralWidget(split)

        #connections
        spectrometer=qApp.spectrometer
        tabsw.ui._liftOnButton.clicked.connect(spectrometer.LoadSample)
        spectrometer.sampleloaded.connect(self.spectral_widget.SetSpectrum)

        self.InitToolBars()


    def InitToolBars(self):
        #view toolbar
        view_toolbar = QToolBar("View toolbar")
        self.addToolBar(view_toolbar)
        view_real_action = QAction(self)
        view_real_action.setStatusTip("Show real numbers")
        view_real_action.triggered.connect(self.spectral_widget.ShowRealValues)
        view_toolbar.addAction(view_real_action)



if __name__ == "__main__":
    app = vooapp.VooApplication([])
    window = VooMainWindow()
    window.show()
    sys.exit(app.exec())
