# if __name__ == "__main__":
#     main()

def test_function(first, second):
    '''This function adds two numbers together'''
    global total
    total = first + second
    return total


help(test_function)

print(test_function(2, 3))


def hypotenuse(leg_1, leg_2):
    hyp = (leg_1**2 + leg_2**2)**1/2
    return hyp


print(hypotenuse(2, 3))
