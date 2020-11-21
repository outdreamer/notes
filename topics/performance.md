- concurrency 
	- errors in multithreaded applications are often the result of incorrectly sharing state between several threads
	- stateless implemnetation (guarantees same output for an input)
		- doesnt rely on external state
		- doesnt modify state
	- classes that share state
		- immutable classes
			- immutable classes sharing state (cant be modified after construction)	
				- all fields private/final and no setters
		- mutable classes
			- read-only access to mutable classes sharing state
	- classes with local state
		- private fields
			- classes have their own state, but it's not shared with other threads

	- Thread-local fields: like normal class fields, except each thread accessing them via a setter/getter gets an independently initialized copy of the field so that each thread has its own state.

	- create thread-safe collection (not contents) with synchronized Collections
		- Collection<Integer> syncCollection = Collections.synchronizedCollection(new ArrayList<>());
		- use intrinsic locking in each method
		- methods can be accessed by only one thread at a time, & other threads will be blocked until the method is unlocked by the first thread

	- create thread-safe collection (not contents) with concurrent Collections
		- Map<String,String> concurrentMap = new ConcurrentHashMap<>();
		- dividing their data into segments
		- several threads can acquire locks on different map segments, so multiple threads can access the Map at the same time
		- better performance than synchronized collections

	- atomic classes 
		- allow atomic operations which are thread-safe without using synchronization
		- atomic operation is executed in one single machine level operation

	- implement synchronized methods
		- only one thread can access a synchronized method at a time, while blocking access to this method from other threads
		- rely on the use of intrinsic locks
		- When a thread calls a synchronized method, it acquires the intrinsic lock
		- implement in instance methods, static methods, and statements (synchronized statements)

	- intrinsic/monitor locks
		- implicit internal entity associated with a particular class instance
		- avoid using strings or any cacheable or reusable objects as intrinsic locks

	- cpu cache vs. main memory

	- values of regular class fields might be cached by the CPU
	- updates aftering caching, even if they're synchronized, might not be visible to other threads
	- use volatile class fields to instruct JVM & compiler to store variable in main memory, so JVM reads value from the main memory, instead of from the CPU cache

	- not synchronized: arraylist, hashmap

- recursion
	- requires halting condition
	public static int sum(int k) {
      return k + sum(k - 1) if k > 0 else k
    }

- buffers: memory processing tool implementing limit/capacity/mark/current position to access channels

	- write data to a buffer, or from a channel to a buffer

    - Capacity: Maximum data/bytes that can be stored in the Buffer
    	- cannot be altered
    	- Once the buffer is full it should be cleared before writing to it

    - Limit: 
    	- data read/write limit, depending on buffer mode
    	- in write mode of Buffer, the Limit is the capacity, so maximum data that could be written in buffer
    	- in read mode of buffer, the Limit is the limit of how much data can be read from the Buffer

    - Position:
    	- current cursor location in buffer (index of next element to be read/written)
    	- Initially set as 0 at buffer creation time
    	- updated automatically by get() and put() methods

    - Mark:
    	- bookmark of the position in a buffer
    	- mark() records current position 
    	- reset() restores (returns cursor to) marked position

- procedural programming: write functions that perform operations

- object-oriented programming: creating objects with data & methods

- fail fast system: shuts down immediately after the occurrence of an error, operations are instantly aborted & the failures or the errors are exposed

- fail safe system: continues to operate even after a fault/error has occurred, don’t abort an operation & hide errors instead of exposing them

- marshalling: transforming the memory representation of an object to a data format suitable for storage or transmission, and it is typically used when data must be moved

- dependency injection
	- Passing the service to the client, rather than allowing a client to build or find the service
	- client delegates the responsibility of providing its services to external code (the injector)
	- separates the responsibility of "use" from responsibility of "construction"
	- increases readability and code reuse

- inversion of control: 
	- the framework calls the task-specific code (the framework injects control flow to code), vs. custom code executing control flow by calling reusable libraries for generic tasks
	- examples: software frameworks, callbacks, schedulers, event loops, dependency injection, & template method
	- intents
	    To decouple the execution of a task from implementation.
	    To focus a module on the task it is designed for.
	    To free modules from assumptions about how other systems do what they do and instead rely on contracts.
	    To prevent side effects when replacing a module.
	- usage
	    - service locator pattern
    	- Using dependency injection (Constructor, parameter, setter, interface)
    	- Using a contextualized lookup
    	- Using template method/strategy design pattern

- inheritance

        Single Inheritance: a derived class acquires the members of a single super class
        	- class B extends A // no other class extends A

        Multi-level inheritance:
        	- class A
        		- class B extends A
        			- class C extends B

        Hierarchical inheritance:
        	- class A
        		- class B1 extends A
        		- class B2 extends A

        Multiple inheritance: a derived class is inherited from more than one base class:
        	- class A
        					- class C extends A,B // order doesnt clarify runtime ambiguity
        	- class B

        Hybrid: mix of inheritance types (multilevel, hierarchical)
        	- class A
        	- class B extends A 
        		- class C1 extends B // hierarchical
        		- class C2 extends B // hierarchical

- thread vs. process

	- thread vs. process use case/limits

		- concurrency problems
			- there is no way to know in which order the code will run if a thread executes simultaneously to a program or another thread
			- When the threads and main program are reading/writing the same variables, the values are unpredictable
			- to avoid this, share as few attributes between threads as possible
			- If attributes must be shared, use the isAlive() method to check if thread has finished running before using attributes it can change
				 while(thread.isAlive()) {

		- python

			- best practice
				- use queue module to feed that thread with requests from other threads

		    - python thread mechanism
	        	Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any one time. 
	        	A thread acquires the GIL, does a little work, then passes the GIL onto the next thread.
	        	This happens very quickly so to the human eye it may seem like your threads are executing in parallel
	        	threads are really just taking turns using the same CPU core.
	        	All this GIL passing adds overhead to execution

		- java

			- multitasking: 
				- allows more than 2 processes to run concurrently
				- allows more than 2 threads to run concurrently

			- java can do thread-based multitasking

			- you cannot extend any other class if you extend the thread class
			- you can extend from another class by implementing the Runnable interface
				class MyClass extends OtherClass implements Runnable

			- create a thread:

				- define a class that extends Thread class & overrides run( ) method of Thread class

					class classA extends Thread {
						public void run( ){}
						public static void main(String args[ ]){
							classA a1 = new classA( );
							a1.start( );
						}
					}
				
				- implement Runnable interface that implements only run( ) method

					class classA implements Runnable {
						public void run(){}
						public static void main(String args[]){
							classA a1 = new classA();
							Thread t1 = new Thread(a1);
							t1.start();
						}
					}


			- thread lifecycle
			- deadlock
			- daemon thread
			- thread garbage collection
			- synchronization
				- static
				- synchronized method/block
			- Thread Scheduler (preemptive scheduling vs. time slicing)


		- process:
			- a program being executed
			- provides an environment for the execution of the thread
			- switching between processes requires:
				- saving/loading registers/memory maps
				- updating lists
			- kernel-based
			- used for concurrent/sequential program execution
			- a terminated process cannot be recovered in its pre-termination state, since if a process dies, all threads die including the process
			- OS creates/schedules/terminates processes for the use of the CPU
			- uses process lifecycle states to track activity
			- lifecycle states: ready, running, blocked, terminated
			- higher number of system calls bc it uses IPC (Inter-process communication) for communication
			- can call child processes (separate system calls) or threads (uses PCB)
			- has its own Process Control Block, Stack and Address Space
			- process control block:
				- process id
				- priority
				- state
				- pws
				- contents CPU register
			- components
				- stack/heap memory
				- instruction
				- data
				- memory map
				- address space
				- global variables
				- signal handlers
				- open files
				- child processes
				- accounting information

			- functions
	    		- Scheduling: selecting process sequence for CPU
	    		- Dispatching: sets up process execution environment
	    		- Context save: saves process information when it gets resumed or blocked

	    - threads (light weight process)
	    	- an execution of a program, given a process execution environment
	    	- allow simultaneous execution of tasks that dont need sequence, like running I/O & computations simultaneously
	    	- Threads are independent (doesn't affect other threads if an exception occurs in one thread)
	        - consumes less resources, and takes less time to communication, destroy, create, switch contexts
	        - thread switching does not require calling a OS switching interface
			- uses process resources for a task
			    - has Parents’ PCB, plus its own Thread Control Block, Stack, shared Address space
			    - shares: instruction, global & heap regions
			    - has its own individual stack & registers
				- kernel allocates a stack & thread control block (TCB) to each thread
				- a thread can be recovered using its associated stack
			- OS only saves stack pointer & CPU state when switching between threads of same process
			- contained in a process, cannot exist independently of a process
			- inter-thread interaction management can be more complicated, as threads need a priority assigned
			- thread types:
				- kernel-level: part of the OS
				- user-level
				- hybrid
			- components
				- register
				- state
				- program counter
				- stack
	        - locks let you synchronize threads, specifying whether they should be blocking or not
		    - synchronization primitives (locks, events, conditions, & semaphores) help coordinate sharing data/resources across threads
			- lifecycle states: running, ready, blocked
			- only includes computational state, not resource allocation & communication state, which reduces switching overhead
			- enhances the concurrency (parallelism) which increases speed
	        - best practices:
	            - concentrating access to a resource in one thread
	            - reducing attributes shared across threadss