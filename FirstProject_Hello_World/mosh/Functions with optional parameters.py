def increment(number, by):
    return number + by
# In this function, we need 2 arguments (number  and by), otherwise it won't work

print(increment(2, 2))


def increment(number, by=8):
    return number + by
# In this function we are giving a default value to one of the parameters( by=1), so we can call the function
# without a second argument and it will automatically take the default value as the parameter
# !!! Keep in mind that all optional parameters should come after the required parameters.


print(increment(2, 1))

################################################################

def multiply(x, y):
    return x * y
# in this function, we take 2 parameteters and multiply them, but if we have more than 2 numbers to multiply we can't


print(multiply(2, 4))