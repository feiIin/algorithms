#!interpreter
#
# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].


def linear_search(arr, x):
    """
    Return an int
    function to return the position of a given element in an array
    """
    for i, value in enumerate(arr):
        if value == x:
            return i


def main():
    arr = [4, 3, 23, 65, 45, 32, 31, 7, 43, 32, 12, 9, 43, 23, 76, 34]
    x = 12
    print(linear_search(arr, x))


if __name__ == "__main__":
    main()
