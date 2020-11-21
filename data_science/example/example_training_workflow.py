- ml workflow

	parameters for configurable machine learning application:
	- margin of error
	- degree/interval of confidence
	- execution time

	Choice: Adjusting inputs - you can change the input number & type to get a more accurate or efficient prediction of outputs.
	Choice: How would someone attack this to insert their bias?
		In neural networks, bias comes in the form of the activation function, which acts like a gatekeeper.
		You can insert your bias by using your own activation function
	Choice: Choose the cost function based on activation function & learning type (S/U/R/O)
	Choice: Choose the type of learning out of the following (S/U/R/O)
	Choice: Choose the algorithm based on the learning type

	Tuning Variables:
		- cost
		- uncertainty
		- loss: you lose information if you use a function to transform a data set that cannot recreate the whole data set with 100% accuracy. The function may lose some of the variation in the data, which may corrupt your results & the conclusions you build on them.
		- accuracy
		- precision
		- efficiency
		- optimization
		- number of inputs
		- type of inputs
		- degree of impact: the effect that a small change in an input has on the change in output. The type of change can be constant, linear, exponential 		change, or otherwise. You may find yourself wanting certain types of change for certain variables. You may want profit y to be exponentially 			increasing with respect to constant increases in cost x. 
		- weights of nodes: weight indicates the strength of the link between two nodes

	Tuning Strategies:
		- collect more data
		- add more hidden units
		- add more layers
		- change the network architecture
		- change the basic algorithm
		- combine neural network types: running cnn & rnn together


'''
Source code:
https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/
'''

'''
https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

Workflow:
1. Label data
2. Load data
3. Define model
4. Compile model
5. Fit model
6. Evaluate model
7. Use model to predict category
'''


'''
http://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/

Install Tools:
- setup aws box
- ssh in
- install python 3
- install scipy with numpy
- install keras 
- install tensorflow
- download this script
- run this script
'''

'''
Questions:
- is there a tool to extrapolate subset training to the whole data set?
'''

'''
Function definitions 

load_data() produces data object with:
- shape property:
- reshape function:
- astype('float32') function:

'''

np_utils.to_categorical:
- converts data to 1 non-zero value per row 

# Larger CNN for the MNIST Dataset
import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# reshape to be [samples][pixels][width][height]

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28).astype('float32')
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255
# one hot encode outputs
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]
	
# define the larger model
def larger_model():
	# create model
	model = Sequential()
	model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(15, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
	
# build the model
model = larger_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Large CNN Error: %.2f%%" % (100-scores[1]*100))