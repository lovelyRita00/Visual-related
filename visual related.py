# -*- coding: utf-8 -*-
"""
Created on 2018/12/3
Python 3.6

Dependency: 

How to use:

Code Performance:

Input data:  
    
Usage: 和可视化相关的常用小方法，例如颜色值转化 (provided by Wen Li)，matplotlib.pyplot 各种参数设置
    
Methods:
    * 
    * 
        

@author: Qian Pan
@e-mail: qianpan_93@163.com
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def hex2rgb(hexcolor):
    """
    把十六进制颜色转化为RGB,
    如 #6F1958,返回[111, 25, 88]
    :param hexcolor: 以#开头，例如: #6F1958
    :return: list
    """
    hexcolor = hexcolor[1:] if '#' in hexcolor else hexcolor[:]
    hexcolor = int('0x' + hexcolor, base=16)

    rgb = [(hexcolor >> 16) & 0xff,
           (hexcolor >> 8) & 0xff,
           hexcolor & 0xff]
    return rgb


def rgb2hex(rgb):
    """
    把RGB颜色转化为十六进制颜色
    例如：[111, 25, 88] 返回 #6F1958
    :param rgb: list like,例如[255,255,255]
    :return: str, hex color
    """
    hexcolor = '#'
    for each in rgb:
        hex_each = hex(each)[2:].upper()
        if len(hex_each) < 2:
            hex_each += '0'
        hexcolor += hex_each
    return hexcolor


def plot_style(ax):
    """
    设置坐标轴风格设置
    :param ax:
    :return:
    """
    label_font = {'family': 'Arial', 'weight': 'medium', 'size': 24, 'style': 'italic'}
    ax.set_xlabel(r'$xlabel$', fontdict=label_font)
    ax.set_ylabel(r'$ylabel$', fontdict=label_font)

    title_font = {'family': 'Arial', 'weight': 'medium', 'size': 26}
    ax.set_title("Title", fontdict=title_font)

    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)

    ax.tick_params(axis='both', direction='in', top=True, right=True, which='major', width=1.8, length=7,
                   pad=5)
    ax.tick_params(axis='both', direction='in', top=True, right=True, which='minor', width=1.5, length=4.5)

    plt.xticks(fontproperties='Arial', fontsize=20, weight='medium')
    plt.yticks(fontproperties='Arial', fontsize=20, weight='medium')

    ax.set_xlim([ax.get_xlim()[0], ax.get_xlim()[1]])
    xmajorlocator = MultipleLocator(0.1)
    xminorlocator = MultipleLocator(0.05)
    ax.xaxis.set_major_locator(xmajorlocator)
    ax.xaxis.set_minor_locator(xminorlocator)

    ax.set_ylim([ax.get_ylim()[0], ax.get_ylim()[1]])
    ymajorlocator = MultipleLocator(0.1)
    yminorlocator = MultipleLocator(0.05)
    ax.yaxis.set_major_locator(ymajorlocator)
    ax.yaxis.set_minor_locator(yminorlocator)
