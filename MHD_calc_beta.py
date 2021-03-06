import h5py
import numpy as np

#specify the old simulation size, it can be expanded two times each time. e.g. 4^3 to 8^3

nx=ny=nz = input("input the simulation size:")

#specify rerun_tag
istep=raw_input("input time step (in the form of 000010, for reruntag=10):")
variable=['V_x','V_y','V_z','B_x','B_y','B_z']
mylist = ['Fields/','P',variable[0],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
vx = np.array(databk)

mylist = ['Fields/','P',variable[1],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
vy = np.array(databk)

mylist = ['Fields/','P',variable[2],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
vz = np.array(databk)

mylist = ['Fields/','P',variable[3],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
bx = np.array(databk)

mylist = ['Fields/','P',variable[4],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
by = np.array(databk)

mylist = ['Fields/','P',variable[5],'/',istep]
filepath = delimiter.join(mylist)  
delimiteratabk = h5file.get(filepath)
bz = np.array(databk)
#store kinetic energy it in vx
vx=(vx*vx+vy*vy+vz*vz)/2
bx=bx*bx+by*by+bz*bz
v2_mean=np.mean(vx)
b2_mean=np.mean(bx)
beta=v2/b2

print "plasma parameter beta is ", beta
h5file.close()
