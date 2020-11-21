- NumPy

        - adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
        - NumPy targets the CPython reference implementation of Python, which is a non-optimizing bytecode interpreter. Mathematical algorithms written for this version of Python often run much slower than compiled equivalents. NumPy addresses the slowness problem partly by providing multidimensional arrays and functions and operators that operate efficiently on arrays, requiring rewriting some code, mostly inner loops using NumPy
        - Due to Python's extensive mathematics library, and the third-party library NumPy that further extends the native capabilities, it is frequently used as a scientific scripting language to aid in problems such as numerical data processing and manipulation


    # If axis=1, then it works on each row
    print(np.argmax(array, axis=1))

    # If axis=0, then it works on each column
    print(np.argmax(array, axis=0))

    # Sort along each row
    print(np.sort(array, axis=1))

    # Sort along each column
    print(np.sort(array, axis=0))

    # return indexes for sorting an array
    print(np.argsort(array))

    # add row
    newArray = np.vstack((array, newRow))

    # add column
    newArray = np.column_stack((array, newColumn))

    # reverse 
    reversedArray = np.flipud(array)

    # multiply matrixes (dot product)
    result = np.dot(matrix1, matrix2)
