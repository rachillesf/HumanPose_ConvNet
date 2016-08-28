
import glob
import numpy as np
from skimage import io
from GLOBAL import *


class Dataset:

    def __init__(self,train_path=train_path,test_path=test_path):
        self.train_path = train_path
        self.test_path = test_path
        self.filename = 'frame'
        self.filetype = '.jpg'
        self.num_files()

    def num_files(self):
        """returns number of examples on the paths given at init"""
        train_path = self.train_path + '/images/*' + self.filetype
        test_path = self.test_path + '/images/*' + self.filetype
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
            path = self.train_path
            num_files = self.train_num
        else:
            path = self.test_path
            num_files = self.test_num

        idx_list = np.random.randint(num_files,size = batch_size)
        im_batch = []
        for i in idx_list:
            im_name = path + '/images/' +  self.filename + str(i) + self.filetype
            im = io.imread(im_name)

            im_batch.append(im)

        return np.array(im_batch)
