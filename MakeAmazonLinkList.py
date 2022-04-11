#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:41:24 2022

@author: woutervandermeij
"""
import re

def MakeAmazonLink(SearchWord):
    SearchWord=re.sub('\s+', '+', SearchWord)  
    sLink='https://amazon.com/s?k='
    sLink=sLink+SearchWord
   
    return sLink

vSearchList=['cooking pot', 'socks', 'food and spices' ]

vLinklist=list()

for item in vSearchList:
    sAmazonLink=MakeAmazonLink(item)
    vLinklist.append(sAmazonLink)

print(vLinklist)
    