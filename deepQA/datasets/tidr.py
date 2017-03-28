from __future__ import absolute_import
import numpy as np
import sys
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import cPickle as pickle
import re
from scipy import linalg
import scipy.ndimage as ndi
from six.moves import range
from keras import backend as K
from PIL import Image
import threading
import warnings
import theano

def load_data():
    dirname='/Users/rwa56/Downloads/tid2013/'
    distortion='distorted_images/'
    reference='reference_images/'
    score='mos.txt'

    size= 256, 256


    DistortLabel = np.zeros((3000,3), dtype='float32')
    RefLabel = np.zeros((25,1), dtype='float32')
    label = [0, 0, 0]

    DistortImg = np.zeros((3000, 256,256,3), dtype='uint8')
    RefImg = np.zeros((25,256,256,3), dtype='uint8')
    i = 0

    for root, dirs, filenames in os.walk(dirname+distortion):
        for imgfile in filenames:

            img = Image.open(root+imgfile, 'r')
            #print img.getbands()
            #x = img_to_array(img)
            #img.thumbnail(size, Image.ANTIALIAS)
            img.thumbnail((256,256), Image.ANTIALIAS)

            img = ImageOps.fit(img,(256,256), Image.ANTIALIAS)
            if i == 0:
                img.show()
            #resizeimage.resize_cover(img, [256, 256])
            #ImageOps.fit(img, size, Image.ANTIALIAS)
            #img = tf.image.resize_images(img, size)
           # testimg = np.asarray(img, dtype='float32')
           # print testimg.shape

            DistortImg[i,:,:,:] = np.asarray(img, dtype='float32')
            #x = x.reshape((1,) + x.shape)
            #print 'The imgfile is' +imgfile
        #    x = 0.2126 * x0[:,:,0] + 0.7152 * x0[:,:,1] + 0.0722 * x0[:,:,2]
            #print  x.shape

            if(len(imgfile) < 12):
                print 'The file: ' + imgfile
            DistortLabel[i,0] = int(imgfile[1:3])
            DistortLabel[i,1] = int(imgfile[4:6])
            DistortLabel[i,2] = int(imgfile[7])

            i = i + 1
            #print label


    j = 0

    for root, dirs, filenames in os.walk(dirname+reference):
        for imgfile in filenames:
            #print filename
            img = Image.open(root+imgfile, 'r')
            #print img.getbands()
            #x = img_to_array(img)
            #img.thumbnail(size, Image.ANTIALIAS)
            img.thumbnail((256,256), Image.ANTIALIAS)

            img = ImageOps.fit(img,(256,256), Image.ANTIALIAS)

            RefImg[j,:,:,:] = np.asarray(img, dtype='float32')
            #x = x.reshape((1,) + x.shape)
            #print 'The imgfile is' +imgfile
    #        x = 0.2126 * x0[:,:,0] + 0.7152 * x0[:,:,1] + 0.0722 * x0[:,:,2]

            RefLabel[j] = int(imgfile[1:3])
            #RefLabel.append(label)
            #print label
            j = j + 1


    ScoreLabel = open(dirname+score).read().splitlines()
    ScoreLabel = map(float, ScoreLabel)
    #print ScoreLabel

    #print DistortImg[1]

    return DistortImg, DistortLabel, RefImg, RefLabel, ScoreLabel


def main():
    load_data()

    return 0

if __name__ == '__main__':
    sys.exit(main())
