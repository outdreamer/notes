
## python sorting 

    - implementations

    - traversals

    - divide & conquer

    - breadth-first search (layer search)
        - queue (fifo)
        - checks whether a vertex has been discovered before enqueueing the vertex
        - good for shortest path analysis & analyzing node relationships

        listvar = deque([starting_node])
        def breadth_first_search(sequence):
            node = sequence.popleft()
            for m in node:
                if m == target_val:
                    return m
            listvar.append(node)

    - depth-first search (path search)
        - stack (lifo)
        - delays checking whether a vertex has been discovered until the vertex is popped from the stack
 
    - bubble (swapping)
        - making multiple passes through a list by comparing adjacent items and swapping them, sorting in ascending order 
        - in each step, the largest elements will be bubbled at the end of the list.

    - selection (comparison, from minimum)
        - start by taking the minimum value in the given list and we compare with each element, sorting in ascending order
    
    - insertion (comparison, adjacent)
        -  compare the first two elements and then we sort them by comparing and again we take the third element and find its position among the previous two and sort in ascending order
      
    - merge (divide & conquer)
        - divides the array by half, sort each half recursively, and then combines them in a sorted way

    - quick (divide & conquer)
        - split into subarrays, choose pivot element, start comparing pivot to first element, position smaller than pivot to left, position greater than pivot to right

    def sort(numbers):
         # require at least two items for comparison & splitting
        if len(numbers) <= 1:
            return numbers

        - bubble (swapping)
            for i in range(len(numbers)-1,0,-1);    # for i in range(len - 1, 0, -1): # reverse list index
                for j in range(i):                    # for j in range(i) # decreasing range from original list length
                    if numbers[j] > numbers[j+1]:       # if current_j_value > next_j_value:
                       temp = numbers[j]                    # temp = current_j_value
                       numbers[j] = numbers[j+1]            # numbers[j] = next_j_value
                       numbers[j+1] = temp                  # numbers[j + 1] = current_j_value

        - selection (comparison, from minimum)
            for i in range(len(numbers) - 1):       # for i in range(0, len - 1):
                min_pos = i                           # current_min_index = i
                for j in range(i,len(numbers)):       # for j in range(0, len):    
                    if numbers[j] < numbers[min_pos]:   # if current_j_value < current_min_value:
                       min_pos = j                          # new_minimum_index = list.index(current_min_index)
                temp = numbers[i]                     # temp = current_i_value
                numbers[i] = numbers[min_pos]         # numbers[i] = new_minimum_value
                numbers[min_pos] = temp               # numbers[new_minimum_index] = current_i_value

        - insertion (comparison, adjacent)
            for i in range(1, len(numbers)):              # for decreasing_original_length in range(1, len):
                j = i-1                                     
                next_e = numbers[i]                         # temp = numbers[decreasing_original_length]            # last value in decreasing original list
                while (numbers[j] > next_e) and (j >= 0):   # for j in range(decreasing_original_length - 1, 0, -1):    # reverse sub list
                                                              # if numbers[j] > temp:                                       # if current value in sub list is greater than last value of sub list
                    numbers[j+1] = numbers[j]                   # numbers[j + 1] = numbers[j]                                   # set next value to current value
                    j = j-1                                     # new_index = j - 1                                             # increase iterator of sub list
                    numbers[j+1] = next_e                       # numbers[j] = temp                                             # set current value to last value of sub list

        - quick (divide & conquer)
            pivot = numbers[0]                      # pivot = original_first_value
            i = 0                                   # iterator is zero
            for j in range(len(numbers)-1):         # for j in range(len - 1)
                if numbers[j+1] < pivot:            #    if next_value < original_first_value
                   numbers[j+1] = numbers[i+1]      #        next_value = value_after_pivot
                   numbers[i+1] = numbers[j+1]      #        value_after_pivot = next_value
                   i += 1                           #        increment iterator
            numbers[0] = numbers[i]                 #  swap original_first_value and original_value at final_iterator_index
            numbers[i] = numbers[0]
            first_part = quick_sort(numbers[:i])     # sorted_lower_part = apply algorithm to list below final_iterator_index
            second_part = quick_sort(numbers[i+1:])  # sorted_upper_part = apply algorithm to list after final_iterator_index
            first_part.append(numbers[i])            # append original_value at final_iterator_index to sorted_lower_part
            return first_part + second_part          # append sorted_upper_part & return


        - merge (divide & conquer)

            def merge_sort(numbers):
                middle = len(numbers) // 2
                l_list = merge_sort(numbers[:middle])
                r_list = merge_sort(numbers[middle:])
                return list(merge(l_list, r_list))

            def merge(l_half,r_half):
                s = []
                while len(l_half) != 0 and len(r_half) != 0:
                    half_to_remove = l_half if l_half[0] < r_half[0] else r_half
                    s.append(half_to_remove[0])
                    half_to_remove.remove(half_to_remove[0])
                return s + r_half if len(l_half) == 0 else s + l_half

        - from sorting_techniques import pysort
            s_obj = pysort.Sorting()
            l_sort = s_obj.bubbleSort(my_list) # insertion, selection, merge

        - bubble (swapping)
            - making multiple passes through a list by comparing adjacent items and swapping them, sorting in ascending order 
            - in each step, the largest elements will be bubbled at the end of the list.

        - selection (comparison, from minimum)
            - start by taking the minimum value in the given list and we compare with each element, sorting in ascending order
        
        - insertion (comparison, adjacent)
            -  compare the first two elements and then we sort them by comparing and again we take the third element and find its position among the previous two and sort in ascending order
          
        - merge (divide & conquer)
            - divides the array by half, sort each half recursively, and then combines them in a sorted way

        - quick (divide & conquer)
            - split into subarrays, choose pivot element, start comparing pivot to first element, position smaller than pivot to left, position greater than pivot to right

        - heap:
            - priority queue
            - heap is a specialized tree-based data structure which is an almost complete tree that satisfies the heap property
                - in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C
                - in a min heap, the key of P is less than or equal to the key of C
            - heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero for frequent access of smallest value
        - bisect has tools for manipulating sorted lists, like insertions that maintain sort
        - list support stack/queue structures with append/pop()/pop(0)
        - collections.deque supports stack/queue structure with append/pop/popleft
            - deques support thread-safe, memory efficient appends & pops
            - use for queues & breadth first tree searches
        - memory of sorts (high to low): bsimq 

        class Stack:

            def __init__(self):
                self.stack = []

            def push(self, item):
                self.stack.appen(item)

            def pop(self):
                if len(self.stack) == 0:
                    return None
                return self.stack.pop() # self.stack.pop(0) for queue

            def size(self):
                return len(self.stack)

            def hanoi(disk, source, temp, dest):
                if disk == 1:
                    move(disk, source, dest)
                else:
                    hanoi(disk - 1, source, temp, dest)
                    move(disk, source, dest)
                    hanoi(disk - 1, temp, dest, source)

            def iterative_fibonacci():
                fo = 0
                f1 = 1
                for (i < 1; i < n; i++):
                    fib = fo + f1
                    fo = f1
                    f1 = fib

            def recursive_fibonacci(fib, f0, f1):
                if len(fib) < 99:
                    next_value = f0 + f1
                    fib.append(next_value)
                    recursive_fibonacci(fib, f1, next_value)
                return fib

            fo = 0
            f1 = 1
            fib = []
            recursive_fibonacci(fib, f0, f1)


## python data structures

        - primitives
            - float
            - int
            - str
                - raw string (no special chars like \n): r'C:\some\name'
                - slice: 
                    - 'test'[0:2] = 'te' # the end char at position 2 is excluded
                    - s[:i] + s[i:] == s
                    - an omitted start index defaults to zero, an omitted end index defaults to the size of the string
                    - negative indexes start at -1

                - format:
                    
                    - format(input, format)
                        format(math.pi, '.2f') = '3.14'

                    - "%(var1)s" % dict
                        '%(var1)s' % {'var1': "Python"} # s specifies string type

                    - str.format(expr_or_vars)
                        "{int1}".format(expression_for_n)
                        "{0}".format(1+2)
                        '{0} = {1}'.format(var1, var2)

                    - f""
                        f"{var1!expression_key}" == f"{expression(var1)}"
                        f"{var1!r}." == f"{repr(var1)}."

                    - f"{expr}"
                        f"{var1:{type_arg1}.{type_arg2}}" 
                        var1 = decimal.Decimal("12.34567")
                        f" {var1:{width}.{precision}}" # nested field example

                    - f"{var1:format}"
                        var1 = 1024
                        f"{var1:#0x}" = '0x400' # uses format specifier
            - bool

        - sequence data type: list, tuple, range, str

        - tuple (immutable) = ()

            - tuple1 = 1,

            - can contain mutable objects like lists

            - accessed with sequence unpacking rather than iterating
                t = 1, 2, 3
                x, y, z = t # fetches 1, 2, and 3 values from t in order

                - any sequence supports this but item count must be equivalent

            - support nesting
                t = 1, 2, 'a'
                u = t, (1, 2, 3, 4, 5) = ((1, 2, 'a!'), (1, 2, 3, 4, 5))

        - set (unique) = set()
            - set1 = {1}
            - unordered collection with no duplicates
                a - b                              # letters in a but not in b
                a | b                              # letters in a or b or both
                a & b                              # letters in both a and b
                a ^ b                              # letters in a or b but not both

            - supports set comprehensions

            - ordered set
            - frozen set

        - array = arr.array()
            - requires same data type, for memory improvements
            - array of numbers stored as two byte unsigned binary numbers (typecode "H") vs. the usual 16 bytes per entry for lists of ints:
                a = array('H', [4000, 10, 700, 22222])

        - list = []
            - lists are order-retaining sequences
            - represented internally as an array
            - the largest costs come from growing beyond the current allocation size (because everything must move), or from inserting/deleting near the beginning (because everything after that must move)
            - good for stacks using append/pop to modify the last item, but not for queues bc inserting/appending/removing at the first position requires a shift of all the others
            - deque is good for queues where the both ends will be changed or when first item needs to be changed (from collections import deque, queue = deque(some_list), queue.append, queue.popleft)
            - concatenation: result.append(a) = result = result + [a]
            - use for random access & stacks
            - optimized for fast fixed-length operations
            - incur O(n) memory movement costs for pop(0) & insert(0, v) operations which change size & position

        - collections.deque() list-like object:
            - deques support thread-safe, memory efficient appends & pops from either side of the deque with about the same O(1) performance in either direction
            - represented internally as a doubly linked list
            - faster appends & pops from left end than lists (O(1) for deques, O(n) for lists), slower lookups in the middle (O(n) for deques, O(k) for lists)
            - use for queues & breadth first tree searches
            - indexed access is O(1) at both ends but slows to O(n) in the middle

                listvar = deque([starting_node])

                def breadth_first_search(sequence):
                    node = sequence.popleft()
                    for m in node:
                        if m == target_val:
                            return m
                    listvar.append(node)

        - heap:
            - priority queue
            - heap is a specialized tree-based data structure which is an almost complete tree that satisfies the heap property
                - in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C
                - in a min heap, the key of P is less than or equal to the key of C
            - heapq module provides functions for implementing heaps based on regular lists. The lowest valued entry is always kept at position zero for frequent access of smallest value

        - bisect has tools for manipulating sorted lists, like insertions that maintain sort

        - complexity

            - list:
                - O(1)
                    get/set/append/pop last/len
                - O(k)
                    get slice/pop intermediate/extend 
                - O(n)
                    insert/delete/iterate/delete slice/in/min/max
                - O(k + n)
                    set slice
                - O(n log n)
                    sort
                - O(nk)
                    multiply

            - deque:
                - O(1)
                    - append, appendleft, pop, popleft
                - O(k)
                    - extend, extendleft, rotate
                - O(n)
                    - remove, copy

            - dict:
                - O(1)
                    - get, set, delte
                - O(n)
                    - iterate, copy

            - set:
                - O(1)
                    - in
                - O(added len of both sets)
                    - union
                - O(lower len of sets)
                    - intersection

            - visual:
                - strange similarities/differences should be grouped together in a table where possible
                - an expectation table would show only surprising similarities/differences in performance for structures expected to be similar/different given position

        - dict = {}
            - dict class can now remember insertion order
            - keys can be any immutable type (strings, numbers, or tuples with no mutable objects)
            - list(d) returns a list of keys used, in insertion order
            - dict([('k1', 1), ('k2', 2), ('k3', 3)]) = dict(k1=1, k2=2, k3=3)
            - supports dict comprehensions

        - stack (LIFO)
            - list type makes a decent stack data structure as it supports push & pop operations in amortized O(1) time, and random access is O(1)
                - given that theyre based on arrays, they occasionally need to resize the storage space with append/insert/deletes
            - linked list has more stable O(1) inserts/deletes

        - queue (FIFO)
            - collections.deque offers optimized end insert/append/delete

        - non linear:
            - tree
            - graph

        - lists
            - CPython uses an array of pointers
            - python lists are dynamic (variable-length) arrays
                The elements of an array occupy a contiguous block of memory, and once created, its size cannot be changed. 
                A dynamic array can, once the array is filled, allocate a bigger chunk of memory, copy the contents from the original array to this new space, and continue to fill the available slots.

        - A list keeps order, dict and set dont
            - when you care about having mutability/order, need duplicates, different types, or need quick insert/delete from end of sequence, use list
            - if you plan on modifying/extending the list a lot (beyond allocation size) or by large numbers of items, use array/set/dict
            - if you need quick insert/delete from both sides but not the middle, use deque 
            - to check for group membership, use set or dict (keys)
            - if you need to minimize memory or access/iteration time and dont need to change the list, use a tuple
            - if you only need iteration & can functionalize it, consider creating a generator
            - if you care about types, built-in arrays are a stricter option, and sets required hashable items 
            - for faster search or linear algebra operations, numpy arrays are a good alternative to list
            - when you want fast lookups, use a set/tuple/dict

        - dict associates with each key a value, while list and set just contain values/positions

        - set requires items to be hashable, list doesnt: 
            - if you have non-hashable items, you cannot use set and must use list

        - set forbids duplicates, list does not
            A "multiset", which maps duplicates into a different count for items present more than once, 
            can be found in collections.Counter

            - Checking for membership of a value in a set (or dict, for keys) is very fast (taking about a constant, short time)

        - Are dictionaries or lists faster for lookups?
            Looking up a value in a list takes O(n) time because the whole list needs to be iterated through until the value is found.
            Looking up a key in a dictionary takes O(1) time because it’s a hash table.
        
        - list vs. tuple 
            List (mutable)
                - consume more memory
                - time-consuming to iterate, quick to insert/delete at end
            Tuple (immutable)
                - consume less memory as compared to the list
                - quicker to iterate/access the elements

        - list vs. numpy array:
            Lists can be populated with different types of data at each index. Arrays require homogeneous elements.
                - they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element. 
            Arithmetic on lists adds or removes elements from the list. 
            Arithmetic on arrays functions per linear algebra.
            Numpy Arrays also use less memory and come with significantly more functionality and are faster at searching

        - list vs. array (import array as ar)
            - arrays can hold only a single data type elements whereas lists can hold any data type elements.


    ''' python operation complexity, where n is one number of iterations and k is another number of iterations '''
    'n' is the number of elements currently in the container. 
    'k' is either the value of a parameter or the number of elements in the parameter. 

    Data Structure                                  Sub-Structure:

        list                                        Dynamic Array
        COLLECTIONS.DEQUE (a double-ended queue)    Doubly linked list of arrays, rather than objects
        dict                                        Hash Table 

    *****LIST*****
    - list is implemented as an array
    - largest costs come from growing beyond the current allocation size (because everything must move), 
        or from inserting or deleting somewhere near the beginning (because everything after that must move)
    - If you need to add/remove at both ends, consider using a collections.deque instead

    Operation                   Average Case    Amortized Worst Case        
        Copy                    O(n)            O(n)        
        Append[1]               O(1)            O(1)        
        pop() Pop last          O(1)            O(1)        
        pop(i) Pop intermed     O(k)            O(k)        
        Insert                  O(n)            O(n) 
        insert(i,val)           O(n)       
        Iteration               O(n)            O(n)     
        Reverse                 O(n)
        Concatenate             O(k)   
        Delete Item             O(n)            O(n)              
        Del Slice               O(n)            O(n)  
        Get Slice [x:y]         O(k)            O(k)  
        index() Get Item        O(1)            O(1)        
        Set Slice               O(k+n)          O(k+n)    
        index assign/Set item   O(1)            O(1)   
        Extend[1]               O(k)            O(k)        
        Sort                    O(n log n)      O(n log n)      
        Multiply                O(nk)           O(nk)       
        x in s                  O(n)        
        min(s), max(s)          O(n)        
        Get Length              O(1)            O(1) 

    *****COLLECTIONS.DEQUE (a double-ended queue, implemented as a doubly linked list of arrays) *****

    - Both ends are accessible, but even getting a value at the middle is slow, and adding to or removing from the middle is even slower. 

    Operation       Average Case    Amortized Worst Case
        Copy        O(n)            O(n)
        append      O(1)            O(1)
        appendleft  O(1)            O(1)
        pop         O(1)            O(1)
        popleft     O(1)            O(1)
        extend      O(k)            O(k)
        extendleft  O(k)            O(k)
        rotate      O(k)            O(k)
        remove      O(n)            O(n) 

    *****DICT*****
    - implemented as a hash table
    - average case assumes hash function is designed to make collisions uncommon, and that param keys are selected uniformly at random from the full key set
    - there is a fast-path for dicts with str keys; this doesnt affect complexity, but it can affect constant factors, like how quickly a typical program finishes

    Operation           Average Case    Amortized Worst Case
        Copy[2]         O(n)            O(n)
        Get Item        O(1)            O(n)
        Set Item[1]     O(1)            O(n)
        Delete Item     O(1)            O(n)
        Iteration[2]    O(n)            O(n)  

    [1] = relies on the "Amortized" part of "Amortized Worst Case". 
        Individual actions may take surprisingly long, depending on the container history.
    [2] = For these, the worst case n is the maximum historical container size, rather than the current size. 
        For example, if N objects are added to a dictionary, then N-1 are deleted, 
        the dictionary will still be sized for N objects, at least until another insertion is made. 

    *****SET*****
    - implemented similarly to a dict
    - To perform set operations like s-t, s & t need to be sets. But you can do method equivalents if t is any iterable, like s.difference(l), where l is a list. 

    Operation                               Average case            Worst Case                                  notes
        x in s                              O(1)                    O(n)        
        Union s|t                           O(len(s)+len(t))            
        Intersection s&t                    O(min(len(s), len(t))   O(len(s) * len(t))                          replace "min" with "max" if t is not a set
        Multiple intersection s1&s2&..&sn                           (n-1)*O(l) if l is max(len(s1),..,len(sn))      
        Difference s-t                      O(len(s))           
        s.difference_update(t)              O(len(t))           
        Symmetric Difference s^t            O(len(s))               O(len(s) * len(t))      
        s.symmetric_difference_update(t)    O(len(t))               O(len(t) * len(s))      

    Data structure features:
        - numerical operators: **, //, /, % take priority over 
          comparison operators: in/not in (to check sequence value occurrence), is/is not (to check object equivalence)
        - use iterators rather than sequences if you can bc iterators dont build the sequence before looping, 
            whereas looping over a sequence requires that the sequence is built first 
        - sequence types: str, unicode, list, tuple, bytearray, buffer, xrange

        str:
            - has similar index & slice operations as a list bc its a sequence too

        list:
            - pop from the front of a list takes o(n) bc it has to shift the position of all the following items, 1 unit to the left after removing 1st item
            - pop from the end of a list takes o(1) bc it only has to do 1 remove operation & no shift operations
            - LIFO stack lists are good (using append(val) to add item to end, pop() to retrieve last item added at end)
            - FIFO queues lists arent good (append & pop from queue list end are fast but inserts & pops at the queue list front arent bc other items must be shifted)
            - use del to remove an item from a list given its index instead of its value, as opposed to the pop() method to remove an item, which returns the value
        dict:
            - unordered set of key-value pairs
            - keys must be unique
            - sequences are indexed by numbers, whereas dicts are indexed by keys
            - dict keys can be any immutable type, like strings, numbers; keys can be a tuple if it only includes immutable objects like strings, numbers, or tuples
            - supports: key in this_dict, delete a key value with del this_dict[key]
            - this_dict.keys() returns a list of keys, which can be sorted with sorted(this_dict.keys())
            - supports dict comprehensions: {x: x**2 for x in (2, 4, 6)} = {'2': 4, '4': 16, '6': 36}
            - using dict() builds a dict from a sequence of key-value pairs, like a list of two-dimensional tuples, or a set of key=value arguments passed to dict()
        set: 
            - unordered (does not store position or insertion order) sequence with no duplicates
            - useful for determining duplicates or doing set operations like union/intersection/difference/subset/superset
            - supports: x in this_set, len(set), for x in set, set comprehensions like a = {x for x in 'abracadabra' if x not in 'abc'}
            - the set copy does a shallow copy
            - create an empty set with the set() function, which can take a sequence as a parameter to create a set with no duplicates out of the sequence 
            - you can use curly braces to create a set of values, but not to create an empty
        tuple:
            - immutable
            - often contain heterogenous sequences, where lists usually contain homogenous sequences
            - to assign values to a tuple, dont use parentheses, use commas:
                this_tuple = 2,3,'this_val', my_dict
              unless youre initializing an empty tuple, then use parentheses:
                this_empty_tuple = ()
              if youre only assigning one value to a tuple, use a trailing comma:
                this_single_tuple = 1,
