'''
FIND FUNCTION
-------------
Write a function called FIND that will take a list of numbers, "list", 
along with one other number, "key". Have it search the list for the value
contained in key. Each time your function finds the key value, 
print the list position of the key. You will need to juggle three variables,
one for the list, one for the key, and one for the position of where you are 
in the list. You may want to review your notes for the code to iterate though
a list using the range and len functions. Start with that code and modify the 
print to show each element and its position. Then instead of just printing 
each number, add an if statement to only print the ones we care about. 
Once you've finished writing your function, copy and paste the following code 
after it and make sure it works with the function you wrote:

INPUT
-----
list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(list, 12)
find(list, 91)
find(list, 80)

OUTPUT
------
Found 12 at position 11
Found 12 at position 13
Found 91 at position 5

Use a for loop with an index variable and a range. 
Inside the loop use an if statement. This function 
can be written in about four lines of code.
'''


def find(list, key):
    position = 0
    for number in range(len(list)):
        position += 1
        if number == key:
            print("Found {} at position {}.".format(key, position))


my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)
