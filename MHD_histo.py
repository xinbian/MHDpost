# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:25:53 2016

@author: Xin
#calcuate fields PDF 
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
h5file = h5py.File('conver.h5','r+')
#rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))
#b=10*np.random.randn(10) 
#plt.hist(b, bins='auto')  # plt.hist passes it's arguments to np.histogram
#plt.title("Histogram with 'auto' bins")
#plt.show()

#plt.plot(x, norm.pdf(x),'r-', lw=5, alpha=0.6, label='norm pdf')



#specify rerun_tag
istep='174000'
norm_const = 1.0/0.2874
large_label = '$\overline {S}_{ij}\overline{B}_i\overline{B}_j$'
small_label = '${S}_{ij}{B}_i{B}_j-\overline {S}_{ij}\overline{B}_i\overline{B}_j$'



def init(istep):
   delimiter = ''
   mylist = ['Fields/','P60converion','/',istep]
   filepath = delimiter.join(mylist)
   databk = h5file.get(filepath)
   large_data = np.array(databk)

   mylist = ['diff/','P','/',istep]
   filepath = delimiter.join(mylist)
   databk = h5file.get(filepath)
   small_data = np.array(databk)

   return large_data, small_data



def visuliz(istep, data, norm_const, scale):
  
    data_2d = norm_const*data[:,:,0]
    plt.figure(1, figsize = (2.6,2.6), dpi=600)
    plt.rc('font', family='Helvetica', size=3)
    plt.imshow(data_2d, origin='none', aspect=1,
               cmap='coolwarm',vmin=-scale,vmax=scale)
    plt.colorbar()
    plt.tight_layout()
    plt.axis('off')
    plt.savefig('vis.pdf', bbox_inches='tight')
    plt.clf()
    


def hist(data, norm_const, xlabel):
    plt.clf()
    data = data.reshape(data.shape[0]*data.shape[1]*data.shape[2])
    data = norm_const*data

    plt.hist(data, bins=500, density='True',histtype='step', log='True')  
    plt.ylim((1E-8, 2*10))
    plt.xlim((-1000, 1000))
    plt.xlabel(xlabel, fontsize=10, color='black', fontname="Helvetica")

    fig = plt.gcf()
    fig.set_size_inches(2.6, 2.6)
    plt.tight_layout()
    mean = np.around(np.mean(data), decimals=2)
    plt.axvline(x=np.mean(data),color='r')
    ax = fig.add_subplot(111)
    ax.annotate('mean\n='+str(mean), xy=(mean, 1), xytext=(mean+20, 0.5),
            arrowprops=dict(arrowstyle="->"))

    delimiter = ''
    titlelist = ['pdf.eps']
    title=delimiter.join(titlelist)
    plt.savefig(title, format='eps', dpi=600)
    plt.show()



ldata, sdata = init(istep)
hist(sdata, norm_const, small_label)
visuliz(istep, sdata, norm_const, 100)


hist(ldata, norm_const, large_label)
visuliz(istep, ldata, norm_const, 20)


h5file.close()
