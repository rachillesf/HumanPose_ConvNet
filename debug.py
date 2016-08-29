from libs.input_data import Dataset
from libs.GLOBAL import *
from libs.draw_lines import *
from libs.data_augmentation import *
import matplotlib.pyplot as plt
import cv2



d = Dataset()

while True:
    [x_batch,y_batch] = d.next_batch("Train",10)
    [img, joints] = random_flip_and_scale(x_batch[0],y_batch[0])

    draw_lines(img,joints)
