import h5py
import numpy as np

#calculate filtered field#
#need to specify wavenumber#

h5file = h5py.File('conver.h5','r+')
h5filetotal = h5py.File('/Volumes/turbDataDrive1/mhd_visual_conversion_1024_abcb0/k=60/conver.h5','r')

#specify rerun_tag
istep="174000"

variable = ['60converion','allconverion']
#generate magnetic conversion difference group
delimiter = ''
mylist = ['diff/','P']
filepath = delimiter.join(mylist)
#h5file.create_group(filepath)
#obtain 32, 16 and take subtraction
mylist = ['Fields/','P',variable[0],'/',istep]
filepath = delimiter.join(mylist)  
databk = h5file.get(filepath)
m1 = np.array(databk)



mylist = ['Fields/','P',variable[1],'/',istep]
filepath = delimiter.join(mylist)  
databk = h5filetotal.get(filepath)
m2 = np.array(databk)
#calculate difference
m1=m2-m1
#write to hdf5 file
mylist = ['diff/','P','/',istep]
filepath = delimiter.join(mylist)
h5file.create_dataset(filepath,data=m1)

h5file.close()
h5filetotal.close()
