# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:09:02 2015

@author: michelegoe2
"""

def getcity(data):
    i = 0
    j = []
    while i < len(data):
        j.append(data[i][0])
        i += 1
    return j