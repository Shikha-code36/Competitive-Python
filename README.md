# Competitive Programming Algorithm Library in Python

competitivepython is an open-source library of algorithms and data structures implemented in Python. It offers a collection of frequently used algorithms and data structures that can be directly used in any Python-based project.

- Checkout the blog regarding this library [Click Here](https://pandeyshikha075.medium.com/an-overview-of-competitivepython-a-python-library-for-implementing-algorithms-and-data-structures-3a5776e13535)

## Features

- Provides implementations for several common algorithms and data structures such as:
  - Searches: Binary Search, Linear Search, KMP Pattern Search
  - Graphs: BFS, DFS, Dijkstra
  - Sorting: Bubble Sort, Insertion Sort, Shell Sort, Selection Sort, Bucket Sort, Merge Sort, Tim Sort, Quick Sort, Heap Sort, Radix Sort
  - Trees: Binary Search Tree
- Codebase is easy to use, well-documented, and compatible with Python 3.
- Open source and available under the MIT license

## Installation

To install competitivepython library, simply run the following command:

```
  pip install competitivepython
  ```

## Usage

To use competitivepython in your project, import the desired algorithm or data structure and use it as needed. Below are some example use cases:

- Implementing searches:
  - Binary Search
    ```
    from competitivepython import searches
    
    arr = [1, 2, 3, 4, 5]
    target = 3
    
    result = searches.binary_search(arr, target)
  
    print("Binary Search:",result)  
    
    '''Output: 
    Binary Search: 2
    '''
    ```
  - Linear Search
    ```
    from competitivepython import searches
    
    arr = [5, 7, 9, 2, 4, 10]
    target = 4
    
    result = searches.linear_search(arr, target)
    
    print("Linear Search:",result)  
    
    '''Output: 
    Linear Search: 4
    '''
    ```
  - Knuth–Morris–Pratt string Search
    ```
    from competitivepython import searches
    
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    
    result = searches.kmp_search(pat,txt)
    
    print("KMP Search:",result) 
    
    '''Output: 
    KMP Search: [10]
    '''
    ```
    
- Implementing sorting:
  - Bubble Sort
    ```
      from competitivepython import sorting

      arr = [112, 6, 7, 12, 15]

      result = sorting.bubble_sort(arr)
      print('bubble sort:', result)

      ''' Output --- 
       bubble sort: [6, 7, 12, 15, 112] 
      '''
      ```
   - Bucket Sort
      ```
      from competitivepython import sorting

      arr = [112, 6, 7, 12, 15]

      result = sorting.bucket_sort(arr)
      print('bucket sort:', result)

      ''' Output --- 
       bucket sort: [6, 7, 12, 15, 112]
      '''
      ```
  - Heap Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]
    
    result = sorting.heap_sort(arr)
    
    print('heap sort:', result)

    ''' Output --- 
     heap sort: [6, 7, 12, 15, 112] 
    '''
    ```
  - Insertion Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.insertion_sort(arr)
    
    print('insertion sort:', result)

    ''' Output ---  
    insertion sort: [6, 7, 12, 15, 112] 
    '''
    ```
  - Merge Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.merge_sort(arr)
    
    print('merge sort:', result)

    ''' Output --- 
     merge sort: [6, 7, 12, 15, 112] 
    '''
    ```
  - Quick Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.quick_sort(arr)
    
    print('quick sort:', result)

    ''' Output --- 
     quick sort: [6, 7, 12, 15, 112] 
    '''
    ```
  - Radix Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.radix_sort(arr)
    
    print('radix sort:', result)

    ''' Output --- 
    radix sort: [6, 7, 12, # 15, 112]
    '''
    ```
  - Selection Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]
    
    result = sorting.selection_sort(arr)
    
    print('selection sort:', result)

    ''' Output --- 
    selection sort: [6, 7, 12, 15, 112]
    '''
    ```
  - Shell Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.shell_sort(arr)

    print('shell sort:', result)

    ''' Output --- 
     shell sort: [6, 7, 12, 15, 112] 
    '''
    ```
  - Tim Sort
    ```
    from competitivepython import sorting

    arr = [112, 6, 7, 12, 15]

    result = sorting.tim_sort(arr)

    print('tim sort:', result)

    ''' Output --- 
    tim sort: [6, 7, 12, 15, 112]
    '''
    ```
  
-  Implementing graphs:
    - Breadth First Search (or Breadth First Traversal)
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

      print("bfs:",result)

      ''' Output--
          bfs: {'B', 'D', 'C', 'A'}
      '''
      ```
    - Depth First Search(or Depth First Traversal)
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

      result = graphs.depth_first_search(graph, 'C')
      print("dfs:",result)

      ''' Output--
          dfs: {'B', 'D', 'C', 'A'}
      '''
      ```
    - Dijkstra’s Shortest Path
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

      result = graphs.dijkstra(graph, start, end)
      print("dijikstra:",result)

      ''' Output--
         dijikstra: {'distance': 4, 'path': ['B', 'C', 'D']}
      '''
      ```

- Implementing trees:

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

If you would like to contribute to the competitivepython project, please refer to the contributing guidelines in CONTRIBUTING.md. We welcome contributions of all types, including bug reports, feature requests, and code contributions.

## License

competitivepython is open source software released under the MIT license. Refer to the LICENSE file for more information.
