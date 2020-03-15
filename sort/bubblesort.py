# Bubble Sort is the simplest sorting algorithm that works by
# repeatedly swapping the adjacent elements if they are in wrong order.


def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j+1)
    return arr



def main():
    arr = [29, 54, 32, 6, 32, 98, 11, 7, 39, 33, 24, 72, 22]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()