
import tensorflow as tf
from libs.activations import *
from libs.batch_norm import batch_norm
import numpy as np

def inference(x, y, keepProb,is_training,batch_size,learning_rate):

    """
    Args:
      images: Images returned from distorted_inputs() or inputs().

    Returns:
      Logits.

    """

    with tf.variable_scope('conv1') as scope:
        kernel = tf.Variable(tf.random_normal([11, 11, 3, 48], stddev=1e-4), name='weights')
        conv = tf.nn.conv2d(x, kernel, [1, 4, 4, 1], padding='SAME')
        biases = tf.Variable(tf.constant(0.001, dtype=tf.float32, shape=[48]), name='biases')

        bias = tf.nn.bias_add(conv, biases)
        conv1 = batch_norm(lrelu(bias, name=scope.name), is_training, scope='bn1')


    # pool1
    pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding='SAME', name='pool1')

    # conv2
    with tf.variable_scope('conv2') as scope:
        kernel = tf.Variable(tf.random_normal([5, 5, 48, 128], stddev=1e-4), name='weights')
        conv = tf.nn.conv2d(pool1, kernel, [1, 1, 1, 1], padding='SAME') #use_cudnn_on_gpu=False,
        biases = tf.Variable(tf.constant(0.001, dtype=tf.float32, shape=[128]), name='biases')
        bias = tf.nn.bias_add(conv, biases)
        conv2 = batch_norm(lrelu(bias, name=scope.name), is_training, scope='bn2')


    # pool2
    pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool2')


    # conv3
    with tf.variable_scope('conv3') as scope:
        kernel = tf.Variable(tf.random_normal([3, 3, 128, 192], stddev=1e-2), name='weights')
        conv = tf.nn.conv2d(pool2, kernel, [1, 1, 1, 1], padding='SAME')
        biases = tf.Variable(tf.constant(0.001, dtype=tf.float32, shape=[192]), name='biases')

        bias = tf.nn.bias_add(conv, biases)
        conv3 = lrelu(bias, name=scope.name)



    # conv4
    with tf.variable_scope('conv4') as scope:
        kernel = tf.Variable(tf.random_normal([3, 3, 192, 192], stddev=1e-2), name='weights')
        conv = tf.nn.conv2d(conv3, kernel, [1, 1, 1, 1], padding='SAME') #use_cudnn_on_gpu=False,
        biases = tf.Variable(tf.constant(0.001, dtype=tf.float32, shape=[192]), name='biases')

        bias = tf.nn.bias_add(conv, biases)
        conv4 = lrelu(bias, name=scope.name)



    # conv5
    with tf.variable_scope('conv5') as scope:
        kernel = tf.Variable(tf.random_normal([5, 5, 192, 128], stddev=1e-2), name='weights')
        conv = tf.nn.conv2d(conv4, kernel, [1, 1, 1, 1], padding='SAME') #use_cudnn_on_gpu=False,
        biases = tf.Variable(tf.constant(0.001, dtype=tf.float32, shape=[128]), name='biases')

        bias = tf.nn.bias_add(conv, biases)
        conv5 = lrelu(bias, name=scope.name)


        pool3 = tf.nn.max_pool(conv5, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME', name='pool3')

    # local1
    with tf.variable_scope('local1') as scope:
        # Move everything into depth so we can perform a single matrix multiply.
        dim = 1
        for d in pool3.get_shape()[1:].as_list():
            dim *= d
        reshape = tf.reshape(pool3, [batch_size, dim])

        weights = tf.Variable(tf.random_normal([dim, 4096], stddev=np.sqrt(1/dim+4096)), name='weights')
        biases = tf.Variable(tf.constant(0.0001, dtype=tf.float32, shape=[4096]), name='biases')
        local1 = tf.nn.relu_layer(reshape, weights, biases)

        local1 = tf.nn.dropout(local1, keepProb)

    # local2
    with tf.variable_scope('local2') as scope:
        weights = tf.Variable(tf.random_normal([4096, 4096], stddev=np.sqrt(1/4096.0)), name='weights')
        biases = tf.Variable(tf.constant(0.0001, dtype=tf.float32, shape=[4096]), name='biases')

        local2 = tf.nn.relu_layer(local1, weights, biases)

        local2 = tf.nn.dropout(local2, keepProb)


    with tf.variable_scope('softmax_linear') as scope:
        weights = tf.Variable(tf.random_normal([4096, 20], stddev=np.sqrt(1/4096.0)), name='weights')
        biases = tf.Variable(tf.constant(0.01, dtype=tf.float32, shape=[20]), name='biases')
        softmax_linear = tf.nn.xw_plus_b(local2, weights, biases)


    with tf.name_scope("loss"):
        loss = tf.nn.l2_loss((y - softmax_linear), name="L2_loss")

    with tf.name_scope("train_step"):
        train_op = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)



    return train_op, softmax_linear, loss
