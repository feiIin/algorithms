# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# Sort the numbers, then add one number and sort again


def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array


def insertion_sort(arr):
    for i in range(1, len(arr)):
        number = arr[i]
        while arr[i] < arr[i-1]:
            swap(arr, i, i-1)
            if i > 1:
                i = i-1

    return arr


def main():
    arr = [32, 4, 54, 32, 76, 5, 87, 34, 7, 9, 2, 43, 83, 61, 52]
    arr = insertion_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()

