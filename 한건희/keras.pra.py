from pyexpat import model
from keras.layers import Dense,Activation,Flatten,Input
from keras.models import Sequential,Model
from keras.utils import plot_model
model=Sequential()
model.add(Input(shape=(28,28)))
model.add(Dense(300,activation='relu'))
model.add(Dense(100,activation='relu'))
model.add(Dense(10,activation='softmax'))
model.summary()
