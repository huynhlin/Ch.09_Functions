'''
10,000 NUMBERS
--------------

In this program we will write three different functions.

Function #1: Write a function named create_list that takes
in a list size and returns a list of random numbers from 1-6.
i.e., calling create_list(5) should return 5 random numbers from 1-6.
Once you've finished writing your function, copy and paste the
following code after it and make sure it works with the function you wrote:

INPUT
-----
my_list = create_list(5)
print(my_list)

OUTPUT
------
[2,5,1,6,3] #something like this 
'''
import random


def create_list(size):
    output = []
    for x in range(size):
        output.append(random.randint(1, 6))
    return output


# print(create_list(5))

'''
Function #2: Write a function called count_list that takes
in a list and a number. Have the function return the number
of times the specified number appears in the list. Once you've
finished writing your function, copy and paste the following code
after it and make sure it works with the function you wrote:

INPUT
-----
my_list = [1,2,3,3,3,4,2,1]
count = count_list(my_list,3)
print(count)

OUTPUT
------
3 
'''


def count_list(list, num):
    counter = 0
    for number in list:
        if num == number:
            counter += 1
    return counter


# my_list = [1, 2, 3, 3, 3, 4, 2, 1]
# count = count_list(my_list, 3)
# print("Your number appeared {} times in the list.".format(count))

'''
Function #3: Write a function called average_list that returns the 
average of the list passed into it. Once you've finished writing your
function, copy and paste the following code after it and make sure it
works with the function you wrote:

INPUT
-----
my_list = [1,2,3]
avg = average_list(my_list)
print(avg)

OUTPUT
------
2.0
'''


def average_list(list_to_average):
    total = 0
    counter = 0
    for number in list_to_average:
        total += number
        counter += 1
    average = total/counter
    return average


# my_list = [1, 2, 3]
# avg = average_list(my_list)
# print(avg)

'''
Now that the functions have been created, use them all in a main program that will:
1.) Create a list of 10,000 random numbers from 1 to 6. (1 line of code)
2.) Print the count of 1 through 6. (For example, "There are 1361 amount of 2s") (3 lines of code)
3.) Print the average of all 10,000 random numbers. (Make sure it's a float) (2 lines of code)
'''

ten_thousand = create_list(10000)
# print(ten_thousand)
for x in range(1, 6+1):
    total = count_list(ten_thousand, x)
    print("There are {} amount of {}'s in your list.".format(total, x))
avg = average_list(ten_thousand)
print("The average of the list is {:.3}".format(avg))

