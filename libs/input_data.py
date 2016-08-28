
import glob
import os
import numpy as np
from skimage import io
from GLOBAL import *


class Dataset:

    def __init__(self,path = data_path):
        self.xtrain_path = path + '/train_images'
        self.xtest_path = path + '/test_images'
        self.ytrain_path = path + '/train_joints.npy'
        self.ytest_path = path + '/test_joints.npy'
        self.filename = 'frame'
        self.filetype = '.jpg'
        self.check_and_load_files()


    def check_and_load_files(self):
        """check if the provided files and directories on path exists then load
            the .npy files containing the joints locations"""

        if os.path.exists(self.xtrain_path) is False:
            raise Exception('\n\n PATH ERROR: \n The provided folder does not exist: \n %s \n' %self.xtrain_path)

        if os.path.exists(self.xtest_path) is False:
            raise Exception('\n\n PATH ERROR:   \n The provided folder does not exist: \n %s \n' %self.xtest_path)

        if os.path.isfile(self.ytrain_path) is False:
            raise Exception('\n\n PATH ERROR:   \n The provided file does not exist: \n %s \n' %self.ytrain_path)

        if os.path.isfile(self.ytest_path) is False:
            raise Exception('\n\n PATH ERROR:   \n The provided file does not exist: \n %s \n' %self.ytest_path)

        #load locations .npy files
        self.ytrain = np.load(self.ytrain_path)
        self.ytest  = np.load(self.ytest_path)
        self.num_files() #get number of images in the folders
        if (len(self.ytrain) == self.train_num) is False:
            raise Exception("The number of TRAIN examples and labels are different, something is wrong with the data")

        if (len(self.ytest) == self.test_num) is False:
            raise Exception("The number of TEST examples and labels are different, something is wrong with the data")



    def num_files(self):
        """returns number of examples on the paths given at init"""
        train_path = self.xtrain_path + '/*' + self.filetype
        test_path = self.xtest_path + '/*' + self.filetype
        self.train_num = len(glob.glob(train_path))
        self.test_num = len(glob.glob(test_path))

        print 'NUMBER OF TRAINING EXAMPLES:',self.train_num
        print 'NUMBER OF TEST EXAMPLES:',self.test_num


    def next_batch(self,set,batch_size):
        """
        reads random batch from training or test set
        inputs:
            -set: string, "Train" for read from training set,
            "Test" (or whatever) for test set.
            -batch_size: amout of images to be read.
        outputs:
            im_batch: np array containing the images as
                     [num_images,rows,collumns,channels]
        """

        if (set == "train" or set == "Train"):
            path = self.xtrain_path
            num_files = self.train_num
            joints = self.ytrain
        else:
            path = self.xtest_path
            num_files = self.test_num
            joints = self.ytest
        #random list of integers
        idx_list = np.random.randint(num_files,size = batch_size)
        idx_list = np.random.choice(num_files, batch_size)

        im_batch = []
        y_batch = []
        for i in idx_list:
            im_name = path + '/' +  self.filename + str(i) + self.filetype
            im = io.imread(im_name)
            joint = joints[i]
            im_batch.append(im)
            y_batch.append(joint)

        return [np.array(im_batch),y_batch]
