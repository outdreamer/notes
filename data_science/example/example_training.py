import pandas as pd
compound_data = pd.read_csv('compound_data.csv', names = column_list)
compound_data.head()
compound_data.describe().transpose()

# 178 data points with 13 features and 1 label column (in the other example in that guy's blog)
compound_data.shape # prints the dimensions of the matrix storing this data
# (178, 14)

# Let's set up our Data and our Labels:

X = element_list.drop('Successful Treatment true/false',axis=1)
y = compound_data['Successful Treatment true/false']

# Train Test Split

# Let's split our data into training and testing sets, this is done easily with SciKit Learn's train_test_split function from model_selection:

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Data Preprocessing

# The neural network may have difficulty converging before the maximum number of iterations allowed if the data is not normalized. Multi-layer Perceptron is sensitive to feature scaling, so it is highly recommended to scale your data. Note that you must apply the same scaling to the test set for meaningful results. There are a lot of different methods for normalization of data, we will use the built-in StandardScaler for standardization.

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Training the model

from sklearn.neural_network import MLPClassifier

# Next we create an instance of the model - there are a lot of parameters you can choose to define and customize here, we will only define the hidden_layer_sizes. For this parameter you pass in a tuple (a tuple is a data type that stores lists for quick access in python) consisting of the number of neurons you want at each layer, where the nth entry in the tuple represents the number of neurons in the nth layer of the MLP model. There are many ways to choose these numbers, but for simplicity we will choose 3 layers with the same number of neurons as there are features in our data set along with 500 max iterations.

# if you had 13 features of chemical pairs & bond types

mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)

# Now that the model has been made we can fit the training data to our model, remember that this data has already been processed and scaled:

mlp.fit(X_train,y_train)

# output with default params of the network: 

/* MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(13, 13, 13), learning_rate='constant',
       learning_rate_init=0.001, max_iter=500, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
*/

predictions = mlp.predict(X_test)

# Now we can use SciKit-Learn's built in metrics such as a classification report and confusion matrix to evaluate how well our model performed:

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))