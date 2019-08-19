# -*- coding: utf-8 -*-
'''
Created on 13.05.2019

@author: yu03
'''
import Rigol_DS4054
import matplotlib.pyplot as plt
import numpy as np
import datetime

def Export_Data(file_name, header, out_str):
    print('Writing Data')
    with open(file_name,'w') as fid: ######################################################################################
        fid.writelines(header)
        fid.writelines(out_str)
    print('Finish Writing')
    return


'''
    采数
'''
now = datetime.datetime.now()
scope = Rigol_DS4054.RigolScope('USB0::0x1AB1::0x04B1::DS4A140800046::INSTR')
print(scope.Read_ID())
print(scope.Read_Memory_Depth())
Data_Ch1, Data_Ch2, Memory_Depth, Fs = scope.Read()
# Data_Ch5 = scope.Read_Ch3 - scope.Read_Ch4
Data = Data_Ch1
N_Data, tau0= len(Data), 1.0/Fs  # 采样点数,采样间隔
T = N_Data*tau0 # 采样时间
timeline = np.array([x*tau0 for x in range(N_Data)]) #采样序列
 
print('Sample Rate: %e'%Fs)
print('Memory Depth: %i'%Memory_Depth)
print('Data Length: %i'%N_Data)
 
 
''' 
    输出数据
'''
file_name = 'Camera Test.txt'####################################################################################
header = ['%s\n' %file_name,
      'Local current time : %s\n' %now.strftime("%Y-%m-%d %H:%M:%S"),
      'Fs = %e (Hz)\n' %Fs,##########################################################################################################
      'Data Length: %i\n' %N_Data,############################################################################################
      'Time Scale = %e (s)\n' %T,############################################################################################
      'Channel_1: Trigger\n',############################################################################################
      'Channel_2: Flash\n',############################################################################################
      'Channel_3: XXX\n',############################################################################################
      'Channel_4: XXX\n',############################################################################################
#       'Channel_3: Demodulated S_curve (from CH_No.2)\n',############################################################################################
#       'Channel_4: Demodulated S_curve (from CH_No.1)\n',############################################################################################
#       'Data_Ch5: Difference between Channel_3 & Channel_4 (Ch3-Ch4)\n'################################################################################
      '-------------------------------------------------\n',
      ]
# out_str = ['%.4f, %.4f, %.4f, %.4f\n' %(Data_Ch1[i], Data_Ch2[i], Data_Ch3[i], Data_Ch4[i]) for i in range(len(Data))] 
# out_str = [' %.4f, %.4f, %.4f, %.4f, %.4f\n' %(Data_Ch1[i], Data_Ch2[i], Data_Ch3[i], Data_Ch4[i], Data_Ch5[i]) for i in range(len(Data))]    
out_str = ['%.4f, %.4f\n' %(Data_Ch1[i], Data_Ch2[i]) for i in range(len(Data))]    
 
''' 
    保存文件
'''
Export_Data(file_name, header, out_str)
 
 
'''
    可视化
'''
if 1:
    plt.figure(1)
         
#     plt.subplot(221)
    #     plt.plot(timeline, Data, color='blue', marker=' ', fillstyle='full', markeredgecolor='blue', markeredgewidth=0.0)
    plt.plot(Data_Ch1, color='yellow')
    plt.plot(Data_Ch2, color='cyan')
#     plt.plot(Data_Ch3, color='magenta')
#     plt.plot(Data_Ch4, color='blue')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.grid(which = 'both')
#     
#     
#     plt.subplot(222)
#     plt.plot(Data_Ch5, color='blue', marker=' ', fillstyle='full', markeredgecolor='blue', markeredgewidth=0.0)
# #     plt.plot(Data_Ch6, color='red', marker=' ', fillstyle='full', markeredgecolor='red', markeredgewidth=0.0)
#     plt.xlabel('Time [s]')
#     plt.ylabel('Voltage [V]')
#     plt.grid(which = 'both')
     
    plt.show()