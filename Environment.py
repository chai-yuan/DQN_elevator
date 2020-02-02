import sys, os
import serial
import numpy as np


class IO_Environment:

    def __init__(self):
        portx = "COM3"
        bps = 9600
        timex = None
        self.ser = serial.Serial(portx, bps, timeout=timex)

    def get_environment():
        number=[]
        lines=self.ser.readline()
        print(lines)
        for i in range(0,11):
            number.append(float(lines[i])-48.0)
        r=(float(lines[11])-48.0)*0.5 
        s=np.arange(number)

        return s,r

        



# #读取串口
# try:
#         portx = "COM3"
#         bps = 9600
#         # 超时设置，None：永远等待操作；
#         #         0：立即返回请求结果；
#         #        其他：等待超时时间（单位为秒）
#         timex = None
#         # 打开串口，并得到串口对象
#         ser = serial.Serial(portx, bps, timeout=timex)
#         # # 十六进制的发送
#         # result = ser.write(chr(0x06).encode("utf-8")) # 写数据
#         # print("写总字节数：", result)
#         # 十六进制的读取
#         for i in range(1,20):
#             number=[]
#             lines=ser.readline()
#             print(lines)
#             for i in range(0,11):
#                 number.append(float(lines[i])-48.0)
#             t=(float(lines[11])-48.0)*0.5 

#             number.append(float(work))
#             number.append(float(work2))
#             number.append(float(work3))
#             work3=work2
#             work2=work
#             print(number)
#             x=np.array(number)#转换为矩阵
#             print("x is:",x)
#             y=network.predict(x[np.newaxis,:])#增加一个维度（为了用上之前写的批处理库）
#             print("y is:",y)
#             work = np.argmax(y[0])
#             if(work==0):
#                 ser.write(chr(0x01).encode("utf-8")) # 写数据
#                 print("UP!!!")
#             elif(work==1):
#                 ser.write(chr(0x02).encode("utf-8")) # 写数据
#                 print("DOWN!!!")
#             else:
#                 ser.write(chr(0x03).encode("utf-8")) # 写数据
#                 print("DO NOT MOVE!!!")
#             print(t)
#             grad = network.gradient(y,t)
#             # 更新
#             for key in ('W1', 'b1', 'W2', 'b2'):
#                 network.params[key] -= learning_rate * grad[key]
#         ser.close() # 关闭串口
# except Exception as e:
#         print("error!", e)