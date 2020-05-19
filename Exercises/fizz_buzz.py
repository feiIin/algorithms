#
# Write a program that prints the number from 1 to 100.
# For  multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"
#

if __name__ == "__main__":

    # create array from 1 to 100
    arr = list(range(1, 100))
    final_arr = []

    for num in arr:
        multiple_of_three = num % 3
        multiple_of_five = num % 5
        if multiple_of_three == 0 and multiple_of_five == 0:
            num = "FizzBzz"
        elif multiple_of_five == 0:
            num = "Buzz"
        elif multiple_of_three == 0:
            num = "Fizz"
        final_arr.append(num)
    print(final_arr)
