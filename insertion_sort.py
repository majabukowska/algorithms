# 0(n2)
# simillar to selection and bubble sort, but tends to be a bit faster

def insertion_sort(array):
    length = range(1, len(array))
    for i in length:
        value_to_sort = array[i]

        while array[i - 1] > value_to_sort and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i =- 1
    return array

test = [1, 4, 3, 6, 7]
print(insertion_sort(test))