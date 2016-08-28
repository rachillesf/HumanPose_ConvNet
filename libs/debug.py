from input_data import *
from GLOBAL import *
import matplotlib.pyplot as plt
from draw_lines import *
import cv2


def random_flip(img,coords):

    theta = 10
    scale = 1
    #rotate image
    [rows,cols,_] = np.shape(img)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),theta,scale)
    new_img = cv2.warpAffine(img,M,(cols,rows))

    for coord in coords:
        pos = coord



    plt.imshow(new_img)
    plt.show()

    return






d = Dataset()


while True:
    [x_batch,y_batch] = d.next_batch("Train",10)
    random_flip(x_batch[0],0)




#io.imshow()
#io.show()
#plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=2)
