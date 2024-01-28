# FIZZBUZZ
def division(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return number


def create_list():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    return numbers


if __name__ == "__main__":
    numbers = create_list()
    finished_numbers = []
    for i in numbers:
        finished_numbers.append(division(i))
    print(finished_numbers)

# BUBBLE SORT

def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# QUICK SORT

def quick_sort(arr):
    length = len(arr)
    smaller_numbers = []
    greater_numbers = []

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    for i in arr:
        if i > pivot:
            greater_numbers.append(i)
        else:
            smaller_numbers.append(i)
    return quick_sort(smaller_numbers) + [pivot] + quick_sort(greater_numbers)


# COUNTING SORT

def counting_sort(arr):
    arr_len = len(arr)
    output = [0] * arr_len
    arr_count = [0] * 10

    for i in range(0, arr_len):
        arr_count[arr[i]] += 1

    for j in range(1, 10):
        arr_count[j] += arr_count[j - 1]

    a = arr_len - 1
    while a >= 0:
        output[arr_count[arr[a]] - 1] = arr[a]
        arr_count[arr[a]] -= 1
        a -= 1

    for k in range(0, arr_len):
        arr[k] = output[k]

# BINARY SEARCH

def binary_search(arr, item):
    begin_index = 0
    end_index = len(arr) - 1
    while begin_index <= end_index:
        midpoint = int(begin_index + (end_index - begin_index) / 2)
        midpoint_value = arr[midpoint]
        if item == midpoint_value:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return "Not found"

