elliptic curve

nodes:
	sender:
		attributes:
			type: agent

	receiver:
		attributes:
			type: agent

	origin function:

		definition: y² = x³+ax+b

		attributes:
			restrictions:
				4a³+27b² ≠ 0 (avoid singular points)

			examples:
				y² = x³+7

	agreement_point (G):
		attribute:
			- x & y values that fulfill origin function

	random number (n):
		attributes:
			- which generator to use?
			- 256-bit random value
			- each bit in the integer is a point operation

	private key (n):
		- how many times you add G to itself to get the point P on the curve

	public key (P):

	elliptic curve:
		attributes:
			- symmetric about x-axis
			- the curve has no cusps or self-intersections

	EC+:
		attributes:
			- distributive property

rules:
	- fast additive operation has distributive property
		n•G + r•G = (n + r)•G

	- derive number of fast additive operations required for computing dG: 
		- cG + b (highest number less than d that is a multiple of c, the base used to isolate EC+ operations) * G
		- C = how many operations to calculate cG (1)
		- B = how many operations to calculate bG
		- number(dG) = C + B

		- 4 = 1 to calculate 2 and 3 to calculate 8
		  4 = 2 ^ 0 + 2 ^ 3

	- limit on number of fast additive operation:
		- bc of distributive property of EC+, computing x•G never requires more than 510 EC+ operations 
		restrictions:
			- 256 bit integer n
			- n <= 1.1579209e+77
			- each bit in the integer is a point operation
			- find the binary expansion constants of n:
				n = 2 ^ 0 * a + 2 ^ 1 * b + ... + 2 ^ 256 * z
			- multiply the binary expansion by G
			- add the points in the binary expansion to exploit the distributive property of EC+

	- at most the binary expansion of n will contain 256 elements

	elliptic curve points:
		1. curve point 1 Elliptic+ curve point 2 = curve point 3b 
		2. Elliptic+:
			1. find straight line linking cp1 and cp2 (line1)
		 	2. find cp3a from final intersection of line1 and elliptic curve
		 	3. cp3b = reflect cp3a across x-axis (change sign of y-value)

		3. Elliptic_crypto+:
			1. find tangent line of cp1, t_line1
			2. find cp3a from intersection of t_line1 and elliptic curve
			3. cp3b = reflect cp3a across x-axis
			Successive ec+ operations use the original point and the most recent generated point with these operations

	public-private key:
		P(x,y) = n * G(x,y)

	sender-receiver:
		1. together: agreement on point G(x1,y1)
		2. each: generate public-private key, random number n & point P
		3. together: exchange public keys (P)
		4. each: multiply received public key by own private key (P_other * n_own)
		5. check that they received same point as by multiplying their own public & private keys: point P(x2,y2)
		6. use x-value of point as shared value & use it as input to encryption 


Solution:
	restrictions:
		- prove knowledge of private key without revealing info which can aid in deriving private key
		- public key does not reveal info about private key

	ec+ restrictions:
		- need to prevent n from being derivable from P(x,y) & G(x,y)
			can you guess n in reasonable time knowing points G & P, or how many times you added G to itself to get P?

Questions:
	- can the pattern of successive EC+ added points really not be derived given these restrictions 
		(tangent, adding p1 to itself, intersections)?
	- why is this complicated - bc the cyclical nature of the point addition patterns means there are many solutions to how many rounds of addition could produce P from G?
	- can you convert each curve into a breakable curve relaxing one of its restrictions?
	- each curve is going to have patterns describing the cycles of addition
		https://crypto.stackexchange.com/questions/58539/how-can-there-be-insecure-elliptic-curves-if-the-discrete-logarithm-problem-is-h