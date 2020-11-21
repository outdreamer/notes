- star method

	- relevant work problem
	- what tasks were required
	- how did you execute them
	- results

    - Tell me about a time when you were faced with a problem that had a number of possible solutions. What was the problem and how did you determine the course of action? What was the outcome of that choice?
    - When did you take a risk, make a mistake, or fail? How did you respond, and how did you grow from that experience?
    - Describe a time you took the lead on a project
    - What did you do when you needed to motivate a group of individuals or promote collaboration on a particular project?
    - How have you leveraged data to develop a strategy?
    - Describe a situation in which you were able to use persuasion to successfully convince someone to see things your way.
    - Describe a time when you were faced with a stressful situation that demonstrated your coping skills.
    - Give me a specific example of a time when you used good judgment and logic in solving a problem.
    - Give me an example of a time when you set a goal and were able to meet or achieve it.
    - Tell me about a time when you had to use your presentation skills to influence someone&#39;s  opinion.
    - Give me a specific example of a time when you had to conform to a policy with which you did not agree.
    - Please discuss an important written document you were required to complete.
    - Tell me about a time when you had to go above and beyond the call of duty in order to get a job done.
    - Tell me about a time when you had too many things to do and you were required to prioritize your tasks.
    - Give me an example of a time when you had to make a split second decision.
    - What is your typical way of dealing with conflict? Give me an example.
    - Tell me about a time you were able to successfully deal with another person even when that individual may not have personally liked you (or vice versa).
    - Tell me about a difficult decision you&#39;ve made in the last year.
    - Give me an example of a time when something you tried to accomplish and failed.
    - Give me an example of when you showed initiative and took the lead.
    - Tell me about a recent situation in which you had to deal with a very upset customer or co-worker.
    - Give me an example of a time when you motivated others.
    - Tell me about a time when you delegated a project effectively.
    - Give me an example of a time when you used your fact-finding skills to solve a problem.
    - Tell me about a time when you missed an obvious solution to a problem.
    - Describe a time when you anticipated potential problems and developed preventive measures.
    - Tell me about a time when you were forced to make an unpopular decision.
    - Please tell me about a time you had to fire a friend.
    - Describe a time when you set your sights too high (or too low).


- example problems

	- finding two numbers in a sorted array whose sum is a given number
	- write two Python functions to find the minimum number in a list. 
		The first function should compare each number to every other number on the list. O(n2). 
		The second function should be linear O(n).
	- write a boolean function that will take two strings and return whether they are anagrams.
		def is_anagram():
			#strategy 1: iterate through characters in first string, checking if character occurs in second string, and returning false if not

	- Implement Fibonacci recursively and iteratively  
		   // iterative
		   function fibI(n) {
		    if (n === 1 || n === 2) {
		      return 1;
		    }
		    currentFib = 1;
		    previousFib = 1;
		    for (var i = 0; i < n - 2; i++) {
		      currentFib = currentFib + previousFib;
		      previousFib = currentFib - previousFib;
		    }
		    return currentFib;
		  }
		  // Recursive
		  function fibR(n) {
		    if (n === 1 || n === 2) {
		      return 1;
		    }
		    return fibR(n-1) + fibR(n-2);
		  }
	- Determine if a string is an anagram 
	- How would you implement a rest service that returns account details. List out some useful end points and what they would look like. Ex). GET /accounts/<accountId>/
	- The most frequent letter used in a String.
	- basic java recursion questions along with brain teasers from the coding interview book.
	- How to calculate marginal cost of using a phone service. marginal cost is derivative of the cost function
	- Given a string, return the first NON-repeating character that occurs in the string. EX: "adzbdcab" returns 'z'.   
	- What is the difference between overloading and overriding?
	- Implement a linked list and return the kth to last element  
	- You have a tree of accounts. Write a program to sum any sub-account passed in.   
	- What is the difference between an object and a class?   
	- Describe how you would build an online chat system between a customer and a representative.   
	- Given an unsorted collection of logs with types A,B,C write an algorithm to stable sort to logs.   
	- Write an algorithm that finds the nth to last element in a linked list.   
	- Why do we keep variables on the heap in Javascript? 
	- how you would design a system in an object oriented fashion (What objects, properties, data structures)
	- how to call an encryption program and how to use it to encrypt every file in a directory
	- Implement a queue as a stack 
	- You have two linked lists where each list represents some positive number. The ith node in the list represents the ith digit (0-9) of the number. Return a new linked list which represents the sum of the two linked lists
	- implement a function for determining the validity of a string. The string is valid if parentheses are correctly distributed within the string
	- "talk about how you would implement a few classes" given a certain business requirement
	- implementing an algorithm to manage student resumes in java
	- implement binary search tree to return the rightmost child node
	- Reverse a linked List
	- Write a method that checks if a string is a palindrome.
	- how do you select a tool to use

- resources

	- hashmaps, b+trees (& variants), caches (& associated algorithms): www.codechef.com

	- Project Euler questions: http://projecteuler.net/ 

	- Understand high scale architecture: http://highscalability.com/blog/category/example
