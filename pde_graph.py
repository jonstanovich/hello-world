#Test file, M488 HW Graphing

import numpy as np
import matplotlib.pyplot as plt


#To find the c_n's use the following
#for phi(x) = 1 solutions
def c_gen_1(n):
  npi = np.multiply(n,np.pi);
  TL = np.divide(2.0,npi);
  TR = np.subtract(1, np.cos(npi));
  
  c_n = np.multiply(TL, TR)
  return  c_n

#For phi(x) = x, use the following for c_n's
def c_gen_x(n):
  
  return


x = np.arange(0,1,0.01)
t1 = 0.02
t2 = 0.5



