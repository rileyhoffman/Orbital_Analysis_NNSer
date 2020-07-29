import os, sys, subprocess
import pyfits
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,'/home/student/RHoffman_Final_Project/')
from afluxcal_code import *

cat_path = '/home/student/RHoffman_Final_Project/sextractor_output/' 
image_path = '/home/student/RHoffman_Final_Project/'  

matchedcat_list = []
for root, dirs, files in os.walk(cat_path):
    for filename in files:
        if filename.endswith('matched.cat'):
            matchedcat_list.append(root + '/' + filename)


Fraw = []
matchnum = []


for n in range(len(matchedcat_list)):
	ndata = np.loadtxt(matchedcat_list[n])
	nflux = ndata[:,11]
	nxpos = ndata[:,15]
	nypos = ndata[:,16]
	nnumb = ndata[:,0]
	for m in range(len(ndata)):
		
		if nnumb[m] == 211:
			Fraw[n].append(nflux[m])
		if nnumb[m] != 211:
			Fraw[n].append(0.0) 
		#if nnumb[m] == 211:
		#	matchnum.append(matchedcat_list[n])

nameflux = np.vstack((matchnum,Fraw))
r = nameflux.T
nameorg = r[r[:,0].argsort()]
#print nameorg

#Frawzeros = np.insert(Fraw, (0,0),0)
print Fraw
#print Frawzeros

#now just need to multiply flux adjustment factor Ff array and raw flux Fraw array

#Fadj = np.multiply(Fraw,Ff)
#framerange = np.arange(47,350)

#image_list = []
#for root, dirs, files in os.walk(image_path):
#    for filename in files:
#        if filename.endswith('e90.fits'):
#            image_list.append(root+filename)



#You can also get a list observation times
#image_time_list = []
#for image_location in image_list:
#    image = pyfits.open(image_location)
#    # This is the Modified Julian Date of observation
#    date_str = image[0].header['MJD-OBS']
#    image_time_list.append(float(date_str))
    #print date_str



#frameflux = np.vstack((framerange,Fadj))
#imagedate = np.vstack((image_list, image_time_list))
#q = imagedate.T
#timeorg = q[q[:,1].argsort()]
#jtime = timeorg[:,1]



#plt.plot(jtime,Fadj,'bo')
#plt.axis([56785.25,56785.43,3500000,4800000])
#plt.xlabel('Julian Date')
#plt.ylabel('Adjusted flux')
#plt.title('Flux vs Time')
#plt.show()
