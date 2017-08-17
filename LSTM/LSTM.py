import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation, Dropout
from keras.models import load_model
from random import uniform
import sys
import keras

def readData(fileName):
    dataframe = pandas.read_csv(fileName,
                                engine='python', header=None)
    dataset = dataframe.values
    dataSet = dataset.astype('float32')

    return dataSet

def initModel(look_back, dropout, dropout_inner, neurons):

    out_neurons = 1
    hidden_neurons = neurons
    hidden_inner_factor = 1
    hidden_neurons_inner = int(hidden_inner_factor * hidden_neurons)
    dropout = dropout 
    dropout_inner = dropout_inner

    model = Sequential()
    model.add(LSTM(output_dim=hidden_neurons,
                   input_dim=look_back,
                   init='uniform',
                   return_sequences=True,
                   consume_less='mem'))
    model.add(Dropout(dropout))
    model.add(LSTM(output_dim=hidden_neurons_inner,
                   input_dim=hidden_neurons,
                   return_sequences=True,
                   consume_less='mem'))
    model.add(Dropout(dropout_inner))
    model.add(LSTM(output_dim=hidden_neurons_inner,
                   input_dim=hidden_neurons_inner,
                   return_sequences=False,
                   consume_less='mem'))
    model.add(Dropout(dropout_inner))
    model.add(Activation('relu'))
    model.add(Dense(output_dim=out_neurons,
                    input_dim=hidden_neurons_inner))
    model.add(keras.layers.advanced_activations.LeakyReLU(alpha=0.3))

    model.compile(loss="mse",
                  optimizer="Adam",
                  metrics=['accuracy'])
                  
    return model


def cookData(matrix):
    matrix = numpy.reshape(matrix, (matrix.shape[0], 1, matrix.shape[1]))
    return matrix


def fitModel(trainX, trainY, model, epochs, batch_size):
    model.fit(trainX, trainY, nb_epoch=epochs, batch_size=batch_size, verbose=2)
    return model


def myround(a, decimals):
    return numpy.around(a - 10 ** (-(decimals + 5)), decimals=decimals)


def predict(predictX):
    Y = []
    
    for line in predictX:
	line = numpy.reshape(line,(1,1,len(line)))
        Y.append(model.predict(line))

    return Y


def writeOutput(fileName, Y):
    numpy.savetxt(fileName, Y, delimiter=",")

epochs = 500

#######Get Training data X,Y and predictX########
fileNameX = 'data/50000_smaller_trainX0406_delete1955.csv'
fileNameY = 'data/50000_smaller_trainY0406_delete1955.csv'
trainX = readData(fileNameX)
trainY = readData(fileNameY)


#######You need to change this part#######
#Please Adjust dropout in [0.001, #0.002, 0.005, 0.01, 0.02] 
#Please Adjust dropout_inner in [0.001, 0.005, 0.01, 0.05, #0.1, 0.2]
#please adjust neurons in [100, 200, #500, 800]
#the # part is what you don't change when you ajust orther part


######Making for loop in this part#######
model = initModel(look_back = 4, dropout, dropout_inner, neurons)
trainX = cookData(trainX)
model = fitModel(trainX, trainY, model, epochs, batch_size = 36)

model.save('./model/model_dropout_'+str(dropout)+'_dropoutInner_'+str(dropout_inner)+'_neurons_'+str(neurons)+'.h5')


