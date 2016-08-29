
import cv2
import numpy as np


def random_flip_and_scale(img,coords,range_theta = [-20, 20],range_scale =[0.5, 1.5]):

    theta = np.random.uniform(low=range_theta[0], high=range_theta[1])
    scale = np.random.uniform(low=range_scale[0], high=range_scale[1])

    scale = 1
    [rows,cols,_] = np.shape(img)
    #rotate image by theta and scale it by scale
    M = cv2.getRotationMatrix2D((cols/2,rows/2),theta,scale) #rotation matrix
    new_img = cv2.warpAffine(img,M,(cols,rows)) #apply affine

    new_coords = []
    for coord in coords:
        pos = coord[0:2]
        val = coord[2]

        if int(val) == 1:
            #multiply rotation matrix by single coordinate
            rot = np.dot(M,[pos[0], pos[1], 1])

            #check if the new_image have valid joints annotations
            if not (rot[0] > 0 and rot[1] > 0 and rot[0] < rows and rot[1] < cols):
                return random_flip(img,coords)

            new_coords.append([rot[0], rot[1], val])

        else:
            new_coords.append(coord)


    return [new_img, new_coords]
