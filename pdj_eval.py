import tensorflow as tf
import numpy as np
from libs.input_data import *
from libs.models import *
from libs.draw_lines import *
from libs.batch_norm import batch_norm
import matplotlib.pyplot as plt


def distance(p1,p2):

    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def pdj(pred,label,r,score):
    pred = np.reshape(pred,[10,2])
    label = np.reshape(label,[10,2])

    d_list = []
    for i in range(10):
        dist = distance(label[i],pred[i])/220
        if dist>=r:
            d_list.append(0)
        else:
            d_list.append(1)
    return np.array(d_list + score)



def eval():

    d = Dataset()
    batch_size = 1
    x = tf.placeholder(tf.float32, [None, 220,220,3],name='x_placeholder')
    y = tf.placeholder(tf.float32, [None, 20],name='y_placeholder')
    is_training = tf.placeholder(tf.bool, name='is_training')
    keepProb = tf.placeholder(tf.float32, name='dropout_prob')

    [train_op, pred, loss] = inference(x,y,keepProb,is_training,1,0.00001)
    saver = tf.train.Saver()

    with tf.Session() as sess:
        saver.restore(sess, "checkpoints/model195000.ckpt")
        range_score = []

        for r_range in range(0,30,1):
            score = np.zeros(10)
            r = r_range/100.0

            print "RADIUS VALUE", r
            for i in range(d.test_num):
                [batch_x, batch_y] = d.get_example("Test",i)
                x_sample = batch_x[0]
                batch_x[:,:,:] /= 255 - np.mean(batch_x)
                batch_y = batch_y[0:10,0:2]
                batch_y = np.reshape(batch_y,[batch_size,10*2])
                test_pred = sess.run(pred,
                    feed_dict={x:batch_x, y:batch_y, keepProb:1, is_training:False})
                score = pdj(test_pred,batch_y,r,score)

            score = score/float(d.test_num)
            print score
            range_score.append(score)
    np.save("pdj",range_score)

eval()

pdj = np.load("pdj.npy")
shoulders =  (pdj[:,0] + pdj[:,3])/2.0
elbows = (pdj[:,1] + pdj[:,4])/2.0
wrist = (pdj[:,2] + pdj[:,5])/2.0
hip = (pdj[:,6] + pdj[:,7])/2.0
head = (pdj[:,8] + pdj[:,9])/2.0

shoulders, = plt.plot(shoulders, label='shoulders')
elbows, = plt.plot(elbows, label='elbows')
wrist, = plt.plot(wrist, label='wrists')
hip, = plt.plot(hip, label='hips')
head, = plt.plot(head, label='head')
plt.legend(handles=[shoulders,elbows,wrist,hip,head],loc=4)
plt.show()
