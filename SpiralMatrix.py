# -*- coding: utf-8 -*- 
# @Author: wacat  
# @Date: 2020-09-22 16:30:59  
# @Last Modified by:   wacat  
# @Last Modified time: 2020-09-22 16:30:59


import numpy as np
import math


#螺旋遍历函数
def spiral(matrix_sr):
    #遍历后的存储容器
    spiral_list = []
    #计算矩阵的四边长度
    row_num,column_num = np.shape(matrix_sr)
    #遍历圈数
    max_iterations = math.ceil(row_num/2)
    #iterations list
    iterations_list = [it for it in range(0,max_iterations)]
    #上水平遍历函数
    def top_Horizontal_spiral(n,m):
        for i in range(n,column_num-m):
            a = matrix_sr[n,i]
            spiral_list.append(a)
        return spiral_list


    #右垂直遍历函数
    def right_vertical_spiral(n,m):
        for j in range(n,row_num-m):
            b = matrix_sr[j,-n-1]
            spiral_list.append(b)
        return spiral_list

    
    #下水平遍历函数
    def blow_Horizontal_spiral(n,m):
        for k in range(n,column_num-m):
            c = matrix_sr[-m,-k-1]
            spiral_list.append(c)
        return spiral_list


    #左垂直遍历函数
    def left_vertical_spiral(n,m):
        for q in range(n,row_num-m):
            d = matrix_sr[-q-1,m-1]
            spiral_list.append(d)
        return spiral_list
    
    for spiralID in iterations_list:
       top_Horizontal_spiral(spiralID,spiralID+1)
       right_vertical_spiral(spiralID,spiralID+1)
       blow_Horizontal_spiral(spiralID,spiralID+1)
       left_vertical_spiral(spiralID,spiralID+1)

    return print('The spiral matrix is {0}'.format(spiral_list))


if __name__ == '__main__':
    #np.matrix生成一个n*m的矩阵
    matrix_sr = np.matrix([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]])
    spiral(matrix_sr)