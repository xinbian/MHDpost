import h5py
import numpy as np

#calculate filtered field#
#need to specify wavenumber#

nx=ny=nz = input("input the simulation size:")

#specify rerun_tag
istep=raw_input("input merge time step (in the form of 000010, for reruntag=10):")

for variable in ['converb0_1','converb0_2','converb0_4','conversion']:
	#generate magnetic conversion difference group
	delimiter = ''
	mylist = ['diff/','P', variable]
	filepath = delimiter.join(mylist)
	h5file.create_group(filepath)
	#obtain 32, 16 and take subtraction
	mylist = ['Fields/','32',variable,'/',istep]
	filepath = delimiter.join(mylist)  
	delimiteratabk = h5file.get(filepath)
	m1 = np.array(databk)
	#obtain converion_B0
	mylist = ['Fields/','16',variable,'/',istep]
	filepath = delimiter.join(mylist)  
	databk = h5file.get(filepath)
	m2 = np.array(databk)
	#calculate difference
	m1=m1-m2
	#write to hdf5 file
	mylist = ['diff/',variable,'/',istep]
	filepath = delimiter.join(mylist)
	h5file.create_dataset(filepath,data=m1)

h5file.close()
