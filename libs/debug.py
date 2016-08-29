from input_data import *
from GLOBAL import *
import matplotlib.pyplot as plt
from draw_lines import *
from data_augmentation import *
import cv2



d = Dataset()

while True:
    [x_batch,y_batch] = d.next_batch("Train",10)
    [img, joints] = random_flip_and_scale(x_batch[0],y_batch[0])

    draw_lines(img,joints)


#io.imshow()
#io.show()
#plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=2)
