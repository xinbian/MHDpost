import h5py
#this file create some new datasets which were not created when ran the simulation

h5file = h5py.File('tests.h5','r+')

for variable in ['V_x','V_y','V_z','B_x','B_y','B_z','Press','converb0','conversion']:
	delimiter = ''
	mylist = ['Fields/','P', variable]
	filepath = delimiter.join(mylist)
	h5file.create_group(filepath)
h5file.close()