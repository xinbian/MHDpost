# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:25:53 2016

@author: Xin
#calcuate fields PDF 
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
h5file = h5py.File('tests.h5','r+')
#rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))
#b=10*np.random.randn(10) 
#plt.hist(b, bins='auto')  # plt.hist passes it's arguments to np.histogram
#plt.title("Histogram with 'auto' bins")
#plt.show()

#plt.plot(x, norm.pdf(x),'r-', lw=5, alpha=0.6, label='norm pdf')


#specify rerun_tag
istep='117012'
#'converb0_1','converb0_2','converb0_4','conversion'
for variable in ['conversion']:
	#generate magnetic conversion difference group
    delimiter = ''
	#write to hdf5 file
    mylist = ['Fields/','Pdiff',variable,'/',istep]
    filepath = delimiter.join(mylist)
    databk = h5file.get(filepath)
    np_data = np.array(databk)
    np_data = np_data.reshape(np_data.shape[0]*np_data.shape[1]*np_data.shape[2])
   
    plt.hist(np_data, bins=2000, normed='True',histtype='step', log='True')  
    plt.ylim((1E-5, 10))
    plt.xlim((-70, 70))
  #  plt.xlabel("$\overline {S}_{ij}\overline{B}_i\overline{B}_j$",
  #        fontsize=8, color='black')
    plt.xlabel("$\overline {S}_{ij}\overline{B}_i\overline{B}_j(k=16)-\overline {S}_{ij}\overline{B}_i\overline{B}_j(k=32)$",
          fontsize=8, color='black')
   # plt.ylabel("PDF of "
   #       "$\overline {S}_{ij}\overline{B}_i\overline{B}_j$",
    #      fontsize=8, color='black')
    fig = plt.gcf()
    fig.set_size_inches(3, 3)
    plt.tight_layout()
    mean = np.around(np.mean(np_data), decimals=2)
    plt.axvline(x=np.mean(np_data),color='r')
    ax = fig.add_subplot(111)
    ax.annotate('mean\n='+str(mean), xy=(mean, 1), xytext=(mean+20, 0.5),
            arrowprops=dict(arrowstyle="->"))

    titlelist = ['diff',variable,'.eps']
    title=delimiter.join(titlelist)
    plt.savefig(title, format='eps', dpi=600)
    plt.show()
h5file.close()
