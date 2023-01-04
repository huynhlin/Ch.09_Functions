'''
MINI FUNCTION
------------
Write a function called mini that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))

OUTPUT
------
3
4
2
-100
A

The function should return the value, not print the value. 
Also, while there is a min function built into Python, don't use it. 
Please use if statements and practice creating it yourself.
'''
# first = input("Input a number.")
# second = input("Input a number.")
# third = input("Input a number.")
# inputs = [first, second, third]


def mini(first, second, third):
    try:
        if first < second and first < third:
            return first
        elif second < first and second < third:
            return second
        elif third < first and third < second:
            return third
        else:  # tie breakers
            if first < second:
                return first
            if first < third:
                return first
            if second < third:
                return second
            if second < first:
                return second
            if third < first:
                return third
            if third < second:
                return third

    except TypeError:
        inputs = [first, second, third]
        inputs.sort()
        return inputs[0]


print(mini(7, 3, 5))
print(mini(5, 5, 4))
print(mini(2, 2, 3))
print(mini(-2, -6, -100))
print(mini("Z", "B", "A"))
# it works :D
