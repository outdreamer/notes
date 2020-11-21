# Statistical tools


# Concepts

	- matrix
	- vector
	- eigenvector/eigenvalue
	- sparsity
	- orthogonal
	- variables
		- random
		- gaussian/normal
	- degrees of freedom
	- jacobian
	- hilbert space
	- lie algebra
	- hessian matrix
	- neumann series
	- taylor series
	- homomorphism
	- topology
	- manifold
	- soft thresholding operator: translates values towards zero, making them exactly zero if they are small enough
	- hard thresholding operator: sets smaller values to zero, leaving larger ones untouched
	- propensity modeling
    - lifetime value estimation
    - segmentation

# Functions

	- loss/cost/objective/penalty
	- kernel
	- norm: function from a real/complex vector space to the real numbers that commutes with scaling, obeys the triangle inequality, and is zero only at the origin


# Tasks

	- selecting hypothesis test: https://towardsdatascience.com/which-hypothesis-test-to-perform-89d7044d34a1
		- use z test for proportion, t test for mean
		- for two-sample paired mean, use two-sample paired mean t-test
		- for two-sample independent mean, use two-sample pooled mean t-test
		
	- backpropagation
	- action/policy/state/reward
	- finding local maxima/minima, where function has equality constraints (like that equations have to be satisfied by the chosen variable values)
		- derivatives (slope is zero indicating a curve maximum/minimum or saddle point)
		- lagrange multiplier
			- convert a constrained problem into a form so the derivative test of an unconstrained problem can be applied
			- Lagrangian function: 
				- to find the maximum/minimum of the original function:
					- find the lagragian function: 
						- original function - lagrange multiplier * g(x), where equality constraint is g(x) = 0
					- find the stationary points of the lagrangian function
						- find the saddle points within the stationary points
							- find the optimizing saddle point of the bordered hessian matrix (having definiteness)
				- the lagragian uses a reformulation of original problem, using the relationship between the gradients of the function & constraints
				- allowing optimization without using constraint parameterization
		- gradient descent

	- data visualization example solutions: 
		  - translating articles to network graphs for summarization intent
		  - reducing interaction options to use case to avoid injecting too many options into a visualization 
		
	- train/test protocols
		- add missing data to training set
		- train & test sets should have no overlap
		- 80/20 is a normal split
		- validation set is from training data
		- add cross-validation to split the data set in multiple ways 
		
	- statistical significance
		- problem-solution: data sources, annotation, modeling approaches, & pitfalls
		- reduce overfitting
			- feature selection
				- pca: reduce variables to linear components so linear combinations can be used to represent variable sets
				- regularization + ANOVA
				- random forest (nodes as feature conditions so similar outputs are in the same set, where feature importance is based on tree entropy reduction)
		- ROC curve
			- plots how a binary classifier's ability changes based on its threshold value
			- plots the true positive rate (true's predicted correctly) against the false positive rate at various thresholds
		- correlation matrix to isolate variables with low correlation for independence
		- confusion matrix to display precision & recall of various values, comparing prediction & true value counts
		- accuracy (total correct prediction ratio)
		- AUC (ability to distinguish +/- observations)
		- precision (confidence in predicting a value): relevant/retrieved
		- recall (values predicted correctly): retrieved/total relevant
		- F1-score (measures test accuracy) = combine precision & recall with a harmonic mean (rate average) = 2 * (precision * recall) / (precision + recall)
		- lime explainer to show factors for a given prediction


# Rules
		- coefficient estimates do not need to be unique if covariates are collinear
	

# Statistical models
		- linear models
		- generalized estimating equations
		- proportional hazards models
		- M-estimators
		- anova
		- arima


## Probability distributions

		- normal (gaussian)
			- logit-normal
			- truncated-normal
			- wrapped normal
			- folded normal
			- half normal
			- log normal
		- poisson
		- binomial 
			- bernouilli
		- uniform
		- weibull
			- exponential
		- gamma
			- chi-squared (used in goodness of fit tests)
		- pareto
		- levy
		- cauchy
		- laplace
		- t-squared

	- distribution types/attributes
		- joint
		- conditional
		- generalized
		- continuous/discrete
		- negative
		- geometric
			- hypergeometric
		- beta
		- stable
		- logarithmic
		- truncated
		- raised
		- half
		- bi
		- phased
		- mixture
		- combination
		- shifted
		- unique
		- convex
		- wrapped
		- folded
		- noncentral
		- inverse
		- scaled

	- probability density functions
		- pdf
		- cdf (cumulative)

	- other functions
		- delta function


# Metrics

	- recall
	- accuracy
	- precision
	- change detection (metrics: false alarm, misdetection, detection delay)


# Algorithms

	- regression

		- linear
		- logistic
		- poisson
		- bayesian probit regression
		- generalized linear regression: version of linear regression, where:
			- output/dependent variables can have non-normal error distribution models
			- the measurement variance magnitude is an output of its predicted value
			- it uses a function to link the linear model & dependent variable (linking the linear model to a mean of the outcome distribution function)
		- lasso regression: involves variable selection & regularization
		- ridge regression
		- best subset selection regression

	- artificial neural network

		- dense network
		- convulational network
		- reinforcement learning
		- random forest: ensemble learning method to weight decision tree output
		- xgboost: similar to a Random Forest with the difference that every tree is fitted on the error of the previous one

	- categories

		- reinforcement learning

			- deep reinforcement learning
			- inverse reinforcement learning
			- safe reinforceement learning

			- specific reinforcement algorithms: 

				- https://en.wikipedia.org/wiki/Reinforcement_learning#Comparison_of_reinforcement_learning_algorithms

				Monte Carlo:		Every visit to Monte Carlo
				Q-learning:			State–action–reward–state
				SARSA:				State–action–reward–state–action
				Q-learning-Lambda:	State–action–reward–state with eligibility traces
				SARSA-Lambda:		State–action–reward–state–action with eligibility traces
				DQN:				Deep Q Network
				DDPG:				Deep Deterministic Policy Gradient
				A3C:				Asynchronous Advantage Actor-Critic Algorithm
				NAF:				Q-Learning with Normalized Advantage Functions
				TRPO:				Trust Region Policy Optimization
				PPO:				Proximal Policy Optimization
				TD3:				Twin Delayed Deep Deterministic Policy Gradient
				SAC:				Soft Actor-Critic

		- unsupervised

			- clustering

		- supervised

			- classification

			- regression
			
			- structure prediction (selecting a structure from a set of structures of a particular format, like a logic tree version)

				- example: sequence tagging (using hidden Markov model or conditional random field to predict next word based on conditional probability given previous word)
				Probabilistic graphical models 
					- Bayesian networks
					- random fields (conditional random field)
				- inductive logic programming
				- case-based reasoning
				- structured SVMs
				- structured k-Nearest Neighbours
				- Markov logic networks
				- constrained conditional models
				- Recurrent neural network, in particular Elman network

	
	- specific problems

		- generalizing (avoiding/reducing overfitting)
			- cross-validation
			- regularization

		- data changes
			- data augmentation
			- alternate data set generation
			- missing value imputation

		- loss function
			- square loss
				- mean square
			- hinge loss

		- standardization: framing values in standard range like 0 - 1 or -1 to 1

		- regularization (generalizing to prevent over-fitting to a specific data set, adding a cost to optimization function to penalize over-fitting) 

			- classification

			- lasso regularization (least absolute shrinkage and selection operator)

				- forces sum of the absolute value of the regression coefficients to be less than a fixed value, so that certain coefficients are zero, effectively choosing a simpler model excluding those coefficients
				- standardization by centering variables around the mean
				- shrinks the magnitude of all the coefficients, but sets some of them to zero
				- translates coefficients towards zero by a constant value, setting them to zero if they reach the constant value
				- linear regression, where coefficients have Laplace prior distributions
				- find the minimum of {{ averaged * [mean squared (meaning y - xB)] - lagrangian multiplier * (B) }}
					min {{ 1/N * ||y - xB|| - L * ||B|| }}

				- isolates components of B that are zero (such as the corners of the lasso norm square), for certain objects that are tangent to the boundaries of the norm shape, to help with removing those components
			
			- ridge regularization

				- forces sum of the squares of the coefficients to be less than a fixed value, which shrinks the size of all coefficients (not setting any of them to zero)
				- improves prediction error by shrinking large regression coefficients in order to reduce overfitting
				- shrinks the magnitude of all the coefficients
				- scales all of the coefficients by a constant factor
				- linear regression, where coefficients have normal prior distributions
				- methods
					- Tikhonov-regularized least squares
			
			- early stopping: training until error on validation set stops decreasing

			- other regularizers
				- signal noise reduction: 
					- total variation regularization

			- regularizers for sparsity
			    - Proximal methods
			    - Group sparsity without overlaps
			    - Group sparsity with overlaps

			- regularizers for semi-supervised learning

			- regularizers for multitask learning
			    - Sparse regularizer on columns
			    - Nuclear norm regularization
			    - Mean-constrained regularization
			    - Clustered mean-constrained regularization
			    - Graph-based similarity

		- selecting model from a model ensemble

			- Bayesian learning methods make use of a prior probability that (usually) gives lower probability to more complex models
			- Akaike information criterion (AIC)
			- minimum description length (MDL)
			- Bayesian information criterion (BIC)

		- dimensionality reduction

			- feature selection: selecting variables for use in the model
				- stepwise: useful only when a few variables have a strong relationship to dependent variable
				- lasso

		- anomaly detection

		    - Density-based techniques
		    	- k-nearest neighbor
		    	- local outlier factor
		    	- isolation forests
		    	
		    - Outlier detection
		    	- subspace
		    	- correlation
		    	- tensor
		    	- cluster analysis 
		    	- fuzzy logic

		    - SVM (one-class)

		    - Replicator neural networks

		    - Autoencoders
		    	- variational autoencoders

		    - Long short-term memory neural networks

		    - Bayesian networks

		    - Hidden Markov models (HMMs)

		    - Deviations from association rules/frequent itemsets

		    - Ensemble techniques
		    	- feature bagging
		    	- score normalization
		    	- different sources of diversity



Featurization/feature extraction: 
  process of transforming raw data into feature/input vectors of fixed length so it can be used in ml algorithms
  better features = less ML needed
  Automation: *** some algorithms use different feature types better than others
  Insight: *** domain knowledge can usually be reduced to structural or semantic metadata properties

1-hot encoding: where a group of related features has only one feature active at any time (ex: only one email address suffix is active at a time)
  a set of binary features that always has exactly one nonzero value

Categorical variable: a variable that takes one of several possible discrete values (ex: gender, species)
  Categorical variables can be encoded with 1-hot encoding, which is called dummy variable encoding
  Automation: *** with some algorithms, using non-redundant feature encoding is recommended
    (using only n - 1 boolean variables instead of n boolean variables to represent a set that only has one positive value at a time)

Labeled datum: a data set with output labels included 

ML algorithm input: labeled data (training set)
ML algorithm output: a prediction function

Prediction function input: a feature vector
Prediction function output: a label (prediction)

Loss function input: a prediction & a target
Loss function output: the loss (a score communicating the difference between prediction & target)
  Large error for incorrect, small error for correct, 0 for no error.

Classification loss: 1 if prediction is wrong, 0 if prediction correct
Regression (square) loss: (predicted - target) squared

Question: *** how do you ensure your test data doesn't match the training data in its distribution?
Insight: *** with time series data, identify time cycles & make sure to include multiple cycles as data set points
Insight: *** if a certain level of error continues to occur & looks like a trend, you can opt for re-gathering data & training to look for new factors

Covariate (input) shift: input distribution changed between training & deployment
Concept (success) drift: correct output categorization changes over time for a given input

Question: *** Whats the standard way to address new factors introduced?

Validating model:

  Automation: *** if you have a small data set, you can use k-fold cross-validation to train on various groups of data & test on the remainder, then take the average mean & standard error of the iterated mean & standard deviation
    k-fold average = average of all iterated test means
    k-fold standard error = standard deviation of all iterated performances / square root of k number of iterated test groups

  Forward chaining: for time series, use forward-chaining to use increasing proportions of the data as iterated training sets, similar to k-fold cross-validation

Error types:

  Leakage: information about classification labels leaks into features (ex: image title entered as feature in training set but not deployment set)
    Automation: *** identify leakage programmatically

  Sample bias: test data & deployment data have different distributions

Algorithms;
  
  Polynomial curve fitting: 
    - a learning function fitPolynomial would have the data & number of parameters as input, & return the output vector of parameters that are the constant multipliers of the polynomial terms
    - a prediction function predictPolynomial would take the parameter vector, number of terms, and the input x and output the prediction value y for that x

  Hyperparameter is a parameter of the algorithm itself, like the number of polynomial terms (degree of polynomial) of the prediction function

  M (the degree of the polynomial) controls the model complexity
    - bigger M allows more complex prediction functions that fit training data better, but not necessarily better performance on test data 

  Automation: *** Sometimes you can use a ml algorithm to choose your hyperparameters for you


Underfitting: the line is too simple for data

Overfitting:
  - the line is too complex for data
  - training performance is good but test/validation performance is poor
  - reduce model complexity & add more training data to fix overfitting

  Question: *** what about the situation where the more complex function is accurate, but the data was gathered in a context isolated from those extra factors?

Regularization: used to control model complexity

Hyperparameters control various things:
- complexity of the model (polynomial order/degree)
- type of model complexity control (l1 vs l2 regularization)
- optimization algorithm (learning rate)
- model type (loss function, kernel type, etc)

Risk of a decision function is the expected loss of the decision function on a new example drawn randomly from the range of possible x & y pairs.

Bayes decision function: a function that achieves the minimal risk across all possible functions

Confidence Interval:
  Size of the confidence interval grows with the log of the number of things youre testing 

Quick calculations to find out:

  Model accuracy:
  - if the prediction function is accurate, calculate the coefficient of determination, r squared

  Changes in two variables:
    - if x changes predict y changes to see if a correlation between x & y exists, calculate the correlation coefficient, r
      Pearson's r = the covariance of x & y divided by the product of their standard deviations, used in linear relationship between 2 variables
    - if x changes similarly to how y changes, calculate the covariance
    - how much y changes because of x, calculate the linear regression prediction function

  Rate of Change at a point:
  - the sensitivity of y with respect to changes in x, calculate the derivative of f(x) (the slope/rate of change)

  Change in one variable:
  - how much a set of numbers deviates from its mean, calculate the variance

  Distortion Area (area between functions, like how different f(x) is from the line y = 0):
  - the distortion of a function, calculate the integral (the area or volume)

  Data Extremity:
  - p-value: estimates how likely it is that the observation is unrelated to what youre testing

Quick Definitions:

regularization: prevent overfitting by adding a tuning parameter, usually a constant multiplier like l1 lasso or l2 ridge to a weight vector to minimize average loss of prediction function
coefficient of determination r squared: describe how well data fit the prediction function, by comparing the performance of the prediction function to the performance of the average as a predictor
correlation coefficient: sum of squared difference between observed & predicted outcomes = the normalized version of the covariance
covariance: how much two variables change together
variance: expectation of the squared difference of a random variable from its mean

Regularization:
  - adding a tuning parameter to a model to prevent overfitting & create a smooth line
  - usually regularization is done by adding a constant multiplier to an existing weight vector
  - the constant is usually either the l1 lasso or l2 ridge but can be any norm
  - after applying the constant multiplier, the prediction function should then minimize the average loss (of the loss function) on the regularized training data

Coefficient of determination: (r squared): used as a way to validate the model by describing how well the data fit a model

Correlation coefficient (r): the difference between the observed & predicted outcomes

  Calculating r:

    calculate the residuals, which is the vector list of differences between observed & predicted outcomes
    calculate the mean of the observed data & use it in the 3 sum of squares formulas,
      to estimate the variability of the data set

      Total sum of squares (proportional to data variance):
        sum of all squared differences between each observed point & the mean of the observed data

      Regression/explained sum of squares:
        sum of all squared differences between each predicted point & the mean of the observed data.

      Residual sum of squares:
        sum of all squared differences between each predicted point & each observed point.

  Calculating r squared:

      R squared = 1 - (residual sum of squares / total sum of squares)

      if R squared = .3, then 30% of the variability of the dependent variable is explained by the prediction function

      The closer R squared is to 1, the better the prediction function.
      You divide the residual sum of squares by the total sum of squares,
       in hopes that the residual sum of squares is very low compared to the total sum of squares,
      so the fraction results in a very small number to subtract from 1.

      Then once you take that fraction, you have a measurement of how much better the prediction function is at explaining the data,
        compared to just taking the average value of y as the prediction function.

      In multiple regression (with an estimated intercept term) r squared is the square of the Pearson correlation coefficient between observed & predicted data values.

Pearson correlation coefficient (bivariate correlation):
  - used when comparing two quantitative variables related linearly
  - measures the linear correlation between two variable x & y, ranging from -1 to 1 where 1 is perfect correlation.
  - defined as the covariance of x & y divided by the product of their standard deviations.

  One way to calculate r is:
    sum of x * y - sample size n * mean of x * mean of y
    ----------------------------------------------------
    square root of (sum of x squared - n * mean of x squared)  -

covariance:
  - how much two variables change together
  - if positive values of one variable occur with positive values of the other variable (etc for other value types), they have positive covariance
  - to calculate covariance:

variance:
  - expectation of the squared difference of a random variable from its mean
  - how far a set of random numbers are spread out from their average value
  - to calculate variance of a discrete variable:
    variance(x) = 1/n * sum of squared difference between x & mean

  - to calculate variance of a continuous variable:
    variance(x) = integral of x squared * f(x)dx - mean squared
    mean(x) = integral of x * f(x)dx

integral:
  - can measure displacement, area, volume & other aspects produced by executing operations on ranges separated into infinitesimally small intervals
    integral of f(x)dx = f(b) - f(a)
    integral of x squared = 1/3 (x ^ 3)

derivative:
  - calculates the sensitivity of y with respect to changes in x
    derivative of x squared = 2 * x

norm:

accuracy: number of total accurate predictions / number of all predictions
recall: number of correct positive predictions / number of all positive data points
precision: number of correct positive predictions / all positive predictions

linear vs. multivariate: in linear models, x is mapped to y, in multivariate models, a vector of inputs is mapped to y

validate the model:
  - if youre predicting a minimum/maximum with gradient descent, does it reflect local or absolute values?
  - is there enough variety in the test data (avoid overfitting)
  - is the sample size enough, was the data gathered without bias?
  - split the data into training data & validation/test data
  - use jackknife resampling if the dataset is small
  - measure validity with r squared and mean squared error
  - test if model appears the same when trained on new data
  - test if model is accurate when fed test data
  - look for multicollinearity, where you have two variables so tightly correlated that they essentially give the same signal so theyre redundant
    multicollinearity affects the calculations done on individual variables, like finding out the impact of one independent variable on the dependent variable
    however a multivariate regression model with collinear predictors can still give a good grasp on how the entire set of input variables impact the output variable.
