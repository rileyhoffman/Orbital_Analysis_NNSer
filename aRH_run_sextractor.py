
import os, sys, subprocess
import pyfits
sys.path.insert(0,'/home/student/RHoffman_Final_Project/MatchImagesgood/')
from MatchImages import *

image_path = '/home/student/RHoffman_Final_Project/'         # Location of fit images
outdir = '/home/student/RHoffman_Final_Project/sextractor_output/'       



image_list = []
for root, dirs, files in os.walk(image_path):
    for filename in files:
        if filename.endswith('.fits'):
            image_list.append(root+filename)



#Make sure to make a directory to output the .cat files
#try:
#    os.mkdir(outdir)
#except OSError as e:
#    if e.errno == 17:
#        pass
#    else:
#        raise
#catalog_list = []
#for image_location in image_list:
#    outpath=outdir+image_location.split('/')[-1].replace('.fits','.cat')
#    print "Finding stars in "+image_location.split('/')[-1]
#    conf_path = '/home/student/RHoffman_Final_Project/default.sex'  # You made need to edit the PARAMETERS_NAME or FILTER_NAME in this file
#    subprocess.call(['sex',image_location,'-c', conf_path,'-CATALOG_NAME',outpath])
#    if os.path.isfile(outpath):
#        catalog_list.append(outpath)
#    else:
#        print "Unable to make catalog file"
#    print ""

#for catalog_location in catalog_list[1:]:
#    outpath=outdir+catalog_list[0].split('/')[-1].split('.')[0]+'_'+catalog_location.split('/')[-1].split('.')[0]+'_matched.cat'
#    cat1 = catalog_list[0]
#    cat2 = catalog_location
#    print "Matching Stars from "+cat1.split('/')[-1]+" and "+cat2.split('/')[-1]
#
#    try:
#        ret = MatchImages(cat1,cat2)
#        np.savetxt(outpath, ret[0],fmt='%10.3f ')
#        np.savetxt(outpath.replace(".cat",".dict"), np.asarray(('\n'.join(['%16s::\t%s' % (key, value) for (key, value) in ret[1].items()])))[None],fmt='%s')
#        np.savetxt(outpath.replace(".cat",".param"), np.asarray(('\n'.join(['%7s::\t%s' % (key, value) for (key, value) in ret[2].items()])))[None],fmt='%s')
#    except UnboundLocalError:
#        print "\tUnable to find matching stars!"
#    print '\tDone\n'



image_time_list = []
for image_location in image_list:
    image = pyfits.open(image_location)
    # This is the Modified Julian Date of observation
    date_str = image[0].header['MJD-OBS']
    image_time_list.append(float(date_str))
    #print date_str
print image_time_list

