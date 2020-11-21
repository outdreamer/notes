		- data structures

			- optimal usage:
				- queue:
					- random access
					- scaling
					- access first-added elements
				- stack:
					- add/remove at end
					- access last-added elements
				- arraylist
					- add/remove at end
					- access last-added elements
					- access random items frequently ***
						- arraylist is not synchronized, increases by 50% if element added
				- arraydeque
					- likely faster than Stack when used as a stack, & faster than LinkedList when used as a queue
				- linkedlist
					- add/remove at beginning/middle
					- iterate
					- access first-added elements
				- treemap
					- efficient retrieval & storing key/value pairs in sorted order
				- queue FIFO linkedlist (fast add to beginning)
				- stack LIFO arraylist (fast add to end)
		        - tracking max & min:
		        	- heap
		        - concatenating a string:
		            - appending to array and then joining the array into a string rather than concatenating strings
		        - ordering:
		        	- heap
		        	- binary search trees
		        - accessing/sorting numbers
		        	- NOT linked list
		        	- array not great for sorting efficiently

			- tools other than java collections
				-  Trove, Colt, Fastutil, Guava

			- mutability
				- when an immutable object is changed, a new object is created
				- mutable objects may not be thread-safe

		    - immutable class should have
		    	- final class
		    	- public constructor
		    	- getter methods only
		    	- final fields (and special handling for mutable objects used as fields to prevent modification)

			- mutable data structures
				- stringbuffer, stringbuilder, java.util.data

			- immutable
				- legacy, wrapper classes
				- string

			- synchronization

				- constant-time get: 
					- arraylist
					- hashmap

				- not synchronized (cannot use them in a multi-threading environment without any external synchronization)
					- arraylist
					- hashmap

				- fail fast iterator (ConcurrentModificationException)
					- arraylist
					- hashmap

			- vector
				- V arr[];
				- Vector<int[]> // vector of int arrays

			- Enumerations, Iterators and enhanced for-loop are all external iterators (vs. foreach)

			- array: 
				- store a fixed-size sequential collection of elements of the same type
					- int[] myNumbers = {1, 2, 3};
					- String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
				- get/set with arr[index]
				- arr.length (rather than size of collections)
				- loop: for (String i : cars) {

			- deque (double-ended queue)
			    - Deque<String> d = new LinkedList<String>();

			- collections
				List<String> names = Arrays.asList("Larry", "Steve", "James");
				Queue<String> namesQueue = new ArrayDeque<>(Arrays.asList("Larry", "Steve", "James"));
				Set<String> uniqueNames = new HashSet<>(Arrays.asList("Larry", "Steve", "James"));
				- loop:
					- Any iterable of type Collection – list, set, queue etc. have the same syntax for using forEach.
						- names.forEach(name -> System.out.println(name));
						- numbers.forEach(System.out::println);

			- hashmap
				- stores each key-value pair as a bucket in an array
				- links buckets stored at same index whose keys could collide in the returned index
				- each bucket contains pointer to next bucket
				- get/put/remove/clear
				- implements map interface
				- HashMap<String, String> hashmapvar = new HashMap<String, String>();
				- loop: 
					- for (String i : hashmapvar.keySet())
					- for (String i : hashmapvar.values())
					- namesMap.forEach((key, value) -> System.out.println(key + " " + value));

			- arraylist (java.util)
				- resizable array (as opposed to built in array) using dynamic arrays
				- arraylist is not synchronized, increases by 50% if element added
				- new, larger array is created to replace the old one if its not big enough, and the old one is removed
				- implements List interface, extends AbstractList class
				- add/set/get/remove/clear/size
				- ArrayList<String> al = new ArrayList<String>();
				- ArrayList al = new ArrayList<String>();
				- ArrayList al = new ArrayList<>();
				  al.add("item");
				  Iterator it = al.iterator();
				  while (it.hasNext()) {
				  	String item = it.next(); //forward to/return next item
				  }
				- loop: for (String i : arraylistvar) {}
				- sort: Collections.sort(cars);

			- linkedlist
				- node group representing a sequence, each node having data & a pointer to next node
				- allows for efficient element insertion/removal from any position
				- uses a doubly-linked list
				- can be used as a list, stack or queue
				- implements List/Deque interfaces
				- add/remove
				- size returns length of list of lists
				- stores its items in containers, rather than an array
				- list has a link to first container, each container having a link to next list container
				- new elements are placed into a new container, which is linked to another list container
				- also provides methods:
					addFirst() 	Adds an item to the beginning of the list. 	
					addLast() 	Add an item to the end of the list 	
					removeFirst() 	Remove an item from the beginning of the list. 	
					removeLast() 	Remove an item from the end of the list 	
					getFirst() 	Get the item at the beginning of the list 	
					getLast() 	Get the item at the end of the list

			- queue (FIFO):
				- linkedlist
				- Circular Queue: 
					- last element is connected to the first element 
					- Initially, first/last point to same location, but move apart as elements inserted
				- used in
					- random access
					- scaling
				- FIFO: removes from front, adds to back
				- methods:
					- enqueue: add element to back
					- dequeue: remove element from front
					- top: returns front/first element
				- Queue<String> str_queue = new LinkedList<> ();
					- variables: front, back, sequence, max size of sequence, current size of queue

			- stack (LIFO):
				- can be implemented with arrays, vectors, & Linked List
				- used in 
					- recursion
					- searching
					- control memory allocation
					- reversing a sequence (starting with last item first)
				- best with array (less memory) or arraylist (removal from end)
				- methods
					- push: add element to end
					- top: return element recently added
					- pop: returns last element added after removing it

				- Stack<Integer> myStack = new Stack<>();
					- variables: sequence, top item, and size

						public class Queue<V> {
						    private int maxSize;
						    private V[] array; //Java does not allow generic type arrays, so use array of Object type & type-cast it to generic type V
						    private int front;
						    private int back;
						    private int currentSize;

						    @SuppressWarnings("unchecked")
						    public Queue(int maxSize) {
						        this.maxSize = maxSize; // fixedArraySize
						        array = (V[]) new Object[maxSize]; //V[] array = (V[]) new Object[maxSize];
						        front = 0;
						        back = -1;
						        currentSize = 0;
						    }

						    public int getMaxSize() { return maxSize; }
						    public int getCurrentSize() { return currentSize; }
						    public boolean isEmpty() { return currentSize == 0; }
						    public boolean isFull() { return currentSize == maxSize; }
						    public V top() { return array[front]; }

						    public void enqueue(V value) {
						        if (isFull()) return;
						        back = (back + 1) % maxSize; //to keep the index in range
						        array[back] = value;
						        currentSize++;
						    }

						    public V dequeue() {
						        if (isEmpty()) return null;
						        V temp = array[front];
						        front = (front + 1) % maxSize; //to keep the index in range
						        currentSize--;
						        return temp;
						    }
						}

			- treemap
				- implements Map interface
				- efficient storing key/value pairs in sorted order
				- efficient retrieval
				- unlike a HashMap, TreeMap guarantees elements sort in ascending key order
			- hashset/linkedhashset
			- treeset
			- arraydeque
				- Resizable-array implementation of Deque interface
				- no capacity restrictions, growing as necessary 
				- not thread-safe; without external synchronization, dont support concurrent access by multiple threads
				- Null elements are prohibited
				- likely faster than Stack when used as a stack, & faster than LinkedList when used as a queue
			- Iterator: used to loop through collections, like ArrayList and HashSet

		    - structures: collections, deque/queue, array, stack, queue, singly linked list, doubly linked list, skip list, hash table, binary search trees, cartesian tree, b tree, red-black tree, splay tree, avl tree, kd tree, heap

		    - array: list of key-value pairs
		        - A typical implementation of a dynamically resizable array (ArrayList) provides o(1) insertion time/access
		        - When the array is full, the array doubles in size - each doubling takes o(n) time, but doubling happens so rarely that the amortized insertion time is still o(1).
		        - inserting n elements takes o(n) work; each insertion is o(1) on average even tho some insertions take o(n) in the worst case when a list is full
		    - stack
		        - can be implemented with a linked list IFFF the items are added & removed from the SAME side
		        - uses pop() to remove an item from end, push(item) to add an item to the end, peek() to return the last item, isEmpty() to check if the stack is empty
		        - cant be used to give constant time access to an item, but does offer constant time adds/removes bc these dont require shifting items around
		        - useful in recursive algorithms when you want to push temporary data on to a stack as you recurse & remove them as you backtrack when the recursive check failed
		        - can also be used to implement a recursive algorithm iteratively
		    - queue
		        - queues can also be implemented with a linked list (queue and linked list are basically the same, if items are added & removed from OPPOSITE sides)
		        - queues are often used in breadth-first search (to store a list of nodes we need to process, adding their adjacent node to the back of the queue as each node is processed to process them in the order that they're viewed in) and in caches
		    - linked list: represents a sequence of nodes
		        - unlike arrays, linked lists do not provide constant time access to an index in the list, but o(k) where k is the number of elements
		        - singly linked list: each node points to the next node in the linked list
		        - doubly linked list: each node has pointers to both the next node and the previous node
		    - hash table: maps keys to values for efficient lookup
		        - common implementation uses an array of linked lists and a hash code function
		        	1. compute key's hash code, usually an integer - multiple keys might have the same hash code
		        	2. map the hash code to an index in the array - hash(key) % array_length
		        	3. at each index is a linked list of keys and values; store the key and value in this index
		        - to retrieve the value pair by its key, you repeat this process: 
		        	1. compute the hash code from the key
		        	2. compute the index from the hash code
		        	3. then search through the linked list for the value with this key
		        - used to find things quickly in an unsorted array (without iterating through each item brute-force)
