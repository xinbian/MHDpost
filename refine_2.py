import h5py
import numpy as np

#specify the old simulation size, it can be expanded two times each time. e.g. 4^3 to 8^3

nx=ny=nz = input("input the old simulation size:")

#specify rerun_tag
istep=raw_input("input reruntag (in the form of 000010, for reruntag=10):")

variable = ['FZx_p', 'FZy_p', 'FZz_p','FZx_m', 'FZy_m', 'FZz_m']

h5file = h5py.File('tests.h5','r+')
#the loop is used for 6 variables




for myvariable in variable:
      delimiter = ''
      mylist = ['CheckPoints/',myvariable,'/',istep]
      filepath = delimiter.join(mylist)
    
      databk = h5file.get(filepath)
      
      np_data = np.array(databk)
      m1 = np_data
      m2= np.zeros((2*nz, 2*ny, 2*nx+2))
      m2[0:nz/2,0:ny/2,0:nx+2]=m1[0:nz/2, 0:ny/2, 0:nx+2]
      m2[0:nz/2,3*ny/2:2*ny,0:nx+2]=m1[0:nz/2, ny/2:ny, 0:nx+2]
      m2[3*nz/2:2*nz,0:ny/2,0:nx+2]=m1[nz/2:nz, 0:ny/2, 0:nx+2]
      m2[3*nz/2:2*nz,3*ny/2:2*ny,0:nx+2]=m1[nz/2:nz, ny/2:ny, 0:nx+2]
      mylist = ['Refine/',myvariable,'/',istep]
      filepath = delimiter.join(mylist)
      h5file.create_dataset(filepath,data=m2)

h5file.close()