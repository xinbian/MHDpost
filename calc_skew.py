import h5py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss



h5file = h5py.File('conver.h5','r')
istep='174000'
#normalize parameters
norm_const = 1.0/0.2874

#init function
def init(istep, norm_const):
    
    delimiter = ''
#    mylist = ['Fields/','P60converion','/',istep]
#    filepath = delimiter.join(mylist)
#    databk = h5file.get(filepath)
#    large_data = np.array(databk)*norm_const

    mylist = ['diff/','P','/',istep]
    filepath = delimiter.join(mylist)
    databk = h5file.get(filepath)
    small_data = np.array(databk)*norm_const

   # return large_data#, small_data
    return small_data

def statistics(data):
    
    data = data.flatten()
    mean = np.mean(data)
    var = np.var(data)
    skew = ss.skew(data)
    
    return mean, var, skew

sdata = init(istep, norm_const)

smean, svar, sskew = statistics(sdata)

print 'small scales'
print smean, svar, sskew

#lmean, lvar, lskew = statistics(ldata)
#
#print 'large scales'
#print lmean, lvar, lskew
#



