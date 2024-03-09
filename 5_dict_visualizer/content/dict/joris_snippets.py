# if you want to be able to do image feature extraction:

#import tensorflow as tf
#from tensorflow.keras.models import Model
#from tensorflow.keras.layers import (Dropout, Dense, Softmax)
#from tensorflow.keras.applications import mobilenet as _mobilenet

import PIL

import moviepy as mp #https://pypi.org/project/moviepy/
from moviepy.editor import *

# retrieves and saves a film fragment to dest. The window is the time around the given time in seconds
def extractFragment(time, path, dest, window = 3):
    time = time
    
    film = VideoFileClip(path)
    tsfps = film.fps

    startTime = time-window
    endTime = time+window
    
    if endTime < film.duration:
        endTime = film.duration

    filmFragment = film.subclip(startTime,endTime)
    filmFragment.write_videofile(dest)
    
    return filmFragment

# Retrieves a pillow image version of the frame from the film in path at time
# Doesn't save it yet!

def get_film_frame(path, time):
    film = VideoFileClip(path)
    frame = film.get_frame(time)
    frame = Image.fromarray(frame,'RGB')
    return frame

# uncomment for image feature extraction:

"""
MODEL = tf.keras.applications.mobilenet.MobileNet(
                # The 3 is the three dimensions of the input: r,g,b.
                  input_shape=(224, 224, 3), 
                  include_top=False, 
                  pooling='avg'
                )

def get_image_feature(impath):
    frame = Image.open(impath)
    rgb_im = frame.convert('RGB')
    rgb_im = rgb_im.resize((224,224))
    X = np.zeros((1, *(224,224), 3))
    X[0, ] = np.array(rgb_im)
    X = tf.keras.applications.mobilenet.preprocess_input(X)
    f = MODEL.predict(X)[0]
    return f

"""