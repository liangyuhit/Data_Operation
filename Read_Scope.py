# -*- coding: utf-8 -*-
'''
Created on 13.05.2019

@author: yu03
'''
import Rigol_DS4054
import matplotlib.pyplot as plt
import numpy as np
import datetime

now = datetime.datetime.now()
scope = Rigol_DS4054.RigolScope('USB0::0x1AB1::0x04B1::DS4A140800046::INSTR')
print(scope.Read_ID())