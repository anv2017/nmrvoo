# This Python file uses the following encoding: utf-8

import scipy as sp

class Spectrum:
    def __init__(self):
        #acquired block
        self.acblock=None
        #final block
        self.fblock=None
        #processed block
        self.pblock=None
