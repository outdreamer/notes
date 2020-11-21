predict vars 

probability-density function
cumulative-density function
moment-generating function
moment =  
variance vs. bias
AI model
distribution = perspective
mean, median, mode, standard deviation
variable = 
function = 
probability 
degrees of freedom, significance value
youre x

t-table: http://www.statisticshowto.com/tables/t-distribution-table/
f-table: http://www.statisticshowto.com/tables/f-table/
z-table: 

standard deviation: proportional distance from the mean
variance: square of the standard deviation
interquartile range: difference between 25 & 75% on cdf
degree of freedom: each of a number of independently variable factors affecting the range of states in which a system may exist, in particular.
	The degree of freedom is the number of independent parameters that define a system's configuration
	so if you have two fields in your profile (username & birthdate), you have two degrees of freedom (two parameters), and the number of possible states of these parameters are the (number of all possible usernames * number of all possible birthdays)

r (correlation coefficient): strength of relationship between x & y: (covariance of x & y) / x standard deviation * y standard deviation
r^2 (determination coefficient): tells you how changes in one variable can be explained by changes in a second variable
z-score: the number of standard deviations from the mean for a particular data point
	z = (x – μ) / σ
standard error: compares the standard deviation of sample means with multiple samples: z = (x – μ) / (σ / √n) 
t-value: ratio of difference between groups, in proportion to the differences within groups
	tells you if a single variable is significant
f-value: ratio of variances: F = s1 / s2
	tells you if multiple variables are jointly significant (influencing each other)
p-value: probability that the data occurred by chance
	- can be determined from the f-value or the t-value
binomial probability (x) = 				  # of trials factorial
						   -------------------------------------------------- * probability(success) ^ # of successes * probability(failure) ^ # of failures
						   # of failures factorial * # of successes factorial


Correlation coefficient (R): tells you the strength of a relationship between variables

    1 = a strong positive relationship
    -1 = a strong negative relationship
    0 = no relationship at all

    - A correlation coefficient of 1 means that for every positive increase in one variable, there is a positive increase of a fixed proportion in the other. 
      For example, shoe sizes go up in (almost) perfect correlation with foot length. 
    - The absolute value of the correlation coefficient gives us the relationship strength. The larger the number, the stronger the relationship

1. Pearsons correlation coefficient: used in linear regression 
	r = n(sum of xy) - (sum of x) * (sum of y)
		--------------------------------------
		square root([n * (sum of x^2) - (sum of x)^2] * [n * sum of y^2 - (sum of y)^2]

2. Sample correlation coefficient: 
	r = sample covariance / sample standard deviation of x * sample standard deviation of y 

3. Population correlation coefficient:
	r = population covariance / population standard deviation of x * population standard deviation of y 


Coefficient of determination (R^2):  tells you how changes in one variable can be explained by changes in a second variable
	the coefficient of determination tells you how many data points fall within the results of the line formed by the regression equation
	So its a measure of accuracy of the regression line, which in turn tells you how much the x-variables explain y

	The adjusted coefficient of determination takes into account the number of variables, and adds a penalty for points that dont fit, which r^2 on its own doesnt penalize
	Adjusted r^2 increases only if a new data point improves the regression more than you would expect by chance, whereas r^2 increase with every new data point & variable

z-score: the number of standard deviations from the mean that a data point x is: 
	z = (x – μ) / σ

standard error: the standard deviation of sample means, when you have multiple samples
z = (x – μ) / (σ / √n)
	tells you how many standard errors there are between the population & sample mean

A z-score tells you where the score lies on a normal distribution curve - it maps to a percentile.
	A z-score of 1 is 1 standard deviation above the mean. 

t score: a ratio between the difference between two groups and the difference within the groups. The larger the t score, the more difference there is between groups
	
	To calculate the t-score:

	ΣD: Sum of corresponding data points differences between samples (corresponding bc they belong to the same person or object, like two test scores a person had)
	ΣD^2: Sum of the squared differences
	(ΣD)^2: Sum of the differences, squared.
	Degrees of freedom (df) = n - 1

	t = 						(ΣD/N)
		-----------------------------------------------------
		square_root[ΣD^2 - ((ΣD)^2)/N / (N - 1) * N]

	  = sum of all differences divided by the number of points n
	  	--------------------------------------------------------
	  	square root of ((the sum of all squared differences minus the (sum of all differences, squared & divided by the number of points)) divided by degrees of freedom * n)

	Now that we have the calculated t-value, lookup the p-value from the t-value using the degrees of freedom & an alpha level of 0.05 unless we have one.
	If the p-value is less than the alpha level, you can reject the null hypothesis (which for the paired t-test is that there is no difference between sample means)

	Compare the calculated t-value (ratio of difference between groups, in proportion to the differences within groups) & the p-value (probability that results occurred by chance).

p-value: the probability that the results from your sample data occurred by chance. Every t-value has a p-value to go with it. 
	Low p-values are good; They indicate your data did not occur by chance. For example, a p-value of .01 means there is only a 1% probability that the results from an experiment happened by chance. 
	The p-value is the probability of getting a result at least as extreme as the one that was actually observed, given that the null hypothesis is true. 
	In most cases, a p-value of 0.05 (5%) is accepted to mean the data is valid.
	The p value is the evidence against a null hypothesis. The smaller the p-value, the strong the evidence that you should reject the null hypothesis.
	When you run a hypothesis test, you compare the p value from your test to the alpha level you selected when you ran the test

    A small p (≤ 0.05), reject the null hypothesis. This is strong evidence that the null hypothesis is invalid.
    A large p (> 0.05) means the alternate hypothesis is weak, so you do not reject the null. 

f-value:
    compare your f-value with your f-critical value. If the f-critical value is smaller than the f-value, you should reject the null hypothesis. 
    The F value in the ANOVA test also determines the P value ***
    The p value is a probability, while the f ratio is a test statistic
    	
    F value = (SSE1 – SSE2 / m) / SSE2 / n-k
    SSE = residual sum of squares
    m = # of restrictions
    k = # of independent variables
    F Statistic (critical value) = variance of the group means (Mean Square Between) / mean of the within group variances (Mean Squared Error)

    	= 						how different the cats average weight is from the dogs average weight
    	  ---------------------------------------------------------------------------------------------------------------------
    	  average of (how different the weights are within the cat group and how different the weights are within the dog group)


    If you get a large f value (one that is bigger than the F critical value found in a table), it means something is significant, while a small p value means all your results are significant. 
    The F statistic just compares the joint effect of all the variables together.
    If you have a significant result, it doesn’t mean that all your variables are significant, so the F statistic must be used with the p-value.
    If the f-table value is smaller than the calculated value, you can reject the null hypothesis.
    Study the individual p values to find out which of the individual variables are statistically significant.

    A Statistical F-test assesses the similarity of two variances: F = s1 / s2
    An F statistic (critical value) is a value you get when you run an ANOVA test or a regression analysis to find out if the means between two populations are significantly different. 
    It’s similar to a T statistic from a T-Test
    A T-test tells you if a single variable is statistically significant
    An F test tells you if a group of variables are jointly significant

    Regression:
    	The F value in regression is the result of a test where the null hypothesis is that all of the regression coefficients are equal to zero (the model has no predictive capability). The f-test compares your model with zero predictor variables (the intercept only model), and tells if your added coefficients improved the model. If you get a significant result, then whatever coefficients you included in your model improved the model’s fit. 

    	To find out if your regression F-value is significant, you’ll need to find the critical value in the f-table.

    F-Test:
    	The f-statistic is used in a variety of tests including regression analysis, the Chow test and the Scheffe Test (a post-hoc ANOVA test).
    	But usually the f-test refers to the f-test to compare two variances.
    	Generally you want to find the f-value, and the f-statistic (the critical value) using the f-table
    	Degrees of freedom is your sample size minus 1. As you have two samples (variance 1 and variance 2), you’ll have two degrees of freedom: one for the numerator variance (columns in f-table) and one for the denominator variance (rows in f-table).
    	The degrees of freedom in the denominator (dfd) is also referred to as the degrees of freedom error (dfe). 
    	

    F-test Assumptions:
	    - The f-test can be used with normally distributed data, where the samples are independent events.
	    - The larger variance should go in the top to make it an easier to calculate right-tailed test.
	    - If your degrees of freedom aren’t listed in the F Table, use the larger critical value. This helps to avoid the possibility of Type I errors.

Chi-square:
	The chi-square statistic tells you if theres a relationship between two categorical variables

	The f-distribution is related to the chi-square distribution bc f-distribution is the ratio of two chi-square distributions with degrees of freedom v1 and v2.
	The f-distributions vary on the degrees of freedom of the numerator & denominator, where a = # of groups, n = # of subjects in experiment

    df_numerator = a – 1
    df_denominator = n – a

    The denominator degrees of freedom is also called the degrees of freedom error

    x^2 = sum of all [(observed - expected value) ^ 2 / expected value]

    A low value for chi-square means there is a high correlation between your two sets of data
    You could take your calculated chi-square value and compare it to a critical value from a chi-square table
    If the chi-square value > critical value, then there is a significant difference
    You could also use a p-value: state the null & alternate hypothesis, then generate a chi-square curve for your results along with a p-value


    Assumptions:
    	- Chi-square statistic can only be used on numbers, not percentages, proportions, means or similar statistical value
    	- Its good for categorical, dichotomous, or ordinal variables
    	- the degrees of freedom = # of categories - 1 = # of samples being summed = ALSO the mean of the distribution
    	- chi-square distributions are always right-skewed
    	- The chi square distribution is the distribution of the sum of a set of random samples (from the normal distribution) squared
    	- So the greater the degrees of freedom, the more the chi square distribution looks like a normal distribution. 

    Distribution:
    	The chi-square distribution is a special case of the gamma distribution
    	A chi square distribution with n degrees of freedom is equal to a gamma distribution with a = n / 2 and b = 0.5

    	Uses:
    	- confidence interval estimation for a population standard deviation of a normal distribution, using a sample standard deviation
    	- the independence of two criteria used for classifying a qualitative variable
    	- relationships between categorical variables 
    	- studying the sample variance for a normal distribution sample
    	- finding the deviations of differences between expected & observed frequencies
    	- the chi-square (goodness-of-fit) test

    The chi distribution describes the square root of a chi-square variable


Rejecting the null hypothesis: 
	Reject the null when your p value is smaller than your alpha level. 
	You should not reject the null if your critical f value is smaller than your F Value, unless you also have a small p-value.

	Read your p-value first. If the p-value is small (less than your alpha level), you can accept the null hypothesis. Only then should you consider the f-value. If you fail to reject the null, discard the f-value result.


T-test types:

    1. Independent Samples t-test compares the means for two groups
    2. Paired sample t-test compares means from the same group at different times
    3. One sample t-test tests the mean of a single group against a known mean

    (1) Independent (Unpaired) Sample t-test: use this if you take a random sample of each group separately & they have different conditions
    	- the null hypothesis is μ1 = μ2. In other words, it assumes the means are equal

    (2) Paired Sample t-test: use this if you have two measurements on the same item, person or thing, or two items being measured under the same unique condition
   		- the null hypothesis is that the pairwise difference between the two tests is equal  H0: µd = 0
   		A paired sample t-test (correlated pairs/dependent samples test) is where you run a t-test on dependent samples.
	    Dependent samples are essentially connected — they are tests on the same person or thing. For example:

	    Dependent sample: Knee MRI costs at two different hospitals, two tests on the same person before/after training, two bp measurements on the same person with different equipment.
	    Unique condition: Cars manufactured by different companies but tested under the same unique conditions.



A critical value is a line on a graph that splits the graph into sections, which identifies the rejection region for a hypothesis.

Critical Value of Z
	A critical value of z (Z-score) is used when the sampling distribution is normal, or close to normal. Z-scores are used when the population standard deviation is known or when you have larger sample sizes.

	The t distribution is used when the sample size is small or when the pop std dev is unknown.

	Every statistic has a probability, and every probability calculated for a sample has a margin of error. 
	The critical value of z can also be used to calculate the margin of error.
	Margin of error = Critical value * Standard deviation of the statistic
	Margin of error = Critical value * Standard error of the sample


	Find a critical z value for a 90% confidence level (alpha = 0.10) (two-tailed test)
		Step 1: Subtract the confidence level from 100% to find the α level: 100% – 90% = 10%.
		Step 2: Convert Step 1 to a decimal: 10% = 0.10.
		Step 3: Divide Step 2 by 2 (this is called “α/2”) - the area in each tail for a 2-tailed test: 0.10 = 0.05. This is the area in each tail.
		Step 4: Subtract Step 3 from 1 (because we want the area in the middle, not the area in the tail): 1 – 0.05 = .95.
		Step 5: Look up the area from Step in the z-table. The area is at z=1.645. This is your critical value for a confidence level of 90%. (the # of std dev above mean)

	Right tailed test: Find a critical value in the z-table for an alpha level of 0.0079.
		Step 1: Subtract alpha (α) from 0.5: 0.5-0.0079 = 0.4921.
		Step 2: Find the result from step 1 in the center part of the z-table. 

T Test
	The t test (also called Student’s T Test) compares two averages (means) and tells you if they are different from each other. The t test also tells you how significant the differences are; In other words it lets you know if those differences could have happened by chance. 

	The t score is a ratio between the difference between two groups and the difference within the groups. The larger the t score, the more difference there is between groups

there are ways for different distributions to have the same metrics. a distribution may have the same mean as another even though every data point is different.
find out which metrics are intrinsically tied to each other: if the mean is the same, does that mean any other metrics are the same by default?
