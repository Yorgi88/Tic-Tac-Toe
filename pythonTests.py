# we are going to revise about dictionaries and all
# python uses key => value pairs as you've seen

from collections import defaultdict
from itertools import filterfalse
from datetime import datetime
import cProfile
import timeit
# to import default dictionary values

from functools import partial
from operator import mul

d = {
    'firstKey': 1,
    'secondKey': 2,
    'thirdKey': 3,
    'fourthKey': 'bitchKey'
}
# lets iterate over the dictionary
x = d['thirdKey']
print(x)
# for key in d:
#     print(key + ' =>', d[key])
# tis prints the key, value pairs in that order
# we can also use a dictionary comprehension too

print([[key + '=>', d[key]] for key in d])

# u can also use the .items() method to print all k,v

# for key, value in d.items():
#     print(key + ' =>', value)

# to iterate over the values, use d.values()


# lets make use of the default dict we imported above

# w = defaultdict(int)
# print(w['key'])
# x = w['key'] = 'haha, the bitch key'
# print(x)


# lets talk abount or code about merging dicts
# fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
# dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
#
# # lets merge this dictionaries
#
# mergeIt = {**fish, **dog}
# print(mergeIt)


# print(d.keys())
# print(d.values())

print(d.get('firstKey'))
print(d.get('fourthKey'))

# if u don't want an error to occur wen getting the values use the get
# method


mydict = {
    'a': [1, 2, 3, 4],
    'b': ['one', 'two', 'three']
}

mydict['a'].append(5)
print(mydict['a'])
mydict['b'].append('four')
print(mydict['b'])
# this is to append elements in the dicts


#       WE ARE GOING INTO FILTER AND MAP METHODS
# to filter means to discard elements of a sequence based on some criteria

names = ['Fred', 'Dredd', 'Ted', 'Lucy', 'Lucius', 'Med']


# for name in names:
#     if len(name) > 4:
#         print(name)

# lets make the above code into a list comprehension

# print([name for name in names if len(name) > 4])
# there we have it

def longNames(name):
    return len(name) > 4


print(list(filter(longNames, names)))


#       MAPS

# calls = ['Ferd', 'wilson', 'jeremy', 'annette']
# def retNames(call):
#     return len(call) > 4
# x = list(map(retNames, calls))
#
# print(x)


def to_percent(num):
    return num * 100


f = list(map(to_percent, [0.89, 0.34, 0.74]))
print(f)

# lets try to convert dollar to naira
# we're going to import some libraries
# from functools import partial
# from operator import mul

rate = 750
dollars = {
    'bed-stand': 400,
    'jeans': 120,
    'mobile phone': 600
}

h = sum(map(partial(mul, rate), dollars.values()))
print(h)

# def exchange_rate(amount):
#     rate = 750
#     return rate * amount
#
# def actual_amount(num):
#     return exchange_rate(num)
# x = actual_amount(1120)
# print(x)
#

# fruits = ['orange', 'mango', 'guava', 'apple', 'coconut', 'pineapple']
# for fruit in fruits:
#     while True:
#         selector = int(input('Enter the fruit available: '))
#
#         if selector > 5:
#             print('out of range')
#             break
#         selection = fruits[selector]
#         print(selection)
#
#
#         continue


#       LETS TRY SOMETHING ELSE STILL WITHIN THE MAP
# series mapping example


insects = ['fly', 'ant', 'beetle', 'cankerworm']
f = lambda x: x + ' is an insect'
print(list(map(f, insects)))

s = 'draculA'
print(s[::-1])


#           LETS ENTER FILES AND FOLDERS I/O
# f = open("c\Users\MOSES\mbox.txt" , "r")
# for words in f:
#     print(words)
# f.close()

# with open("mbox.txt", 'r') as file:
#     lines = file.readlines()
# for texts in range(len(lines)) :
#     print(texts)


# FUNCTIONS
#
# def greeting(msg = 'Howdy') :
#     return msg
# print(greeting())


# def choose(x):
#     if x <= 2:
#         return 'Not good enough'
#     else:
#         return 'haha, welcome here to the python class'
# print(choose(int(input('Enter a goddamn number: '))))


# defining a function capable of taking an arbitrary number of argument

# def func(*args):
#     for items in args:
#         print(items)
#
#
# func(1, 3, 4, 'wewin always')
#
#
# def keyWord(**kwargs):
#     for keys, values in kwargs.items():
#         print(keys + ' =>', values)



# cDicts = {
#     'foo' : 1,
#     'boo' : 1,
#     'goo' : 6
# }
#
# keyWord(**cDicts)
# print(keyWord(key1=3, key2=6, key3=9))

f = lambda : 'hello world'
print(f())

#
# now = datetime.now()
# print(now)
# to check the current date of the day


# def f(x):
#     return '45'
# cProfile.run('f(4)')

# n = int(input(' enter a num: '))
# for i in range(n):
#     print(timeit(i))

lists = ["The cat", "is gon", "forever"]
f = []
print('will cry tonight'.format(lists, "{0} {1}"))