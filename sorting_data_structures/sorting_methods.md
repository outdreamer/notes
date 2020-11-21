complexity:

    - recursive algorithms take at least o(n) space, where n is the depth of the call
    - recursive algorithms CAN be implemented iteratively but they may be much more complex that way


computational complexity goes with the following types of operations
    constant o(1) time: no matter how big the input is, the code will always take the same amount of time
        o(1) time:
        - look up values in array
        - sum values
        - store values
        - return
        - o(log n) is almost as good as o(1)

        o (log n) time:
        - Adding an item to a binary search tree

        o(n) time: the time will always increase at a constant rate (linearly) with the size of the input

        o(n) time:
        - look up item in hash table
        - find elements with a particular property

        o(a + b) time:
        - two inputs running two sets of iterations

        o(a * b) time:
        - two inputs running embedded sets of iterations

        o(n log n) time:
        - sort an array
        - Adding n items to a binary search tree

        o(n^2) time: the time will always increase at a rate of n with the size of the input n (exponential rate of increase)
                    for every item in n, we have to do n more operations, n * n
        o(n!) time:
        - generate all possible permutations of the letters in a string of length n


sorting algorithms:

    Attributes:
        Adaptive: A sorting algorithm falls into the adaptive sort family if it takes advantage of existing order in its input. It benefits from the presortedness in the input sequence
            Straight insertion sort, adaptive heap & merge sort, Shellsort, splaysort and Timsort

        Stable: stable algorithms preserve the relative order of equivalent elements from the input list in the output list

        In-Place: an algorithm that transforms input using no auxiliary data structure, except for extra storage space for auxiliary variables
            uses a constant amount of extra space

    quicksort: array, comparison sort
        - average takes o(n log n), but worst case is o(n^2)
        A. divides array into smaller arrays based on a pivot element:
            1. pick pivot element
            2. reorder array so all elements lower than the pivot come before and all higher than pivot come after
        B. recursively applies operation A to each resulting sub-array

    mergesort: array, comparison sort
        - both average & worst case is o(n log n)
        A. divide array into n sub-arrays of length 1
        B. compare & merge sub-arrays into sorted lists until one complete list is remaining

    timsort: array, derived from mergesort & selection sort
        - average & worst case is o(n log n)
        A. find sub-sequences that are already ordered
        B. merge sub-sequences recursively until none left or criteria are fulfilled

    heapsort: array, improved selection sort
        - always o(n log n)
        - uses heap data structure instead of linear-time search to find the maximum, which is why it's better than selection sort
        A. divides list into an unsorted heap (containing all the data at first) and a sorted array
        B. recursively selects largest element (maximum) in unsorted heap and adds to top of sorted array

    bubble sort: array, comparison sort by exchange
        - quadratic: both average & worst case is o(n^2)
        - good for when the input data is usually sorted but occasionally is out of order, bc it can confirm a list is sorted efficiently in o(n) time, but is still less efficient than insertion sort at determining if a list is sorted efficiently
        A. recursively compares each pair of adjacent items
        B. if each pair is in the wrong order, bubble sort swaps them

    insertion sort: array, in-place comparison sort by insertion
        - quadratic: both worst & average case is o(n^2) comparisons/swaps
        - good only for small data sets. adaptive, meaning has complexity o(nk) when each element is only k spaces away from sorted position, so works best on lists that are already semi-sorted. stable, meaning it doesn't change the correct order of elements with the same key. in-place, meaning it only requires o(1) of extra space, and online, meaning it can sort a list as data is received.
        A. iterates through existing array
        B. at each iteration, finds correct position of current element in output array by comparing to values in sorted array, starting with largest value, and moves it from input to output array
    
    selection sort: array, in-place comparison sort
        - quadratic: both worst & average is o(n^2)
        - good only for small data sets, usually less efficient than insertion, but has o(1) auxilary (external) space complexity 
        A. divides list into already sorted array and unsorted array
        B. iterates through unsorted array
            for each iteration, finds smallest or largest element in unsorted array, swaps it with leftmost unsorted element & moves sublist boundary one element to the right to move the smallest or largest element in the unsorted array to its correct position in the sorted array

    tree sort: array, comparison sort, 
        - worst case o(n^2) unbalanced, o(n log n) balanced and average o(n log n)
        Adding an item to an unbalanced binary tree requires O(n) time in the worst-case - when the tree resembles a linked list (degenerate tree). This results in a worst case of O(n²) time, which occurs with an already or nearly sorted set. Expected O(n log n) time is achieved by shuffling the array. Worst case performance is improved using a self-balancing BS tree to o(n log n), but takes a performance hit if stored in the heap. But if you use a splay tree as the BST, resulting in a splay sort algorithm, it becomes an adaptive sort, meaning its runtime is faster than o(n log n) for inputs that are already nearly sorted.
        A. builds binary search tree from unsorted elements

    shell sort: array, in-place comparison sort by insertion/exchange
        - unstable & adaptive
        - o(n^2) with worst gap sequence, o(n log n) with best gap sequence
        - example: sort in five groups, then sort in 3 groups, then sort in groups of 1 (ordinary insertion sort of the whole array)
        A. identifies pairs or groups of elements that are far apart from each other, sorting the pair or group
        B. iterates through subsequence pairs with smaller gaps until none left

    bucket sort: array, distribution sort, related to radix sort
        - worst case o(n^2), average o(n+k) where k is number of buckets
        A. divides list into buckets
        B. sorts buckets individually, either with bucket sort or another sorting algorithm
        C. iterate over sorted buckets, fitting them into original array

    radix sort: array, non-comparative sort, used to sort data with integer keys by grouping keys according to digits with same significant position & value. LSD (least significant digit) radix sorts process the integer representations starting from least toward most significant digit, where short keys come before long keys, and keys of same length are sorted lexicographically.
        - can handle sorting larger keys better than counting sort
        - worst case o(wn) for n integer keys of word size w
        - used to sort data stored in sequences of bits
        - computers represent their data as electronic representations of binary numbers, so they process digits of integer representations by groups of binary digit representations

    counting sort: integer sorting algorithm (NOT a comparison sort), used for sorting objects by keys that are small integers
        - stable, no recursion, only for loops
        - good only when key variation is not much greater than the number of items, often used as subroutine in radix sort
        - o(n) linear runtime
        - bucket sort is a good alternative to counting sort in several use cases with similar runtime, but bucket requires linked lists, dynamic arrays or more memory than counting sort, whereas counting sort only stores a single item per bucket.
        A. counts number of objects with distinct key value, creating histogram of different keys
        B. iterates through each possible key to determine starting position of each item having that key in the final output array
        C. loops over items again to move them to proper position in output array

            # calculate the histogram of key frequencies:
            for x in input:
                count[key(x)] += 1
            # calculate the starting index for each key:
            total = 0
            for i in range(k):   # i = 0, 1, ... k-1
                oldCount = count[i]
                count[i] = total
                total += oldCount
            # copy to output array, preserving order of inputs with equal keys:
            for x in input:
                output[count[key(x)]] = x
                count[key(x)] += 1
            return output



Terms:
- interface: set of operations, type of input parameters, and type of outputs supported by a data structure object 
- implementation: explicit representation of a data structure object 
- time complexity: runtime or execution time of a set of operations 
    - time(program) = time that a constant step takes * number of constant steps
    - worst case: maximum time an operation can take. if the worst case time is f(n), the operation will not take more time than f(n)
    - average case: average time an operation usually takes. m operations will take m * f(n) time, if f(n) represents average execution time
    - best case: minimum time an operation can take. if the best case time is f(n), the operation will not take less time than f(n)
- space complexity: maximum extra space required by a set of operations
    - space(program) = c (number of constants * space required by constants) + s(i) (number of vars * space required by vars)
    - space complexity = fixed space + variable space
    - fixed space: space required independent of program size
    - variable space: space required dependent on size of program (example: recursion stack space, dynamic memory allocation)
- performance considerations: data size, processor speed, and concurrent thread count
- common operations: search, sort, insert, update, delete, traverse, merge
- algorithms must: 
    - >= 0 inputs & >= 1 expected outputs
    - finite & feasible
    - independent (of possible code implementations of the algorithm)
    - unambiguous (leading to only one interpretation)
- a priori analysis: assumes all other factors like processor speed are constant & have no impact on performance of the code 
- a posterior analysis: an algorithm is implemented & executed, and its run time & space requirements are measured
- asymptotic analysis: finding the best, average, & worst case complexity of an algorithm, based on inputs
    - if there are no inputs, the algorithm is assumed to run in constant time
    - o(n) notation is the max/worst/upper bound of the run time: 
        o(f(n)) = g(n) where f(n) <= c * g(n) for c > 0, for all n > n0
    - theta notation expresses the average of the upper & lower bound of the run time: 
        theta(f(n)) = g(n), where g(n) = o(f(n)) and g(n) = omega(f(n)) for all n > n0
    - omega(n) is the min/best/lower bound of the run time: 
        o(f(n)) = g(n) where g(n) <= c * f(n) for c > 0, for all n > n0
- notations:
    constant: o(1)
    logarithmic: o(log n)
    linear: o(n)
    n log n: o(n log n)
    quadratic: o(n^2)
    cubic: o(n^3)
    polynomial: n^(o(1))
    exponential: 2^(0(n))
- greedy algorithms: the closest solution providing an optimal solution is chosen (local max/min) rather than always providing globally optimal solutions
    examples: knapsack, job scheduling, and traveling salesman problems; prims MST, kruskal MST, dijkstra MST; color a map graph or covering a vertex graph
- divide & conquer: the problem is split into sub-problems once the smallest atomic unit of problem is achieved, which are solved independently, then merged
    examples: merge sort, quick sort, binary search, strassen matrix multiplication, closest pair of points
- dynamic programming: similar to divide & conquer except rather than solving independently, the solution of a sub-problem is remembered & reused to solve others
    - dynamic programming can be used in either direction & uses memoization to remember the output of solved sub-problems
    - examples: fibonacci, knapsack, tower of hanoi, floyd warshall & dijkstra pair shortest path, project scheduling
- memoization: where the output of expensive function calls is cached & re-used when the same inputs are received in that function



- expressions:
    - infix notation (a + b): 
        (a + b) ∗ (c + d) (costly in time & space)
    - prefix/polish notation (+ab): 
        ∗ + a b + c d
    - postfix/reversed polish notation (ab+): 
        a b + c d + ∗
        example algorithm to implement postfix using a stack:
        Step 1 − scan expression from left to right 
        Step 2 − if it is an operand, push it to the stack 
        Step 3 − if it is an operator, pull the operand from the stack and execute the operation 
        Step 4 − push the output of step 3 execution in the stack 
        Step 5 − scan the expression until all operands are consumed 
        Step 6 − pop the stack and perform operation
- order of operations: exponents are handled first, then multiplication/division, then substraction/addition, unless parenthesis interfere 


Data Structures
    - atomic: defining a single concept
    - traceable: mapped to some data element 
    - accurate: unambiguous
    - understandable: clear & concise
    - built-in data types: languages usually come with these accessible
        examples: integers, booleans, floats (decimals), strings
    - derived data types: built with built-in data types
        examples: list, array, stack, queue
    - array supports:
        - traverse, insert, delete, search, update 
    - linked list: a list of data structures, connected by links in a direction
        has:
        - a first (head) element
        - each link has a data field & a next link field
        - each link is connected with the next link by its next link field
        - the last link has a null link field to signal the end of the list 
        - operation behavior is dependent on position & changes if the last or first node
        - singly linked list:
            - supports: insert first, insert at key, delete first, delete at key, display list, search at key, reverse list
            - insert: evaluates position, changes the previous item to point to the inserted item, & changes the inserted item next link to the previous next item
            - delete: evaluates position, changes previous items next link to point to deleted item next link
        - double linked list:
            - supports: insert first, insert last, insert after key, delete first, delete last, delete at key, display forward, display backward
        - circular double linked list:
            - supports: insert first, delete first, display list
        types:
        - simple linked list: navigation is forward only
        - double linked list: navigation is forward & backward
        - circular linked list: last item next link is assigned to the 1st element, first item previous link is assigned to the last element
    - stack: 
        - can be fixed or dynamic sized
        - supports: operations at the top only (LIFO), like placing a plate on the top of a stack of plates, so the last element placed is accessed first
            - initialize stack
            - push function to store an element on the top of the stack 
            - pop function to access & remove an element off the top of the stack 
            - peek function to see the value of the top element without removing it
            - isEmpty function to check if the stack is empty
            - isFull function to check if the stack is full
            - pointer variable to track the top value of the stack at all times
            - destroy stack function
            - push & pop should check to see if the stack is full/empty respectively before proceeding
        - arrays may just change the pointer value & not actually remove elements with pop
            while linked list removes the element (deallocating memory) & changes the pointer value
        - if a linked list is used, push needs to allocate space before adding an element
        - implemented with: array, structure, pointer, linked list
    - queue: 
        - supports: operations at both ends, unlike stacks
        - the back end is always used to insert data; the front end is used to delete data (FIFO), where the item inserted first will be accessed first 
        - examples: line of cars
        - implemented with: array, structure, pointer, linked list 
        - operations: 
            - initialize queue
            - push function to store an element on the back of the queue 
            - pop function to access & remove an element off the front of the queue 
            - peek function to see the value of the front element without removing it
            - isEmpty function to check if the queue is empty
            - isFull function to check if the queue is full
            - removePointer variable to track the front value of the queue, addPointer to track the back value of the queue
            - destroy queue function
            - push & pop should check to see if the queue is full/empty respectively before proceeding

Search:
    - linear search: o(n)
        - where traversal travels the whole list, one by one, stopping only if a match is found
    - binary search: o (log n)
        - more efficient than linear search
        - uses divide & conquer
        - requires data to be sorted
        - examines middle item first, returning the index if a match is found 
        - if the middle item is greater than the item being searched for, then the search starts again in the lower half, lower than the middle.
        - otherwise, the search starts again in the upper half, greater than the middle.
        - this split & search process continues until the size of the split sub-array is 0
    - interpolation search: o(log (log n))
        - an improved version of binary search 
        - determines the sorted sub-set to search, then searches only that sub-set
        - data must be sorted and equally distributed so it can be split into sorted sub-sets
        - example: in a phone book, you can search for name "mary" starting with the M sub-set
        - search position starts at middle, but then you compute the search position of expected sub-set
        - to split the list into two parts, use:
          mid = L + ((H - L) / (A[H] - A[L])) * (X - A[L]) 
        - if the sought item is greater than the middle item, the search position is re-calculated in the higher sub-set to the right
        - this re-calculation continues until the size of the sub-set is 0
    - hash table: 
        - stores data in an associated way, with a key & value pair, where keys are unique, and data is stored in an array
        - insertion & search are very fast with a hash table *******
        - supports: search, insert, delete
        - has a hash function that generates a unique index for each input value
        - if the hash function generates a index that is not unique, it increments the value of the index & checks that (incrementing is linear position probing)
        - for search, first execute the hash function on the index value to find out which index to search
        - then retrieve the array value at that index
        - hash tables are somewhat similar to interpolation in that they first determine the likely position of data, 
            though interpolation uses a splitting method similar to binary search, 
            & hash tables use a formula to derive the correct position immediately
        - for delete, keep a dummy item in the delete location to retain the performance of the table
        - for any hash table operation, use linear probing to determine the next likely position if the desired item is not found at the initial position 


Sorting:
    - in place sorting: sorting that does not require extra space, as in swaps made in bubble sort
    - not in place sorting: sorting that does require equal or more extra space, as in merge sort
    - stable sorting: a sort that doesnt change the order of relative elements:
        (A1, C, A2, B) retains the relative position of A1 and A2 bc A1 still comes before A2 in the output list: (A1, A2, B, C)
    - unstable sorting: a sort that changes the order of relative elements:
        (A1, C, A2, B) retains the relative position of A1 and A2 bc A1 doesnt comes before A2 in the output list anymore: (A2, A1, B, C)
    - stability matters if sequence matters, like in a tuple
    - adaptive algorithms: dont try to sort already sorted sub-sequences found in the list, but instead skip already sorted sub-sequences
    - increasing order: successive elements are greater
    - decreasing order: successive elements are less
    - non-increasing order: successive elements are less than or equal to
    - non-decreasing order: successive elements are greater than or equal to
    
    - bubble sort O(n^2): 
        - in-place comparison algorithm
        - starts with the first two items
        - adjacent items are compared & swapped if not in desired order until none are left, 
        - then it repeats until the array is completely sorted
        - uses a flag variable to indicate whether a swap occurred in the current iteration - if no swaps occurred, another iteration isnt required
        - you can avoid already sorted items at the end of the list if desired, to speed it up a little
    - insertion sort o(n^2):
        - in-place comparison algorithm
        - maintains a sorted sub-list, such as the lower part of the array
        - only one item is added to the sorted sub-list at a time
        - every time an item is added to the sorted sub-list, the whole sub-list is checked for correct order, and if any swaps necessary, those are executed
        - the correct place of each element in the sorted sub-list must be found & inserted there
        - starts with the first two items
        - the first item is already sorted, to skip any sorting logic & return 
        - the second & all subsequent items must be compared with the sorted sub-list, and inserted at the position where a value is found that is greater,
            shifting all the greater elements by one to the right to make room for the inserted element
        - then proceed to the next item, until the list is sorted (the size of the sorted sub-list equals the size of the original list)
    - selection sort o(n^2):
        - in-place comparison algorithm
        - the list is divided into two parts, the sorted section on the left and the unsorted section on the right
        - the sorted part starts out empty, the unsorted part starts out as the whole list
        - iterating through the unsorted array, the smallest position is stored for future reference
        - the stored smallest element is swapped with the leftmost element, and the new leftmost element is added to the sorted array
        - then the search proceeds in a linear manner, finding the smallest element in the unsorted array again, 
            and swapping it with the item in the position of (size of sorted array + 1)
        - this process is repeated, moving the unsorted array boundary by one unit to the right each time
    - merge sort o(n log n):
        - *** one of the best basic sorts
        - divide & conquer algorithm
        - splits the array into sub-sets until no more splitting is possible
        - begins re-merging each sub-set, sorting each sub-set after each merge, until the whole set is merged to the original array length
    - shell sort o(n):
        - *** highly efficient
        - based on insertion sort
        - uses insertion sort on items separated by a wide interval rather than adjacent items separated by an interval of size 0
        - example: instead of comparing items 1 and 2, it uses an interval like 4 and compare items 1 and 5, 2 and 6, 3 and 7, 4 and 8
        - then it sorts the items in those pairs 
        - then it chooses a slightly smaller interval (interval - 1)/3, like 1 & does the comparison iteration again, comparing items 1 & 2, 3 & 4, 5 & 6, etc
        - then it iterates the whole list, comparing adjacent items
    - quick sort o(n^2):
        - ***efficient
        - based on splitting into sub-arrays using a pivot value
        1. the pivot value is initially the highest value
        2. use two variables to store the low and high index, excluding the pivot 
        3. iterate through the list, comparing the low & high values - if the lower value has a higher index, swap them 
        4. after swapping, if the low index value is lower than the pivot, move right, otherwise if the high index value is higher than the pivot, move left
        6. if left >= right, the point where they met is the new pivot value
        7. if no values are left except the pivot, use the pivot to compare & swap, if the value is greater than the pivot
        8. if the pivot is used to swap, then the array is now partitioned, and quicksort must be done again recursively on the left & right sub-arrays

Graph:
    - a data structure where pairs of nodes/vertices are connected by lines/edges
    - a graph is defined as two lists: a one-dimensional array of the unique nodes, and a two-dimensional array of the unique lines (or node-pairs)
    - the start & end nodes can be represented by a two-dimensional list or tuple, like (0, 1) for nodes in positions 0 (root) and 1 (left child of root)
    - supports: add node, add line, display node 

    Depth First Search: (DS)
        - traverses depth first; it explores adjacent nodes on the next layer down (multiple unit-paths) rather than covering all adjacent nodes of a parent node
        - uses a stack to store & retrieve the next node to search on hitting a dead end in any iteration
        1. visit adjacent unvisited node & mark it as visited, push it on the stack
        2. if no adjacent nodes found for a particular node, pop that particular node off the stack 
            & go to the next item in the stack & check if that node has any unvisited nodes
        3. if multiple adjacent nodes found, use the specified order to choose which one to visit next (alphabetical, ascending)
        4. if a dead end is reached (a node has no unvisited adjacent nodes), then pop nodes off the stack until empty, checking for unvisited nodes

    Breadth First Search: (BQ)
        - traverses breadth first; it explores all adjacent nodes of a parent node in the next layer before progressing to another layer (one-unit paths)
        - uses a queue to store & retrieve the next node to search on hitting a dead end in any iteration
        1. visit adjacent unvisited node & mark it as visited, push it on the queue
        2. if no adjacent nodes found for a particular node, pop the first node off the queue 
            & go to the first item in the queue & check if that node has any unvisited nodes
        3. if multiple adjacent nodes found, use the specified order to choose which one to visit next (alphabetical, ascending)
        4. if a dead end is reached (a node has no unvisited adjacent nodes), then pop nodes off the queue until empty, checking for unvisited nodes

    - breadth-first search (layer search)
        - queue (fifo)
        - checks whether a vertex has been discovered before enqueueing the vertex
        - good for shortest path analysis & analyzing node relationships

    - depth-first search (path search)
        - stack (lifo)
        - delays checking whether a vertex has been discovered until the vertex is popped from the stack


Tree: 
    - a data structure similar to a graph but where each node can only have two children 
    - root: first node of a search tree
    - visit: check the value of the current node
    - leaf: final node with no child nodes in a binary search tree
    - tree level: a generation of nodes (layer)
    - supports: insert, search, pre order traverse, in order traverse, post order traverse
    - traversing: passing through nodes in a specific order
    - in-order traversal: left-root-right
        recursively traverse left subtree, then root, then recursively traverse right subtree
    - pre-order traversal:  root-left-right
        root, then recursively traverse left subtree, then recursively traverse right subtree
    - post-order traversal: left-right-root
        recursively traverse left subtree, then recursively traverse right subtree, then root

    - *** if a binary tree is traversed in order, the output will be a list of ascending sorted values

    Search tree:
        - each tree can be traversed by:
            - in-order traversal (left, root, right),
            - pre-order traversal (root, left, right)
            - post-order traversal (left, right, root) 
        - each tree has search & insert operations
        - search operations should start by comparing values to root node: 
            if less than root, use the left subtree, if more than root, use the right subtree
        - insert operations need to determine the correct location for insertion

    Binary tree: 
        - each node can have a max of two child nodes
        - the left child value must be less than parent value
        - the right child value must be greater than parent value
        - left subtree values <= node values <= right subtree values
        - each node has a key & associated value
        - has the benefits of a sorted array search & a linked list insert/delete:
            - binary tree search speed = sorted array search speed
            - binary tree insert/delete speed = linked list insert/delete speed
        - BST worst case is close to linear search, o(n)

    AVL tree:
        - a height-balancing type of binary search tree
        - sorted with one possible offshoot layer, and one main line non-increasing or non-decreasing vertically
        - the balance factor: height of the left subtree - height of the right subtree
        - AVL checks that the balance factor isnt more than 1
        - if the balance factor is more than 1, the tree can be balanced using rotation techniques
        - rotation techniques:
            single rotations:
            - left rotation: a line of 3 nodes starting highest on the left is bent so the original highest node is on the same layer as the lowest node
            - right rotation: a line of 3 nodes starting highest on the right is bent so the original highest node is on the same layer as the lowest node
            double rotations: 
            - left-right rotation: a bent 3-node line w/ an unbalanced node only on the right of 2nd node; the bottom 2 are swapped, & a left rotation on the top node
            - right-left rotation: a bent 3-node line w/ an unbalanced node only on the left of 2nd node; the bottom 2 are swapped, & a right rotation on the top node
        - the minimum height of an unbalanced tree is 2 
        - counting height starts at 0 so a tree like the following has height 2 even though it has 3 layers:
                  c
               b /
            a /
        - after a left rotation, the above would be:
            'b'
        'a /   \ c'

    Spanning tree:
        - used to find a minimal path to connect all nodes in a graph
        - a subset of an undirected graph that covers all its vertices (nodes) with the minimum number of steps
        - example: a spanning tree of a triangular graph of 3 nodes would be a v shape connecting all 3 nodes
        - a complete connected undirected graph can have n ^ (n-2) number of spanning trees, where n is the number of nodes 
        - with 3 nodes, 3 ^ 1 = 3 spanning trees are possible
        - a complete connected undirected graph can have more than one spanning tree 
        - all possible spanning trees of a graph have the same number of lines & nodes
        - spanning trees dont have any cycles/loops 
        - removing a line from the spanning tree makes the graph disconnected, so the spanning tree is minimally connected (smallest possible number of connections)
        - adding a line to the spanning tree makes a cycle or loop, so the spanning tree is maximally acyclic (all possible cycles are avoided)
        - spanning trees have n-1 lines
        - by removing (e - n + 1) lines from a connected graph, you can make a spanning tree 
        - spanning trees are a subset of the connected graph & disconnected graphs do not have spanning trees

    Minimum Spanning Tree:
        - in a weighted graph, a min spanning tree has minimum weight than all the other spanning trees for that graph
        - weight of a line can represent variables like distance or traffic amount

        - Kruskal Minimum Spanning Tree Algorithm:
            - uses greedy approach, treating the graph as a forest and every node as an individual tree
            - a tree connects to another if it has the least cost among all available options & obeys MST properties 
            1. remove all loops & parallel lines from graph
            2. with parallel lines, remove the one with the least cost & remove all others 
            3. arrange lines (referenced by (a,b) pairs) by increasing weight 
            4. add the line with the least weight
            5. iterate through increasing weights, checking if adding them violates MST properties
            6. if adding a weight & associated line creates a loop, skip it

        - Prims Minimum Spanning Tree Algorithm:
            - uses greedy approach & shortest path first
            - treats the nodes as a single tree & adds nodes to this spanning tree from the given graph
            1. remove all loops & parallel lines from graph
            2. with parallel lines, remove the one with the least cost & remove all others 
            3. choose any node as the root node
            4. check outgoing lines & select the one with the least cost and include it in the tree
            5. repeat the previous step 
            6. if the two line options have equal weights, both can be selected 

    Heap: 
        - a special case of the balanced binary tree where the root is compared with its children & the position adjusted accordingly
        - the parent value should be greater than the child value
        - the parent being greater than the child indicates a Max Heap
        - Min Heap: value of the root node is less than or equal to its children
        - Max Heap: value of the root node is greater than or equal to its children
            To create a max heap:
            1. create a node at the end of the heap
            2. assign a value to the node 
            3. compare the value of this node to its parent if it exists
            4. if value of parent is less than child, swap them (parent should be greater than child)
            5. repeat steps 3 & 4 until the heap is complete, while max heap properties hold

            To delete a max heap:
            1. Remove root
            2. Move the last element of the last level to root
            3. Compare the value of this child node to its parent
            4. If the value of the parent is less than the child, swap them
            5. Repeat steps 3 & 4 until the max heap is deleted, while map heap properties hold

Recursion:
    - To avoid infinite recursion, a function must:
        1. have at least one base criteria, which when met stops the calling of the function
        2. have calls that progress in a way that each time the recursive function is called, it makes progress toward the base criteria
    - Many languages implement recursion through stacks, where the initial call goes at the bottom of the stack & subsequent calls on top of the previous call
    - this stack (of activation records) tracks:
        - all data passed between function calls as local variables or function parameters
        - the return address
        - the info passed to the caller (triggering) function
    - advantages to recursion as opposed to iteration are readability & efficiency
    - time complexity is assessed by number of times an iteration or recursive function is called
        - every function call is o(1), so with n = the number of times a call is made, the complexity of a recursive function is o(n)
        - time complexity of recursive functions is similar to iteration, disregarding other factors
    - space complexity, the amount of extra space required for execution, is assessed by what needs to be stored
        - iterations can replace variables values, but recursions require tracking each version of a variable value
        - space complexity of recursive functions is higher than iteration

    Tower of Hanoi:
        - three stacks have rings that are in decreasing size; the goal is to move all the rings from one stack to another without violating the decreasing constraint
        - only one ring can be moved at a time
        - only the top ring can be removed 
        - a larger ring cannot be on top of a smaller ring
        - a puzzle with n rings can be solved with (2^n) - 1 steps
        - an algorithm should use source, destination, and temp variables to store each stack
        - the goal is to move the largest ring (nth ring) to another location and put all the others (n-1 ... 1 rings) on top of it
        1. move n-1 disks from source to temp
        2. move nth disk from source to destination 
        3. move n-1 disks from temp to destination

    Fibonacci Series:
        - f(n) = f(n-1) + f(n-2)
        - the first value of the series can be 0 or 1
