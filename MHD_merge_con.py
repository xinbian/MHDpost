import h5py
import numpy as np

#join two fields to one
nx=ny=nz = input("input the simulation size:")

#specify rerun_tag
istep=raw_input("input merge time step (in the form of 000010, for reruntag=10):")

variable1 = 'Pconversion'
variable2 = 'Pconverb0'
variable3 = 'Pconmerge'

h5file = h5py.File('tests.h5','r+')

#obtain converion
delimiter = ''
mylist = ['Fields/',variable1,'/',istep]
filepath = delimiter.join(mylist)  
databk = h5file.get(filepath)
m1 = np.array(databk)
#obtain converion_B0
delimiter = ''
mylist = ['Fields/',variable2,'/',istep]
filepath = delimiter.join(mylist)  
databk = h5file.get(filepath)
m2 = np.array(databk)
#calculate merge
m3=m1+m2

#write to hdf5 file
mylist = ['Fields/',variable3,'/',istep]
filepath = delimiter.join(mylist)
h5file.create_dataset(filepath,data=m3)

h5file.close()
