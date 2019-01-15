# coding=utf-8
d = {'key1': 'value1', 'key2': {'key3': [1, 2, [3, 4]]}}

a = True
b = True
c = True

if a and b:
    x = [1, 1, 1, 3, 3, 5, 6, 6, 6, 6, 6, 9, 9, 9, 9]
    y = [2, 2, 4, 4, 7, 7, 8]
    z = x + y
    print(z)
    print(set(z))

elif c:
    print('elseif')

else:
    print(d['key2']['key3'][2][0])

# A tuple is a type of array that is constant
tuples = (1, 2, 3)


def my_process(param1='placeholder'):

    print(param1)

    for num in x:
        print(num)

    i = 1

    while i < 5:
        print(i)
        i += 1

    xyz = [num*2 for num in x]
    print(xyz)

my_process('My process worked!')


