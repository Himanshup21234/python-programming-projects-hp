#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df=pd.read_csv('C:\\Users\\Himanshu Pant\\Documents\\bezdekIris.txt',sep=",").T
df.to_csv('C:\\Users\\Himanshu Pant\\Documents\\bezdekIris.csv',index=True,header=False)
