#!/usr/bin/python3

'''这是一个BP神经网络的训练模块，建立BP神经网咯类实现多种神经网络的功能
   如果实现效果良好，可以参考将其搬入Study作为之后的训练模板'''

import sys
sys.path.append("..")
import MYSQL.sql as sql
from math import *
import numpy as np

class BPNet:
    def __init__(self , m , n , alpha):
        # 定义必要的参数
        self.eb = 0.01   # 误差容限
        self.iterator = 0    # 当前的迭代次数
        self.eta = 0.1    # 学习步长
        self.mc = 0.3  # 动量因子
        self.maxiter = 2000    # 最大迭代次数
        self.nhidden = int(sqrt(m + n)) + int(alpha)   # 隐含层神经元个数
        self.nOut = n
        self.nIn = m
        # 以下参数是系统的生成
        self.errorlist = []    # 存储迭代过程误差列表
        self.datamat = 0    # 训练集
        self.classlabels = 0    # 分类标签
        self.nSampNum = 0    # 样本集行数
        self.nSampDim = 0    # 样本列数
    def logistic(self , net):
        return 1.0 / (1.0 + np.exp(-net))
    def dlogit(self , net):
        return np.multiply(net , (1.0 - net))
    def errorfunc(self , inx):
        return np.sum(np.power(inx , 2)) * 0.5
    def normalize(self , datamat):
        # 数据集归一化
        [m , n] = np.shape(datamt)
        for i in range(n - 1):
            datamat[: , i] = (datamat[:,i] - mean(datamat[:,i])) / (np.std(datamat[:,i] + 1.0e-10))
            return datamat
    def loaddataset(self , filename):
        # 加载数据集
        save = sql.main(5)
        self.datamat = []    # 数据集
        self.classlabels = []    # 标志集
        for line in save:
            self.datamat.append([line[1],line[2],line[3],line[5],line[6],line[7] , 1.0])
            self.classlabels.append(line[4])
        self.datamat = np.mat(self.datamat)
        self.nSampNum  , self.nSampDim = np.shape(self.datamat)
        self.nSampDim -= 1    # 偏置值不进行计算
    def addcol(self , matrix1 , matrix2):
        # 矩阵增加新的一列
        [m1 , n1] = np.shape(matrix1)
        [m2 , n2] = np.shape(matrix2)
        if m1 != m2:
            print("Different rows can not merge into matrix")
            return 
        merge = np.zeros((m1 , n1 + n2))
        merge[: , 0:n1] = matrix1[:,0:n1]
        merge[: , n1:(n1+n2)] = matrix2[: ,0:n2]
        return merge
    def init_hiddenWB(self):
        # 隐含层参数初始化
        self.hi_w = 2 * (np.random.rand(self.nhidden , self.nSampDim) - 0.5)
        self.hi_b = 2 * (np.random.rand(self.nhidden , 1) - 0.5)
        self.hi_wb = np.mat(self.addcol(np.mat(self.hi_w) , np.mat(self.hi_b)))
    def init_outputWB(self):
        # 输出层参数初始化
        self.out_w = 2 * (np.random.rand(self.nOut , self.nhidden) - 0.5)
        self.out_b = 2 * (np.random.rand(self.nOut , 1) - 0.5)
        self.out_wb = np.mat(self.addcol(np.mat(self.out_w) , np.mat(self.out_b)))
    def BPtrain(self):
        sampin = self.datamat.T    # 每一列都是一个样本
        expected = np.mat(self.classlabels)
        self.init_hiddenWB()    # 初始化隐藏层
        self.init_outputWB()    # 初始化输出层
        for i in range(self.maxiter):
            # 主循环迭代
            # 隐藏层
            hi_input = self.hi_wb * sampin    # 生成nhidden * m的结果矩阵，保存每一个输入对每一个隐藏层的影响,每一列是一个隐藏层
            hi_output = self.logistic(hi_input)    # logistic激活
            # 隐藏层输出 : 加入隐藏层偏置
            hi_out = self.addcol(hi_output.T , np.ones((self.nSampNum , 1))).T
            # 输出层
            output_input = self.out_wb * hi_out    # 每一列是一个输出层
            output_output = self.logistic(output_input)
            # output_output : 6 * 314大小规模的矩阵
            # softmax取值
            softmax_output = []
            for i in range(np.shape(output_output)[1]):
                softmax = np.exp(output_output[:,i]) / np.sum(np.exp(output_output[:,i]))
                dis = np.where(softmax == np.max(softmax))
                softmax_output.append(dis[0][0])
            softmax_output = np.mat(softmax_output)
            
            # 误差计算
            err = expected - softmax_output    # 广播计算
            sse = self.errorfunc(err)    # 均方误差
            self.errorlist.append(sse)    # 误差统计
            if sse <= self.eb : 
                # 小于误差容限
                self.iterator = i + 1
                break

            # 反向传播
            DELTA = np.multiply(err , self.dlogit(output_output))
            delta = np.multiply(self.out_wb[:,:-1].T * DELTA , self.dlogit(output_output))
            dout_wb = DELTA * hi_out.T
            dhi_wb = delta * SampIn.T

            if i == 0:
                pass
            else:
                pass

            exit()

if __name__ == "__main__":
    p = BPNet(6,6,2)
    p.loaddataset('')
    p.BPtrain()
