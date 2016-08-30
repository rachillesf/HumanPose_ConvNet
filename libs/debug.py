from input_data import *
from GLOBAL import *
import matplotlib.pyplot as plt
from draw_lines import *
from data_augmentation import *
import cv2

def random_sv(img,range = [0.25, 4]):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    r = np.random.uniform(low=range[0], high=range[1])
    hsv[1:2,:,:] = hsv[1:2,:,:]**r
    new_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return new_img



d = Dataset()

while True:
    [x_batch,y_batch] = d.next_batch("Train",10)
    [img, joints] = random_flip_and_scale(x_batch[0],y_batch[0])

    img = random_sv(img)
    plt.imshow(img)
    plt.show()
