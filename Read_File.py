# -*- coding: utf-8 -*-
'''
Created on 13.05.2019

@author: yu03
'''

import matplotlib.pyplot as plt
import numpy as np
import datetime

'''
    读取数据 (4通道)
'''
def Read_Data_4Ch(name):
    '''
        Return Data in File (4 Channels: Data_Ch1, Data_Ch2, Data_Ch3, Data_Ch4)
        File name required (default path)
    '''
    print('Reading Data')
    with open(name,'r') as fid:
        line=''
        while line[0:4] != '----':
            line = fid.readline()
            print(line)
            if line[0:2] == 'Fs':
                p, q, m, n = line.strip().split(' ')
                Fs = float(m)
                print('Fs = %f\n'%Fs)
        out_str = fid.readlines()
    Data_Ch1, Data_Ch2, Data_Ch3, Data_Ch4 = [], [], [], []
    for line in out_str:
        a, b, c, d= line.strip().split(', ')
        Data_Ch1.append(float(a))
        Data_Ch2.append(float(b))
        Data_Ch3.append(float(c))
        Data_Ch4.append(float(d))    
    Data_Ch1 = np.array(Data_Ch1)
    Data_Ch2 = np.array(Data_Ch2)
    Data_Ch3 = np.array(Data_Ch3)
    Data_Ch4 = np.array(Data_Ch4)
    return Data_Ch1, Data_Ch2, Data_Ch3, Data_Ch4, Fs
    
def Read_Data_2Ch(name):
    '''
        Return Data in File (4 Channels: Data_Ch1, Data_Ch2, Data_Ch3, Data_Ch4)
        File name required (default path)
    '''
    print('Reading Data')
    with open(name,'r') as fid:
        line=''
        while line[0:4] != '----':
            line = fid.readline()
            print(line)
            if line[0:2] == 'Fs':
                p, q, m, n = line.strip().split(' ')
                Fs = float(m)
                print('Fs = %f\n'%Fs)
        out_str = fid.readlines()
    Data_Ch1, Data_Ch2 = [], []
    for line in out_str:
        a, b= line.strip().split(', ')
        Data_Ch1.append(float(a))
        Data_Ch2.append(float(b))
    Data_Ch1 = np.array(Data_Ch1)
    Data_Ch2 = np.array(Data_Ch2)
    return Data_Ch1, Data_Ch2, Fs
    
    
'''
    平滑滤波
'''
def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return np.concatenate((np.zeros(N-1), (cumsum[N:] - cumsum[:-N]) / float(N)))


'''
    读取数据
'''
file_name = r'C:\Users\yu03\Desktop\Test 2019.11.18(spacer)\1st_mental_glue\3_Cavity_Test(Releasing_short_term)\16MHz_Demodulation.txt'
now = datetime.datetime.now()
Data_Ch1, Data_Ch2, Data_Ch3, Data_Ch4, Fs = Read_Data_4Ch(file_name)

Data = Data_Ch1
N_Data = len(Data)
tau0 = 1/Fs
T = N_Data*tau0
print('Sampling Rate: %e'%Fs)
print('Read length: %i'%N_Data)

# Data_Ch1 = running_mean(Data_Ch1, 100)
# Data_Ch2 = running_mean(Data_Ch2, 100)
# cutting_start = np.where(np.diff(Data_Ch2)>3)[0][1] + 1
# cutting_end = np.where(np.diff(Data_Ch2)>3)[0][-1] + 1
# print(cutting_start, cutting_end)

'''
    可视化
'''
if 1:
    plt.figure(1)
    plt.plot(Data_Ch4, label='Wavelength Sweeping', color='blue')
    plt.plot(Data_Ch1, label='Transmitted light', color='yellow')
    plt.plot(Data_Ch2, label='Reflected light', color='cyan')
    plt.plot(Data_Ch3, label='Demodulated Error Signal', color='magenta')
    
#     plt.xlim(2e5, 5e5)
#     plt.ylim(0, 3)
#     plt.xlabel('Cavity Length Scanning')
#     plt.ylabel('Voltage [V]')
    plt.grid(which = 'both')
    plt.legend(loc='best')
    plt.get_current_fig_manager().window.setGeometry(20, 50, 1000, 800)
    plt.gca().tick_params(axis='x',labelbottom=False)
    
#     plt.figure(2)
#     plt.plot(Data_Ch1[cutting_start:cutting_end], label='Trigger', color='yellow')
#     plt.plot(Data_Ch2[cutting_start:cutting_end], label='Flash', color='cyan')
    plt.show()