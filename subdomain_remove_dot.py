#!/usr/bin/python
# @wareeq_shile 
# 
from sys import argv

f = open(argv[1],'r')
n = [x[:-2] for x in f.readlines()]
n_f = open(argv[1]+'_new.txt','w')
for z in n:
    n_f.write(z+"\n")
n_f.close()


    
