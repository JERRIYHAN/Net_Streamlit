import streamlit as st
st.balloons()
st.write("# NN")
st.code('''
# %% [markdown]
# # 自由手写数字识别
# MNIST数据集请点击[这里查看](http://yann.lecun.com/exdb/mnist/)

# %%


# %% [markdown]
# ## 本demo主要是通过输入自己的手写数字图片，使用多层神经网络模型进行识别

# %% [markdown]
# ### 环境配置 numpy和tf加载

# %%
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import time
import cv2
import matplotlib.pyplot as plt

# %% [markdown]
# ### 下载数据 

# %%
mnist = input_data.read_data_sets("data/MNIST/", one_hot=True) #调用input_data的read_data_sets函数下载数据集

# %% [markdown]
# ### 查看下下载的mnist数据结构
# - 查看数据集中trian test validation的大小
# - 查看某一个样本并显示

# %%
import matplotlib.pyplot as plt
print(mnist.train.images.shape)          #mnist里已分好train和validation,看一下shape,shape是什么类型
print(mnist.train.labels.shape)
print(mnist.validation.images.shape)
print(mnist.validation.labels.shape)
print(mnist.test.images.shape)
print(mnist.test.labels.shape)
image = mnist.train.images[54999].reshape(28,28)
plt.imshow(image)
plt.show()

# %% [markdown]
# ## 读取图片文件

# %% [markdown]
# - 给你自己输入的图片加label--make_label函数
# - 将你自己输入的图片取反并转成1x784的数组
# - 程序考核

# %%
def make_label(label_num):
    label = np.zeros((1, 10),dtype='float32')
    label[:,label_num] = 1.0
    print(label)
    return label

label_test = make_label(5)
# 图片路径
img_path = "data/MNIST_test/5.jpg"
img_file = cv2.imread(img_path)
print(img_file.shape)
img_file = cv2.cvtColor(img_file, cv2.COLOR_RGB2GRAY)
print(img_file)
print(img_file.shape)
plt.imshow(img_file,'gray')
plt.show()
data_test = img_file / 255
data_test = np.float32(img_file.reshape(1, 28*28))
data_test.shape

# %% [markdown]
# ## 创建DNN模型
# * 设定输入节点数、隐含层节点数、训练迭代次数这三个超参，理解超参
# * 创建两个tf.Variable 作为W和B
# * 创建三个tf.placeholder 作为数据x，标签label，onehot保留系数keep_prob

# %%
input_num = 784
h1_num = 200
h2_num = 10
epochs = 1000
batch_num = 1000
lr = 0.09

# %%
W1 = tf.Variable(tf.truncated_normal([input_num, h1_num],stddev=0.1))
B1 = tf.Variable(tf.zeros([h1_num]))
W2 = tf.Variable(tf.truncated_normal([h1_num, h2_num],stddev=0.1))
B2 = tf.Variable(tf.zeros([h2_num]))

x = tf.placeholder(tf.float32, [None, input_num])
keep_prob = tf.placeholder(tf.float32)
label = tf.placeholder(tf.float32, [None,10])

hidden1 = tf.matmul(x,W1) + B1
hidden1_drop = tf.nn.dropout(hidden1, keep_prob)
hidden2 = tf.matmul(hidden1_drop, W2) + B2
hidden2_drop = tf.nn.dropout(hidden2, keep_prob)

y = tf.nn.softmax(hidden2_drop)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(label * tf.log(y), reduction_indices=[1]))
train_step = tf.train.AdagradOptimizer(lr).minimize(cross_entropy)   
#train_step = tf.train.GradientDescentOptimizer(lr).minimize(cross_entropy)

# %% [markdown]
# ### 创建session并开始训练

# %%
#with tf.Session() as sess:
sess = tf.Session()
start = time.time()
sess.run(tf.global_variables_initializer())
for epoch in range(epochs):
    batch_xs, batch_ys = mnist.train.next_batch(batch_num)
    _,cost = sess.run([train_step, cross_entropy], feed_dict={x: batch_xs, label: batch_ys, keep_prob:1})
    if epoch % 100 == 0:
        print("epoch: {}, loss: {:.2f}".format(epoch, cost))

stop = time.time()
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(label,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
predict_acc = sess.run(accuracy, feed_dict={x: mnist.test.images, label: mnist.test.labels, keep_prob:1.0})
print("测试集准确度为：{:.2f}%".format(predict_acc * 100))
print("程序耗时：{:.2f}秒".format(stop-start))


# %%
test_acc,test_value = sess.run([accuracy,y], feed_dict={x:data_test, label:label_test, keep_prob:1.0})
print("自己的手写字测试准确度为:{:.2f}%".format(test_acc * 100))
print("自己的手写字测试准确度为:{}".format(test_value))

# %%
print("AI判断的数字是{}".format(list(test_value[0]).index(test_value[0].max())))
sess.close()

# %%



''')