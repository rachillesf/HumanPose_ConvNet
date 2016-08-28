from input_data import *
from GLOBAL import *
import matplotlib.pyplot as plt

d = Dataset()

def make_joints_dict(joint):

    joint_name = ['r_ankle', 'r_knee', 'r_hip', 'l_hip', 'l_knee','l_ankle','r_wrist',
                'r_elbow','r_shoulder','l_shoulder','l_elbow','l_wrist','neck','head']

    joints_dict = {}
    for (i,name) in zip(range(14), joint_name):
        joints_dict[name] = joint[i]
    return joints_dict

def draw(pos1,pos2):
    """ draw line if p1 and p2 are valid points"""

    if (pos1[2] == 1) and (pos2[2] == 1):
        plt.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], color='k', linestyle='-', linewidth=2)
        return
    else:
        return

def draw_lines(im,joints_dict):
    plt.imshow(im)

    #first line r_ankle to r_knee
    p1 = joints_dict['r_ankle']
    p2 = joints_dict['r_knee']
    draw(p1,p2)

    p1 = joints_dict['r_knee']
    p2 = joints_dict['r_hip']
    draw(p1,p2)

    p1 = joints_dict['r_hip']
    p2 = joints_dict['l_hip']
    draw(p1,p2)

    p1 = joints_dict['l_hip']
    p2 = joints_dict['l_knee']
    draw(p1,p2)

    p1 = joints_dict['l_knee']
    p2 = joints_dict['l_ankle']
    draw(p1,p2)

    p1 = joints_dict['l_hip']
    p2 = joints_dict['l_shoulder']
    draw(p1,p2)




    plt.show()
    return


while True:
    [x_batch,y_batch] = d.next_batch("Train",10)
    y = y_batch[0]
    dict = make_joints_dict(y)
    draw_lines(x_batch[0],dict)


#io.imshow()
#io.show()
#plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=2)
