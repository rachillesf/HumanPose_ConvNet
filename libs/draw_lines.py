import matplotlib.pyplot as plt


"""""
this module is meant for displaying the body joints annotations
the draw_lines function receive am image and a list of anotations were each
one is in shape [ x,y,is_visible ].
"""



def make_joints_dict(joint,dataset = 'FLIC'):

    if dataset == 'Leeds' or dataset == 'LEEDS' or dataset == 'lsp':
        joint_name = ['r_ankle', 'r_knee', 'r_hip', 'l_hip', 'l_knee','l_ankle','r_wrist',
                    'r_elbow','r_shoulder','l_shoulder','l_elbow','l_wrist','neck','head']
        joint_number = 14

    if dataset == 'FLIC' or dataset == 'flic':
        joint_name = ['l_shoulder', 'l_elbow','l_wrist','r_shoulder','r_elbow','r_wrist',
                    'l_hip','r_hip','head','neck']
        joint_number = 10


    joints_dict = {}
    for (i,name) in zip(range(joint_number), joint_name):
        joints_dict[name] = joint[i]
    return joints_dict


def draw(pos1,pos2,color):
    """ draw line if p1 and p2 are valid points"""

    if (pos1[2] == 1) and (pos2[2] == 1):
        plt.plot([pos1[0], pos2[0]], [pos1[1], pos2[1]], color=color, linestyle='-', linewidth=4)
        return
    else:
        return

def draw_lines(im,joint):
    joints_dict = make_joints_dict(joint)
    plt.imshow(im)

    #first line r_ankle to r_knee
    if  not (joints_dict.get('r_ankle') == None) and   not (joints_dict.get('r_ankle') == None):
            p1 = joints_dict['r_ankle']
            p2 = joints_dict['r_knee']
            draw(p1,p2,'g')

    if  not (joints_dict.get('r_knee') == None) and   not (joints_dict.get('r_hip') == None):

            p1 = joints_dict['r_knee']
            p2 = joints_dict['r_hip']
            draw(p1,p2,'r')

    if  not (joints_dict.get('r_hip') == None) and   not (joints_dict.get('l_hip') == None):

            p1 = joints_dict['r_hip']
            p2 = joints_dict['l_hip']
            draw(p1,p2,'m')

    if  not (joints_dict.get('l_hip') == None) and   not (joints_dict.get('l_knee') == None):

            p1 = joints_dict['l_hip']
            p2 = joints_dict['l_knee']
            draw(p1,p2,'c')

    if  not (joints_dict.get('l_knee') == None) and   not (joints_dict.get('l_ankle') == None):
            p1 = joints_dict['l_knee']
            p2 = joints_dict['l_ankle']
            draw(p1,p2,'b')

    if  not (joints_dict.get('l_hip') == None) and   not (joints_dict.get('l_shoulder') == None):

            p1 = joints_dict['l_hip']
            p2 = joints_dict['l_shoulder']
            draw(p1,p2,'m')

    if  not (joints_dict.get('l_shoulder') == None) and   not (joints_dict.get('neck') == None):

            p1 = joints_dict['l_shoulder']
            p2 = joints_dict['r_shoulder']
            draw(p1,p2,'m')

    if  not (joints_dict.get('l_shoulder') == None) and   not (joints_dict.get('l_elbow') == None):
            p1 = joints_dict['l_shoulder']
            p2 = joints_dict['l_elbow']
            draw(p1,p2,'c')
    if  not (joints_dict.get('l_elbow') == None) and   not (joints_dict.get('l_wrist') == None):

            p1 = joints_dict['l_elbow']
            p2 = joints_dict['l_wrist']
            draw(p1,p2,'b')

    if  not (joints_dict.get('r_shoulder') == None) and   not (joints_dict.get('r_hip') == None):
            p1 = joints_dict['r_hip']
            p2 = joints_dict['r_shoulder']
            draw(p1,p2,'m')

    if  not (joints_dict.get('l_shouder') == None) and   not (joints_dict.get('r_shoulder') == None):

            p1 = joints_dict['r_shouder']
            p2 = joints_dict['l_shoulder']
            draw(p1,p2,'m')

    if  not (joints_dict.get('r_shoulder') == None) and   not (joints_dict.get('r_elbow') == None):

            p1 = joints_dict['r_shoulder']
            p2 = joints_dict['r_elbow']
            draw(p1,p2,'r')

    if  not (joints_dict.get('r_elbow') == None) and   not (joints_dict.get('r_wrist') == None):
            p1 = joints_dict['r_elbow']
            p2 = joints_dict['r_wrist']
            draw(p1,p2,'g')

    if  not (joints_dict.get('neck') == None) and   not (joints_dict.get('head') == None):

            p1 = joints_dict['neck']
            p2 = joints_dict['head']
            draw(p1,p2,'y')

    plt.show()
    return
