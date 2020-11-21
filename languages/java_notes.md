
- java:

	- features
	
		- interpreted

		- oop: inheritance, encapsulation, abstraction, polymorphism

		- optimization barriers
			- java app scalability & performance on multi-core systems is limited by the object allocation rate
			- garbage collection on multiple cores can help with this
			- startup time: higher bc loading many classes
			- uses more memory than C++
			- jit compilation time: similar to C#, slower than C, faster than languages without a jut/aot compiler
			- using JNI/JNA adds overhead
			- JVMs have scalability issues, especially with static hardware

		- optimizations

			- Java String pool 
				- collection of Strings stored in heap memory
				- whenever a new object is created, String pool first checks if object is already present in the pool
				- if present, same reference is returned to variable
				- otherwise new object is created in String pool & new object reference is returned

			- just in time compilation
				- HotSpot can deoptimize code formerly JITed, allowing fall back to a safe path
				- jit compiler compiles bytecode of invoked method into native machine code, compiling it “just in time” to execute
			    - Once method is compiled, JVM calls compiled code directly, rather than interpreting it

			- adaptive optimizing
				- dynamic recompilation of parts of a program based on the current execution profile
				- examples:
					- make a trade-off between just-in-time compiling and interpreting instructions
					- exploit local data conditions to optimize away branches & use inline expansion

			- perform processor specific optimizations/inline expansion

			- garbage collection
				 - JVM formerly used a mark-sweep collector, which could fragment the heap after a garbage collection
				 - JVMs changed to a generational collector, with better defragmentation behaviour
				 - Replace existing concurrent low-pause garbage/mark-sweep (CMS) collector with Garbage First (G1) collector to ensure consistent pauses over time

			- Compressed Oops
			- Split bytecode verification
			- Escape analysis and lock coarsening
			- Register allocation improvements
			- Class data sharing
			- Java Quick Starter reduces application start-up time
				- preloading/disk cache
			- prioritized downloads
			- Provide JVM support for dynamic programming languages
			- Enhance concurrency library with parallel computing on multi-core processors
			- Allow the JVM to use both client & server JIT compilers in same session with tiered compiling

		- object-oriented (encapsulate data/method, with abstraction for reusability/organization, implements concepts like interfaces/inheritance/polymorphism)
		- platform-independent (bytecode is same)
			- Java includes a software-based platform (platform provides environment where programs can run)
				- platform components: provides its own JRE & API
		- high performance, multithreaded, and portable
		- secure (doesn't use explicit pointers)
			- JVM is responsible for implicit memory allocation, so it avoids direct pointer memory access by user
		- dynamic loading of classes (classes loaded on demand)
		- strong memory management, automatic garbage collection
		- supports pointer internally (but can't write pointer program in java)
		- source code is converted into bytecode at compilation time, interpreter executes bytecode at runtime 
		- Java is interpreted
		- supports call by value only (no call by reference in java)
			- All object references in Java are passed by value
			- a copy of the value will be passed to a method
			- object variables are references pointing to real objects in memory heap
			- even though Java passes parameters to methods by value, if the variable points to an object reference, the real object will also be changed
		- can override all non-static methods by default
		- always uses a single inheritance tree because all classes are the child of java.lang.Object class (root of the inheritance tree)
		- everything (except fundamental types) is an object in Java

		- annotations
			- override: use when inheriting a method to replace its functionality

		- java has no:
			- keywords for delete, next, main, exit or null
			- operator overloading
			- pointers (variable referencing memory address) are not used in Java because they are unsafe/unsecured

		- inheritance
			- used for runtime polymorphism, reusability, data/method hiding, method overriding
			- java has no multiple inheritance through class (can be achieved by interfaces) to avoid runtime ambiguity of class identity

		- rules:
			- order of specifiers doesn't matter in Java
			- local variables are not initialized to any default value, neither primitives nor object references
			- All object references are initialized to null in Java

		- void: method without a return value
			public void myMethod(int x) { system.out.println("str"); }
			public int myMethod(int x) { return x + 1; }

		- local vs. instance
			- local variable inside a method/constructor/block has only local scope, can be used only within a block
			- instance variable is bounded to object instance of class, declared within a class & outside a method

		- break/continue
			- break can be used in switch & ends innermost loop
			- continue in a loop in a switch will trigger next loop iteeration

		- infinite loop has no functional exit, will continue until app exists
			- example: for(;;)

		- nested classes: group classes that belong together
			- inner class can be private, protected, or static
			- inner class can access attributes/methods of outer class
			class OuterClass {
			  class InnerClass {}
			}
			OuterClass.InnerClass myInner = myOuter.new InnerClass();

		- aggregations

			- employee class owns an address class, and has an address class reference/object
				class Employee {
					Address address;
				}

			- association: relationship where objects have their own lifecycle with no owner

			- aggregation:
				- objects have their own lifecycle, but there is ownership
				- child object can not belong to another parent object
					- if parent is deleted, child will not be deleted

			- composition (strict aggregation): one class cannot exist without another
				- Holding the reference of a class within some other class
				- if parent is deleted, child will also be deleted
        
		- equals vs. ==
			- Equals() checks object value equivalence
			- == checks if objects are the same object (same memory address)

		- heap vs. stack memory

			- stack
				- used to execute threads
				- used by one thread execution (cant be accessed by other threads)
				- referenced in LIFO
				- exists until end of thread execution
				- only contains method-specific values (local primitive/reference variables to objects in heap space)
				- Whenever a method is invoked, a new block is created in the stack memory
				- block is available to other methods at end of method execution

			- heap
				- used by all application parts executed in JRE
				- Memory management based on object generation
				- Heap memory lives from start-to-end of app execution
				- all objects & JRE classes are stored in the Heap space
				- garbage collection frees heap memory once an object has zero references
				- objects in heap space can be referenced by any part of the application

		- modifiers

			- access modifiers
			    Public: accessed by any class/method
			    Protected: accessed in same package/class/sub-classes
			    Private: accessed in class only
			    Default: accessed in same package only (used if no modifiers specified)

			- classes: 
				- public, default

				- non-access modifiers
					- final: class cannot be inherited by other classes (ends inheritance chain)
						- final blank variable
							- cannot be initialized at declaration
							- can be initialized only once
							- useful when user has data that shouldnt be changed by others
							- can be static
							- if not static, can be initialized in class constructor
						- cannot declare as final:
							- constructor is never inherited
							- interface must be implemented by a class to be defined
							- abstract method must be overridden in a class to be defined

					- abstract: class cannot be used to create objects

			- attributes/methods/constructors: 
				- public, private, protected, default

				- non-access modifiers
					- final: cannot be overridden/modified
					- static: belong to class, rather than an object
					- abstract: only be used in an abstract class, and only on methods. The method does not have a body, for example abstract void run()
					- transient: skipped when serializing the object containing them
					- synchronized: only be accessed by one thread at a time
					- volatile: value of an attribute is not cached thread-locally, always read from the "main memory"

		- enum: a special "class" for a group of constants (unchangeable variables, like final variables)
			- definition: enum EnumName { LOW, MEDIUM }
			- access: EnumName myVar = EnumName.MEDIUM; 
			- can be defined in a class
			- often used in switch statements to check for possible supported values in a list
			- enum can have attributes and methods
			- enum constants are public, static & final - use with values that wont change

		- file
			- instantiate
				import java.io.File; 
				import java.io.FileWriter;
				import java.util.Scanner;
				import java.io.IOException;
				import java.io.FileNotFoundException;
				
				File myObj = new File("filename.txt"); // IOException
				myObj.createNewFile();

				FileWriter myWriter = new FileWriter("filename.txt"); // IOException
      			myWriter.write("content");
      			myWriter.close();

      			// myObj.delete()

      			if (myObj.exists()) {
	      			Scanner myReader = new Scanner(myObj); // FileNotFoundException
				    while (myReader.hasNextLine()) {
				        String data = myReader.nextLine();
				    }
				    myReader.close();
				}

			- methods
				canRead(): Tests whether the file is readable or not
				canWrite(): Tests whether the file is writable or not
				createNewFile(): Creates an empty file
				delete(): Deletes a file
				exists(): Tests whether the file exists
				getName(): Returns the name of the file
				getAbsolutePath(): Returns the absolute pathname of the file
				length(): Returns the size of the file in bytes
				list(): Returns an array of the files in the directory
				mkdir(): Creates a directory


		- buffer
			- a fixed sized container of memory segments
			- used to write/read data from channel, acting as channel endpoints to interact with a memory block

			- define file resource for input stream: 
				file = Paths.get("C:\\path\filename.txt");

			- create input stream
				InputStream inputStream = Files.newInputStream(file);  
			- create inputStreamReader and pass to BufferedReader
				BufferedReader(new InputStreamReader(inputStream)
			- use BufferedReader to read contents of buffered file input stream reader
				 BufferedReader.readLine()

			- allocate a buffer, read/write, then close

			- methods

			    - allocate(int capacity)
			    	- allocates a new buffer with capacity as parameter

			    - read() & put() 
			    	− read (method of channel) writes data from channel to buffer
			    	- put (method of buffer) writes data in buffer

			    - flip()
			    	- switches buffer mode from writing/eading mode
			    	- sets position back to 0
			    	- sets limit to where position was at time of writing

			    - write() & get()
			    	- write (method of channel) is used to write data from buffer to channel
			    	- get (method of buffer) reads data from buffer

			    - rewind()
			    	- used to reread, sets the position back to zero & doesnt change limit

			    - clear & compact are both methods are used to make buffer from read to write mode

			    - clear()
			    	- sets the position to zero & limit equal to capacity
			    	- in this method the data in the buffer is not cleared, only the markers are re-initialized

			    - compact()
			    	- used if unread data remains, and we still need to write data to channel
			    	- compact() copies unread data to beginning of buffer & set position to right after last unread element
			    	- limit property remains at capacity

			    - mark() & reset() 
			    	- mark method is used to mark any particular position in a buffer
			    	- reset sets position back to marked position


			- example
				Path file = null;  
		        BufferedReader bufferedReader = null;  
		        try {  
		            file = Paths.get("C:\\path\filename.txt");  
		            InputStream inputStream = Files.newInputStream(file);  
		            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));  
		            System.out.println(bufferedReader.readLine());  // read first line
		        } catch (IOException e) {  
		            e.printStackTrace();  
		        } finally {  
		            try {  
		                bufferedReader.close();  
		            } catch (IOException ioe) {  
		                ioe.printStackTrace();  
		            }  
		        }  

		- lambdas
			- parameter -> expression
			- (var1, var2) -> { code block} 
			- numbers.forEach( (n) -> { System.out.println(n); } );
			- Expressions have to immediately return a value & cannot contain variables/assignments/statements like if/for
			- expressions can be a code block with a return statement if wrapped in braces

			- can be stored in variables if the variable's type is an interface with only one method, and if the expression has same param number/return type
			    Consumer<Integer> method = (n) -> { System.out.println(n); };
    			numbers.forEach( method );

    		- can be used in a method if a single-method interface is a param

	    		interface CustomLambdaInterface {
				  String singleLambdaInterfaceMethod(String str);
				}

				class A {
					public static void main(String args[]) {
						CustomLambdaInterface ask = (s) -> s + "?";
						functionWithLambdaParam("some str", ask)
					}
					public static void functionWithLambdaParam(String str, CustomLambdaInterface ask) {
						String result = ask.singleLambdaInterfaceMethod(str)
					}
				}

		- static methods/variables
			- part of the class (not object)
			- cant be overridden
			- must be called like className.methodName
			- used to define variables/methods common to all objects of the class
			- do not need to create the object to access static variables
			- Static variable gets memory only once in the class area at classloading
			- makes program more memory efficient in that it saves memory
			- Static block 
				- initializes static data member, executed before main method, at classloading
					class A {
					  static{System.out.println("static block is invoked");}  
					}
				- enables executing a program without a main method
			- static method can: 
				- access/change static variable value
			- static method cannot: 
				- use non-static data member or call it directly
				- use this/super
			- main method is static bc object isnt required
				- if you remove 'static' from main, the program compiles but throws an error
				- can declare the main method as static
			- making abstract methods static makes them a callable part of the class, but theyre still undefined even if callable
			- can use static methods in an abstract class
		
		- packages
			- avoid name collisions, provide access control, provide hidden classes
		
		- commands
			- run: java A
			- compile:  javac A.java

		- strings
			- string concatenation: "Java" + 10 + 20
			- strings are immutable, faster than stringbuffer/builder, are thread-safe, use constant string pool
				- immutability enhances security, caching, synchronization, and performance of the application
			- string buffer/builder 
				- are mutable & use heap memory
				- string buffer is thread-safe but stringbuilder is faster

		- type parameterization
			- types that take other types as params
			- allows writing generic classes/traits, and specify a type allowed in a general object type

				class MyClass<T> {
				    private T obj;
				    public MyClass<T>(T obj) {
				        this.obj = obj;
				    }
				    public int getId() {
				        return obj.hashCode();
				    }
				}
				int sid = new MyClass<String>("str").hashCode();

		- map
			- Map: maps unique keys to values
			- doesn’t contain duplicate keys
    		- Each key can map at max one value
    		- not part of collections, implemented by java.util

    	- collections
    		- interfaces: iterable, collection, list, queue, set, deque, sortedset
    		- class: array list, linked list, vector, stack, priority queue, array deque, hash set, linked hash set, tree set

		- Array vs. ArrayList
			- arrayList can contain different data type, can change in size, doesnt require specifying index, are type parameterized, and cannot contain primitive data types (only objects)

		- function
			- all functions in Java are virtual by default

		- Constructor chaining 

			- call one constructor from another constructor of the class, with respect to the current class object
			- can be done:
				- in same class using this()
    			- from extended class using super()

				class B extends A {
				    public B(int A1, String A2, String A3, float salary) {  
				        super(A1,A2,A3);  
				    }  

		- class
			- instanceof: Checks if an object is an instance of a specific class or an interface
			- interface: 
				- empty/Marker interface: interface having no data member and member functions
			- class
			- constructor:
				- does not have return type
				- default constructor is provided
				- must have same name as class
			- module
			- package
			- clone: creates exact copy of object
			- import/exports
			- requires
			- var: declares a variable
			- super: specifies class inherited from
			    - refer to the immediate parent class instance variable
			    - call the immediate parent class method
			    - super() can invoke immediate parent class constructor
			    - super() is implicitly invoked by compiler if no super() or this() is included explicitly in the derived class constructor
				- super and this must be the first statement inside constructor otherwise the compiler will throw an error
				- cant use both super/this in constructor
			- this: 
				- refers to current object/constructor
				- used to differentiate between local/instance variables when passed in the class constructor
				public class MyClass {
					int x;
					public MyClass(int x) { // constructor
					    this.x = x;
					}
					public static void main(String[] args) {
						MyClass classInstance = new MyClass(0);
						System.out.println(classInstance.x);
					}
				}


			    - call current class constructor/method
			    - return current class object
			    - can be passed into methods/constructors
			    - cannot assign to this
			    - can be used in the synchronized block

			- throws: specifies which exceptions a method can throw
			- throw: create a custom error
				throw new ArithmeticException("custom");
			- native: methods written in another language
			- implements: designate an interface that is implemented by a class
			- abstract class: 
				- a restricted class that cannot be used to create objects
				- to access it, it must be inherited from another class
				- can have both abstract and regular methods
				abstract class Test
			- public class TestClass extends Test   
			- interface 
				interface Animal {
			  		public void run(); // interface method (does not have a body)
				}

		- java bean: 
			- classes that encapsulate many objects into a single object (the bean)
			- serializable
			- have a zero-argument constructor
			- allow access to properties with getter/setter methods

		- encapsulation:
			- Class attributes can be made read-only/write-only
			- data is hidden & accessed only via current class methods
			- makes sure sensitive data is hidden from users
    			- declare class variables/attributes as private
   				- provide public get/set methods to access and update the value of a private variable

				  private String name;
				  public String getName() { return name; }
				  public void setName(String newName) { this.name = newName; }

		- method oveerloading
			- method overloading, multiple methods can have the same name with different parameters
			- methods must have a different signature
			- increases readability, adds/extends functionality
			- compile-time polymorphism (as opposed to runtime polymorphism/dynamic method dispatch)
			- method overloading cant be done by 
				- changing return type
				- applying static keyword (doesnt change param count/type)
			- if there are two params & param types are reversed in overloaded methods, function selection is an ambiguity
			- can overload main method
			- type promotion is an example of method overloading
				- one data type is promoted to another if no exact matching is found

		- abstraction: abstract classes & interfaces

			- abstract class
				- can have instance variables, non-abstract methods, any visibility
				- can provide default implementation
				- can contain constructors
				- faster relative to interfaces 
				- class can only extend one abstract class

			- interface:
				- collection of abstract public methods & static constants governing extending classes
				- doesnt have a constructor
				- provides signature but not code
				- may be public or none
				- add overhead, require adding methods to child classes if a method is added to interface
				- classes can implement multiple interfaces

		- polymorphism allows custom logic in same method name inherited from base class
			- runtime polymorphism/dynamic method dispatch: call to an overridden method is resolved at runtime vs. compile-time

			class Animal {
			  public void animalSound() {}
			}
			class Dog extends Animal {
			  public void animalSound() {
			  	super.animalSound(); // Call the superclass method
			  }
			}

			- for adding specificity to an inherited function
			- params must be the same
			- overridding methods must have same method name, signature, and IS-A relationship

			- cant override:
				- static method 
					- static attributes/methods are bound to the class
					- static gets memory in class area
					- instance gets memory in a heap
				- private method
					- not accessible outside the class
			- can override:
				- an overloaded method
			- can change:
				- return type (covariant)
					- can change the return type of overridden method, if the return type is subclass type
				- scope of overridden method
					- but cant decrease accessibility (make it more private), only increase
						- private -> protected -> default -> public
				- throws clause of superclass method, while overriding it in the subclass
				    If the superclass method 
				    	- does not declare an exception
				    		- subclass overridden method 
				    			- cannot declare the checked exception
				    			- can declare the unchecked exception
				    	- declares an exception
				    		- subclass overridden method 
				    			- can declare same, subclass exception or no exception
				    			- cannot declare parent exception


		- main
			- public static void main (String args[]) 

		- print: 
			- System.out.println("Hello Java");

		- wrapper classes
			- ArrayList<Integer> myNumbers = new ArrayList<Integer>(); // Valid as collections like ArrayList can only store Object versions of primite type keywords like int

		- exceptions

		    try {
		      int[] myNumbers = {1, 2, 3};
		    } catch (Exception e) {
		      System.out.println("Something went wrong.");
		    } finally {
		      System.out.println("The 'try catch' is finished.");
		    }

		- loop: 
			- do-while
				do {
				  // code block to be executed at least once before modification
				}
				while (condition); // while needs exit condition like recursive methods

			- loop through enum
				for (EnumName var1 : EnumName.values()) {

			- for(int i=0; i < array.length; i++)   
			- for (String i : cars) {
			- avoiding nested for loops:
				- in python: for f, b in zip(foo, bar):
					- Functional Java: zip, zipWith and zipIndex 

				- python generator
					def iterate_multi(*lists):
					    for i in range(min(map(len,lists))):
					        yield tuple(v[i] for v in lists)

					for v1, v2, v3 in iterate_multi(list1,list2,list3):
					    print(str(v1) + "," + str(v2) + "," + str(v3))

				- For collections that implement the List interface
					- listIterator() method to use two methods 
						- nextIndex(), to get the index
						- next(), to get the value (like other iterators)

				- iterator

					List<String> numbers = Arrays.asList("zero", "one", "two");
					ListIterator<String> it = numbers.listIterator();
					while (it.hasNext()) {
					    System.out.println(it.nextIndex() + " " + it.next()); // Print next index & item, advance to next item
					}

		- operators

		- switch
			switch(expression) {
			  case x:
			    break;
			  default:
			}

		- arrays: 
			- String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
			- cars[0] = "new car";
			- loop through array
				for (int i = 0; i < cars.length; i++) {
				for (String i : cars) {

		- get random number: int randomNum = (int)(Math.random() * 101); // between 0 and 100

		- types
			- string
				- find first index of string: txt.indexOf("string")
				- str.concat(str2)
				- backslash: "this string hasn\'t errored out" # also supports \n, \t, \r carriage return, \b backspace, \f form feed

		- type casting
			- small to large:
				 byte -> short -> char -> int -> long -> float -> double
			- automatic widening casting: double myDouble = myInt; 
    		- manual narrowing casting: int myInt = (int) myDouble; 

		- copy values from one object to another
		    By constructor
		    By assigning the values of one object into another
		    By clone() method of Object class

		- constructors
			- not inherited or final
			- no point in making them static bc theyre used on object creation
			- constructors can be overloaded by changing argument number/data type
				class Test {  
				    int i;   
				    public Test(int k) {}  
				    public Test(int k, int m) {}
				}
			- used to initialize object state
			- invoked when the class is instantiated & memory is allocated for the object
			- name of the constructor must be similar to the class name (method names cannot be class names)
			- constructor must not have an explicit return type (methods must have a return type)
				- constructor implicitly returns current instance of class
			- types:

   				- Default Constructor: 
   					- does not accept any value
   					- used to initialize instance variables with default values
   					- can be used for performing a task on object creation
   					- invoked implicitly by the compiler if there is no constructor defined in the class

			    - Parameterized Constructor:
			    	- initialize the instance variables with the given values
			    	- constructors which can accept arguments 

		- JVM: 

			- loads/verifies/executes code

			- converts source code to bytecode, provides spec for runtime environment specification/implementation/instance
			
			- JVM specifies memory area, class file format, registers, garbage-collected heap, fatal error reporting

			- class loader
					- bootstrap: loads the rt.jar file which contains all class files of Java Standard Edition
					- extension: child of Bootstrap & parent of System, loads jar files in $JAVA_HOME/jre/lib/ext directory
					- system/application: loads the classfiles from classpath
			
			- memory areas
				- class method area: stores class structures (runtime constant pool, field & method data, method code)
				- heap: runtime data area where objects are allocated
				- stack:
					- Java Stack stores frames
					- holds local variables & partial results
					- involved in method invocation & return
					- A new frame is created each time a method is invoked, destroyed on method completion
					- Each thread has a private JVM stack
				- native method stack: native methods used in an app
				- PC (program counter) register: contains address of JVM instruction being executed

			- native method interface
				- Java Native Interface (JNI): allows communication with apps in other languages (send output to console, interact with OS libraries)
				- Java Native Access: dynamic code access at runtime, without code generation
				- analogous to Python's ctypes

			- execution engine:
			    - A virtual processor
			    - Interpreter: Read bytecode stream, execute instructions
			    - Just-In-Time(JIT) compiler
		- JRE: implementation of JVM
		- JDK: includes JRE & dev tools (standard, enterprise, micro)

	- tools
		- RMI and EJB are used for creating distributed applications
		- Java Naming and Directory Interface (JNDI):  API for directory services
		- Java Persistence API (JPA): A specification for object-relational mapping
		- Java Data Objects (JDO): A specification of Java object persistence
		- Akka: Toolkit/runtime for building concurrent/distributed apps on the JVM
		- HBase: Non-relational, distributed database modeled after Google's BigTable 
		- Spark: Fast and general engine for big data processing, with built-in modules for streaming, SQL, machine learning and graph processing. 
		- Hibernate: 
			- Object-relational mapping tool, provides a framework for mapping an object-oriented domain model to a relational database
			- handles object-relational impedance mismatch problems by replacing direct, persistent database accesses with high-level object handling functions
			- mapping from Java classes to database tables
			- mapping from Java data types to SQL data types
			- data query and retrieval facilities
			- generates SQL calls and handles result object conversion
		- Jackson: High-performance JSON processor for Java
		- JAX-WS: Java API for XML Web Services
		- JAX-RS: Java API for RESTful Web Services
		- JAX-RPC: Java API for XML-Based RPC
		- web apps
			- Tomcat: Tomcat Server, is an open-source Java Servlet Container 
			- ejb vs. spring
				- EJB: 
					- a specification of Java EE, good for server-side development
					- only supports jpa, jta
					- bean-managed persistence, extended persistence context
					- stateful session beans
					- declarative/programmatic security
					- container-managed remote method calls
					- messaging with message-driven beans
					- simple scheduling with timer
					- aop support with intercepters
					- can inject EJB’s data, JMS & JPA resources in the container
				- Spring: 
					- a framework, for building entire app
					- supports integration with persistence technologies
					- web container session management
					- declarative security through spring config & acegi security framework
					- supports remote calls with RMI, JAX-RPC and web services
					- add listener config for messaging
					- add quartz for scheduling
					- can inject Lists, properties, map & JNDI resources

			- spring:
				- app framework and inversion of control container for the Java platform
				- features can be used by any Java app, but there are extensions for building web apps on Java EE
				- supports services:
				    
				    - Spring Core Container: this is the base module of Spring and provides spring containers (BeanFactory and AppContext)
				    
				    - Aspect-oriented programming: enables implementing cross-cutting concerns
				    
				    - Authentication and authorization: configurable security processes that support a range of standards, protocols, tools and practices via the Spring Security project 
				    
				    - Convention over configuration: a rapid app development solution for Spring-based enterprise apps is offered in the Spring Roo module
				    
				    - Data access: working with relational database management systems on the Java platform using Java Database Connectivity (JDBC) and object-relational mapping tools and with NoSQL databases

				        Resource management - automatically acquiring/releasing database resources
					    Exception handling - translating data access related exception to a Spring data access hierarchy
					    Transaction participation - transparent participation in ongoing transactions
					    Resource unwrapping - retrieving database objects from connection pool wrappers
					    Abstraction for binary large object (BLOB) & character large object (CLOB) handling

					    - configure beans for Hibernate:

					        A Data Source like com.mchange.v2.c3p0.ComboPooledDataSource or org.apache.commons.dbcp.BasicDataSource
						    A SessionFactory like org.springframework.orm.hibernate3.LocalSessionFactoryBean with a DataSource attribute
						    A HibernateProperties like org.springframework.beans.factory.config.PropertiesFactoryBean
						    A TransactionManager like org.springframework.orm.hibernate3.HibernateTransactionManager with a SessionFactory attribute

				    - Inversion of control container: configuration of app components & lifecycle management of Java objects, done mainly via dependency injection
				    
				    - Messaging: configurative registration of message listener objects for transparent message-consumption from message queues via Java Message Service (JMS), improvement of message sending over standard JMS APIs
				    
				    - Model–view–controller: an HTTP/servlet-based framework providing hooks for extension/customization for web apps and RESTful (representational state transfer) Web services

				    	- primary interfaces:
					        Controller: comes between Model and View to manage incoming requests and redirect to proper response. Controller will map the http request to corresponding methods. It acts as a gate that directs the incoming information. It switches between going into model or view.
						    HandlerAdapter: execution of objects that handle incoming requests
						    HandlerInterceptor: interception of incoming requests comparable, but not equal to Servlet filters (use is optional and not controlled by DispatcherServlet).
						    HandlerMapping: selecting objects that handle incoming requests (handlers) based on any attribute or condition internal or external to those requests
						    LocaleResolver: resolving and optionally saving of the locale of an individual user
						    MultipartResolver: facilitate working with file uploads by wrapping incoming requests
						    View: responsible for returning a response to the client. Some requests may go straight to view without going to the model part; others may go through all three.
						    ViewResolver: selecting a View based on a logical name for the view (use is not strictly required)

				    - Remote access framework: configurative remote procedure call (RPC)-style marshalling of Java objects over networks supporting Java remote method invocation (RMI), CORBA (Common Object Request Broker Architecture) and HTTP-based protocols including Web services (SOAP)

				    - Transaction management: unifies several transaction management APIs, coordinates transactions for Java objects
				        - working with local/global transactions (local transaction does not require an app server)
					    - working with nested transactions, savepoints, and almost all environments of the Java platform
					    - manages transactions handled by JDBC Connection, Object-relational mapping Units of Work, JTA TransactionManager and UserTransaction, and other resources like object databases
					    - allows setup of a transactional system through configuration without having to rely on JTA or EJB. The transactional framework also integrates with messaging and caching engines. 

				    - Remote management: configurative exposure/management of Java objects for local/remote configuration via Java Management Extensions (JMX)
				    - Testing: support classes for writing unit/integration tests


				- Spring Boot
					- Spring's convention-over-configuration solution for creating stand-alone, production-grade Spring-based Applications that you can "just run"
					- preconfigured with the Spring team's "opinionated view" of the best configuration and use of the Spring platform and third-party libraries so you can get started with minimum fuss
					- Most Spring Boot applications need very little Spring configuration. 
					- Features:
					    Create stand-alone Spring applications
					    Embed Tomcat or Jetty directly (no need to deploy WAR files)
					    Provide opinionated 'starter' Project Object Models (POMs) to simplify your Maven configuration
					    Automatically configure Spring whenever possible
					    Provide production-ready features such as metrics, health checks and externalized configuration
					    Absolutely no code generation and no requirement for XML configuration.

				- Spring Roo
					- a community project which provides an alternative, code-generation based approach at using convention-over-configuration to rapidly build applications in Java
					- supports Spring Framework, Spring Security and Spring Web Flow
					- Roo differs from other rapid application development frameworks by focusing on:
					    Extensibility (via add-ons)
					    Java platform productivity (as opposed to other languages)
					    Lock-in avoidance (Roo can be removed within a few minutes from any application)
					    Runtime avoidance (with associated deployment advantages)
					    Usability (particularly via the shell features and usage patterns)

			- EJB: 
				- a Java API for modular construction of software
				- server-side software component that encapsulates business logic of an app
				- EJB web container provides a runtime environment for web related software components
				- allows standard handling of:
				    Transaction processing
				    Integration with the persistence services offered by the Java Persistence API (JPA)
				    Concurrency control
				    Event-driven programming using Java Message Service and Java EE Connector Architecture
				    Asynchronous method invocation
				    Job scheduling
				    Naming and directory services (JNDI)
				    Java servlet lifecycle management
				    Interprocess Communication using RMI-IIOP and Web services
				    Security (JCE and JAAS)
				    Deployment of software components in an app server

			- JavaFX: software platform for creating/delivering desktop apps, as well as rich Internet apps (RIAs) that can run across a wide variety of devices, intended to replace Swing
			
			- Generics: allow compile-time type checking without creating many container classes, each with almost identical code, and prevents certain runtime exceptions from occurring by issuing compile-time errors
			
			- just in time compilation
				- When Java bytecode is executed by an interpreter, execution is slower than execution of same program compiled into machine language.- just-in-time (JIT) compilers for executing Java bytecode may translate Java bytecode into machine language while executing the program
				- translated parts of program are executed much faster than they could be interpreted
				- This is applied to frequently executed parts of a program

			- JNLP (Java Network Launch Protocol)
				- a file format used for launching Java executable over the Web/Network, containing:
					- remote address for downloading a Java program/location of the jar package file
					- initial main class to run
					- program parameters
				- JNLP mirrors the http/html process; in the same way that a Web browser renders a webpage, a JNLP client "renders" a Java app. After the user clicks on a weblink, the browser submits an URL to a webserver, which replies with a JNLP file (instead of a HTML file) for the application. The JNLP client parses this file, requests the resources specified (jar files), waits for the retrieval of all required resources, and then launches the application

			- Java Web Start - deprecated
				- useful for compatability
				- Unlike Java applets, Web Start applications do not run inside the browser
				- IcedTea provides an alternative JNLP implementation in IcedTea-Web

			- Swing: a GUI library for the Java SE platform
				- Webswing is a specialized web server for running Swing based Java applications in a browser
			
			- Applets: programs that were embedded in other apps, typically in a Web page displayed in a web browser, now deprecated
			
			- MIDlets: mobile tools
		    
		    - Servlet: 
		    	- a Java component that extends the capabilities of a server
		    	- can respond to many types of requests
		    	- most commonly implement web containers for hosting web apps on web servers
		    	- Java counterpart to other dynamic web content technologies such as PHP
		    	- Servlets are server-side Java EE components that generate responses to requests from clients, usually HTML pages in response to HTTP requests
		    
		    - Java Server Pages 
		    	- technologies that helps create dynamically generated web pages based on HTML, XML, SOAP, or other document types
		    	- similar to PHP and ASP, but uses the Java programming language
		    	- a compatible web server with a servlet container, such as Apache Tomcat or Jetty, is required
		    	- JSPs are server-side Java EE components that generate responses, typically HTML pages, to HTTP requests from clients
		    	- embed Java code in an HTML page by using delimiters <% and %>
		    	- a JSP is compiled to a Java servlet, a Java app in its own right, the first time it is accessed
		    		- after that, the generated servlet creates the response
		    
		    - Expression Language: 
		    	- a language used in Jakarta EE web apps for embedding/evaluating expressions in web pages
		    
		    - JSTL (Java Standard Tag Library): 
		    	- adds a tag library of JSP tags for common tasks (XML data processing, conditional execution, database access, loops & internationalization)
		    
		    - Java Server Faces: 
		    	- a Java specification for building component-based user interfaces for web apps
		    	- uses JavaServer Pages (JSP) as its templating system
		- testing
			- JUnit: Unit testing framework 
			- TestNG: JUnit-inspired test framework with extra functionality
			- Spock: Testing and specification framework for Java and Groovy apps. 
			- selenium: Portable software-testing framework for web apps. 
			- Mockito: unit testing framework (TDD or BDD)

	- code samples
		- api libraries
		- jackson, jersey, hibernate, jdbc, jswing, jax-rs
		- data type usage
		- class example
		- tests
		- input/output/stream/buffer/resource
		- networking
			- connections
				- managing connection detection/retries
			- requests
		- implement data structure in java

	- files
		- class: compiled source codoe
		- jar: package of classes/metadata/resource

	- attributes
		- interpreted
		- threaded
		- dynamic

	- typing: Static, strong, safe, nominative, manifest

		- statically typed - in the sense that method calls have their signatures type-checked at compile time, without a mechanism to defer this decision to run time (means the type cant be changed from a particular type for a variable, or hard-coded types)
			- duck typing allows for type variation with a set of types

	- compilation
		- bytecode: instructions compiled from source code into class files to be executed by the virtual machine
			- compilers for different programming languages to the Java VM translate other language code so it can be run by the java vm

