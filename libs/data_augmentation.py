
import cv2
import numpy as np


def random_flip_and_scale(img,coords,range_theta = [-20, 20],range_scale =[0.5, 1.5]):

    theta = np.random.uniform(low=range_theta[0], high=range_theta[1])
    scale = np.random.uniform(low=range_scale[0], high=range_scale[1])

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
                return random_flip_and_scale(img,coords)

            new_coords.append([rot[0], rot[1], val])

        else:
            new_coords.append(coord)


    return [new_img, new_coords]


def random_sv(img):
        """changes the s and v components of the hsv image
        using random values given by range """

        #Ranges of random values used for changes
        p_range = [0.25, 0.4]
        m_range = [0.7, 1.4]
        a_range = [-0.1, 0.1]
        h_range = [-0.1, 0.1]

        
        #RGB to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


        #random values for s and v changes
        pow_s = np.random.uniform(low=p_range[0], high=p_range[1])
        pow_v = np.random.uniform(low=p_range[0], high=p_range[1])

        add_s = np.random.uniform(low=a_range[0], high=a_range[1])
        add_v = np.random.uniform(low=a_range[0], high=a_range[1])

        mul_s = np.random.uniform(low=m_range[0], high=m_range[1])
        mul_v = np.random.uniform(low=m_range[0], high=m_range[1])

        add_h = np.random.uniform(low=h_range[0], high=h_range[1])


        #apply changes to hsv values
        hsv[:,:,0] = hsv[:,:,0] + add_h
        hsv[:,:,1] = ((hsv[:,:,1]**pow_s) * mul_s) + add_s
        hsv[:,:,2] = ((hsv[:,:,2]**pow_v) * mul_v) + add_v

        #back to RGB
        new_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        return new_img
