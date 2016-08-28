import cv2
import numpy as np

#original image
img = cv2.imread('im.jpg')
#plt.imshow(img)
p1 = [200,200]
p2 = [300, 200]

#plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='k', linestyle='-', linewidth=2)
#plt.show()

def random_flip(im,coords):

    theta = 10
    scale = 1
    #rotate image
    [rows,cols,_] = np.shape(img)
    M = cv2.getRotationMatrix2D((cols/2,rows/2),theta,scale)
    new_img = cv2.warpAffine(img,M,(cols,rows))

    plt.imshow(new_img)
    plt.show

    return









#rotated image
[rows,cols,_] = np.shape(img)
M = cv2.getRotationMatrix2D((cols/2,rows/2),40,1)
r_img = cv2.warpAffine(img,M,(cols,rows))
plt.imshow(r_img)


M = cv2.getRotationMatrix2D((cols/2,rows/2),40,1)
print np.shape(M)
p1 = np.dot(M,[200,200,1])
p2 = np.dot(M,[300,200,1])

plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='r', linestyle='-', linewidth=2)
plt.show()







#io.imshow()
#io.show()
#plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=2)
