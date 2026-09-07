def g(x):
    return 3* x**2 - 2*x +5
print(g(2))
print(g(5))

def absolute (x):
    if x >=0:
        return x;
    else:
        return -x
print (absolute (5))
print (absolute (-3))

def calculate(x):
    y = x**2
    z = y + 10
    return z
answer = calculate(5)
print(answer)



def square_list(numbers):
    result = []
    for x in numbers:
        result.append(x**2)
    return result
a = [1, 2, 3, 4, 5]
b = square_list(a)
print(b)



def positive_numbers(numbers):
    result = []
    for x in numbers:
        if x >0:
             result.append (x)
    return result
a = [-3, 5, -1, 8, 0, 4, -7]
b = positive_numbers(a)
print(b)



def even_squares (number):
    result = []
    for x in number:
        if x % 2 == 0:
            result .append (x**2)
    return result
a=[3,8,5,2,7,10,4]
b=even_squares(a)
print(b)



    