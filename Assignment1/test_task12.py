import os
import pandas
import numpy as np

df = pandas.read_table('task1/input.txt', sep = True, delimiter=',',header=0, encoding='utf-16', escapechar='\\', index_col=0)

def test_1():
	assert(df.shape[0]) == 225
	assert(df.shape[1]) == 31

def test_2():
	df['2010'].replace('--',0,inplace=True)
	assert(int((df[['2010']].fillna(0).astype(np.float)).sum(axis = 0))) == 7065
