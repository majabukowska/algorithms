# FizzBuzz and Sorting Algorithms
This repository contains Python code for implementing the FizzBuzz problem and several sorting algorithms: Bubble Sort, Quick Sort, Insertion Sort, Counting Sort, and Binary Search.

### FizzBuzz
The FizzBuzz problem is solved using the division function. Given a number, the function checks if it's divisible by 3, 5, or both, and returns "Fizz", "Buzz", "FizzBuzz", or the number itself accordingly. The create_list function generates a list of numbers from 1 to 100 and applies the division function to each number, resulting in a list of FizzBuzz outputs.

## Sorting Algorithms

### Bubble Sort
The bubble function implements the Bubble Sort algorithm. It iterates through the input array and compares adjacent elements, swapping them if they are in the wrong order. This process is repeated until the entire array is sorted.

### Quick Sort
The quick_sort function demonstrates the Quick Sort algorithm. It selects a pivot element and divides the array into two sub-arrays - one containing elements smaller than the pivot and the other containing elements greater than the pivot. The function recursively sorts these sub-arrays and concatenates them around the pivot.

### Insertion Sort
The insertion_sort function showcases the Insertion Sort algorithm. It iterates through the array, comparing each element with the elements before it and moving them one position ahead if necessary to place the element in the correct sorted position.

### Counting Sort
The counting_sort function implements the Counting Sort algorithm, which is suitable for sorting integers within a specified range. It uses auxiliary arrays to count the occurrences of each element and then reassembles the sorted array.

### Binary Search
The binary_search function demonstrates the Binary Search algorithm. Given a sorted array and an item to search for, it repeatedly divides the search interval in half until the item is found or the interval is empty.
