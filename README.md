# traffic_prediction
> This work was introduced in the ASC17 (ASC student supercomputer challenge), under the supervise by Dr.Xiao Wenchu and Mr. Peng Feixu with the help our team member. 

In this project, the task is to predict the traffic flow on 2016/04/20 from 8:00AM-10:00AM given the previous 50 days' traffic flow and spatial information. Different Network structure including Multi-Layer proceptron and LSTM was tried in this project, and spatial and flow information are combined light and handy. During the competition, performance was improved from 0.8086 (Baseline) to 0.5423 on RMSE, ranked 4th over 230 teams worldwide.

## Installation

Keras, PaddlePaddle, and Python

## Usage

./Preprocessing/ combine the spacial and traffic flow information

./TrainingBatch/ transform the preprocessing data to training batch

```sh
python modelPredict.py
python predict-result.py
```

## Network Structure

Multi-layer Proceptron

![alt tag](https://raw.githubusercontent.com/MaureenZOU/traffic_prediction/master/dnn.png)

LSTM

![alt tag](https://raw.githubusercontent.com/MaureenZOU/traffic_prediction/master/lstm.png)



## Experiment Result

Result Comparison on different network structure

![alt tag](https://raw.githubusercontent.com/MaureenZOU/traffic_prediction/master/Screen%20Shot%202017-08-16%20at%2011.47.44%20PM.png)
