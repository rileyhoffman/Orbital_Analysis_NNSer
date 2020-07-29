import os, sys, subprocess
import pyfits
import numpy as np
import matplotlib.pyplot as plt

image_path = '/home/student/RHoffman_Final_Project/sextractor_output/'       
outdir = '/home/student/RHoffman_Final_Project/sextractor_output/'   

matchcat_list = []
for root, dirs, files in os.walk(image_path):
    for filename in files:
        if filename.endswith('matched.cat'):
            matchcat_list.append(root + '/' + filename)

f22 = []
f63 = []
f103 = []
f125 = []
f130 = []
f142 = []
f167 = []

for n in range(len(matchcat_list)):
	data = np.loadtxt(matchcat_list[n])
	flux = data[:,11]
	xpos = data[:,15]
	ypos = data[:,16]
	numb = data[:,0]
	for m in range(len(numb)):
		
		if numb[m] == 22:
			f22.append(flux[m])
		if numb[m] == 63:
			f63.append(flux[m])
		if numb[m] == 103:
			f103.append(flux[m])
		if numb[m] == 125:
			f125.append(flux[m])
		if numb[m] == 130:
			f130.append(flux[m])
		if numb[m] == 142:
			f142.append(flux[m])
		if numb[m] == 167:
			f167.append(flux[m])

b22 = []
b63 = []
b103 = []
b125 = []
b130 = []
b142 = []
b167 = []

for n in range(len(f22)):
	b22.append(305516.8)
	b63.append(31978.1)
	b103.append(18217.28)
	b125.append(110261.5)
	b130.append(2510136.0)
	b142.append(26639.45)
	b167.append(152435.0)

F22 = np.divide(f22,b22)
F63 = np.divide(f63,b63)
F103 = np.divide(f103,b103)
F125 = np.divide(f125,b125)
F130 = np.divide(f130,b130)
F142 = np.divide(f142,b142)
F167 = np.divide(f167,b167)

F = np.vstack((F22,F63,F103,F125,F130,F142,F167))
Fav = np.average(F,axis = 0)
Ff = np.insert(Fav,214,1.0)  #flux adjustment for all 303 frames


