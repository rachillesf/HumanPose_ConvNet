import tensorflow as tf
import numpy as np
from libs.input_data import *
from libs.models import *
from libs.draw_lines import *
from libs.batch_norm import batch_norm

batch_size = 10
learning_rate = 0.0000008
num_steps = 200000

d = Dataset()

x = tf.placeholder(tf.float32, [None, 220,220,3],name='x_placeholder')
y = tf.placeholder(tf.float32, [None, 20],name='y_placeholder')
is_training = tf.placeholder(tf.bool, name='is_training')
keepProb = tf.placeholder(tf.float32, name='dropout_prob')

[train_op, pred, loss] = inference(x,y,keepProb,is_training,batch_size,learning_rate)
saver = tf.train.Saver()
cost_acc = 0
with tf.Session() as sess:

    #sess.run(tf.initialize_all_variables())
    saver.restore(sess, "checkpoints/model105000.ckpt")
    for i in range(105001,num_steps):

        [batch_x, batch_y] = d.next_batch("Train",batch_size)
        batch_x /= 255 - np.mean(batch_x)
        batch_y = batch_y[:,0:10,0:2]
        batch_y = np.reshape(batch_y,[batch_size,10*2])

        sess.run(train_op, feed_dict={x:batch_x, y:batch_y, keepProb:0.7, is_training:True})
        cost_acc += sess.run(loss,
            feed_dict={x:batch_x, y:batch_y, keepProb:0.7, is_training:True})
        if i%100 == 0:

                print "Step:", i
                print "Avg Train Loss", cost_acc/100
                cost_acc = 0

        if i%5000 ==0:
            test_acc = 0
            print "Running Test Set Evaluation on Random Sample..."
            for test_it in range(100):
                [batch_x, batch_y] = d.next_batch("Test",batch_size)
                x_sample = batch_x[0]
                batch_x[:,:,:,:] /= 255 - np.mean(batch_x)
                batch_y = batch_y[:,0:10,0:2]
                batch_y = np.reshape(batch_y,[batch_size,10*2])
                test_loss, test_pred = sess.run([loss,pred],
                    feed_dict={x:batch_x, y:batch_y, keepProb:1, is_training:False})
                test_acc += test_loss/100
            print "TEST Loss: ", test_acc
            test_acc = 0

            y_sample = np.reshape(test_pred[0],[10,2])
            draw_lines(x_sample,y_sample,i)

            savepath = "checkpoints/model" + str(i) + ".ckpt"
            print "Saving model to", savepath
            save_path = saver.save(sess, savepath)



save_path = saver.save(sess, savepath)
