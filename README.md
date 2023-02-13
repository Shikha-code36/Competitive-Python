# Competitive Programming Algorithm Library in Python

competitivepython is a library of algorithms and data structures implemented in Python. It is designed to be a useful resource for developers who need to implement common algorithms and data structures in their projects.

## Features

- Implements a wide range of algorithms and data structures, including:
  - Searches: Binary Search, Linear Search, KMP Pattern Search
  - Graphs: BFS, DFS, Dijkstra
  - Sorting: Bubble Sort, Insertion Sort, Shell Sort, Selection Sort, Bucket Sort, Merge Sort, Tim Sort, Quick Sort, Heap Sort, Radix Sort
  - Trees: Binary Search Tree
- Easy to use and understand, with well-documented code
- Portable and compatible with Python 3
- Open source and available under the MIT license

## Installation

To install competitivepython library, simply run the following command:

```
  pip install competitivepython
  ```

## Usage

To use PyPy in your project, simply import the desired algorithm or data structure and use it as needed. For example:

- searches implementation example
    ```
    from competitivepython import searches

    result = searches.binary_search([1, 2, 3, 4, 5], 3)
    result2 = searches.linear_search([5, 7, 9, 2, 4, 10], 4)
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    result3 = searches.kmp_search(pat,txt)
    print(result)  # Output: 2
    print(result2)  # Output: 4
    print(result3) # Output: [10]
    ```

- sorting implementation example
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    res = sorting.bubble_sort(arr)
    res1 = sorting.bucket_sort(arr)
    res2 = sorting.heap_sort(arr)
    res3 = sorting.insertion_sort(arr)
    res4 = sorting.merge_sort(arr)
    res5 = sorting.quick_sort(arr)
    res6 = sorting.radix_sort(arr)
    res7 = sorting.selection_sort(arr)
    res8 = sorting.shell_sort(arr)
    res9 = sorting.tim_sort(arr)

    print('bubble sort:', res, 'bucket sort:', res1, 'heap sort:', res2, 'insertion sort:', res3, 'merge sort:', res4,
        'quick sort:', res5, 'radix sort:', res6, 'selection sort:', res7, 'shell sort:', res8, 'tim sort:', res9)

    ''' Output --- 
     bubble sort: [6, 7, 12, 15, 112] bucket sort: [6, 7, 12, 15, 112] heap sort: [6, 7, 12, 15, 112] 
    insertion sort: [6, 7, 12, 15, 112] merge sort: [6, 7, 12, 15, 112] quick sort: [6, 7, 12, 15, 112] 
    radix sort: [6, 7, 12, # 15, 112] selection sort: [6, 7, 12, 15, 112] shell sort: [6, 7, 12, 15, 112] 
    tim sort: [6, 7, 12, 15, 112]
    '''
    ```

-  graphs implementation example
    ```
    from competitivepython import graphs

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1},
    }
    start = 'A'
    end = 'D'

    result = graphs.breadth_first_search(graph, 'C')
    result2 = graphs.depth_first_search(graph, 'C')
    result3 = graphs.dijkstra(graph, start, end)
    print("bfs:",result)
    print("dfs:",result2)
    print("dijikstra:",result3)

    ''' Output--
        bfs: {'B', 'D', 'C', 'A'}
        dfs: {'B', 'D', 'C', 'A'}
        dijikstra: {'distance': 4, 'path': ['B', 'C', 'D']}
    '''
    ```

- trees implementation example

    ```
    from competitivepython import trees

    # Create an instance of the BinarySearchTree
    bst = trees.BinarySearchTree()

    # Insert some values into the tree
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Check if a value is present in the tree
    print(bst.search(50)) # Output: True
    print(bst.search(35)) # Output: False

    # Get the values in the tree in in-order traversal order
    print(bst.get_in_order_traversal()) # Output: [20, 30, 40, 50, 60, 70, 80]
    ```

## Contributing

If you would like to contribute to the PyPy project, please refer to the contributing guidelines. We welcome contributions of all types, including bug reports, feature requests, and code contributions.

## License

PyPy is open source software released under the MIT license. Refer to the LICENSE file for more information.
