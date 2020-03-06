#
# Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
# Begin with an interval covering the whole array. If the value of the search key is
# less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise narrow it to the upper half.
# Repeatedly check until the value is found or the interval is empty.
#

def binary_search(arr, x, start, end):
    index = start + ((end - start) // 2)
    if x == arr[index]:
        return index
    elif x < arr[index]:
        return binary_search(arr, x, start, index)
    elif x > arr[index]:
        return binary_search(arr, x, index, end)
    else:
        return -1


def main():
    arr = [1, 7, 13, 23, 31, 36, 41, 48, 50, 53, 54, 58, 74, 82, 93, 101, 102, 106, 109]
    x = 7
    print(binary_search(arr, x, 0, len(arr) - 1))


if __name__ == "__main__":
    main()
