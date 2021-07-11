# load and evaluate a saved model
from __future__ import print_function

import os, pickle
from skimage.transform import resize
from skimage.io import imsave
import tensorflow as tf
import numpy as np
from keras.models import Model
from keras.layers import Input, concatenate, Conv2D, MaxPooling2D, Conv2DTranspose
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras import backend as K
from data import load_train_data, load_test_data

from numpy import loadtxt
from keras.models import load_model
 
from data import load_train_data, load_test_data

import numpy as np


model = load_model('model.h5', compile=False)

model.summary()

