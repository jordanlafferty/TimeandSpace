import timeit
from collections import Counter
from turtle import clear

import line_profiler
from memory_profiler import profile
import random


class utility:
    def __init__(self):
        pass

    def generateTestArray(self):
        a = []
        for i in range(10):
            a.append(random.randint(0, 10))
        return a


def generateOneDuplicate(theList):
    i = len(theList)
    i = i - 1
    j = random.randrange(i)  # 0 <= j <= i-1

    theList[j], theList[i] = theList[i], theList[j]
    return theList


def SCAN(arr):
    for i in range(len(arr) - 1 - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                print(i, " - ", j)
                print("duplicate num: ", arr[i])
                return


@profile
def STOR(arr):
    visited = [False] * 1000  # creates an array to see if you have visited that spot
    for i in range(len(arr)):
        if visited[arr[i]]:
            print("the duplicate occurs at i = ", i)
            print(arr[i])
            return i
        else:
            visited[arr[i]] = True


def STOR_LL(arr):
    currNode = arr.head
    currNode = currNode.next
    x = 1000000
    for i in range(1000000):
        a = currNode.getData()
        getNext = currNode
        x = x - 1
        for j in range(x):
            getNext = getNext.next
            y = getNext.getData()
            if y == a:
                print("the duplicate occurs at i = ", 10 - x + j)
                print(currNode.data)
                return
        currNode = currNode.next


@profile
def STOR_Dictionary(d):
    for key, value in d.items():
        if value == 2:
            print(key)
            return


def DictionaryImplementation():
    theArray = oneSameElementHW()
    d = dict(Counter(theArray))
    theArray.clear()
    STOR_Dictionary(d)


@profile
def LinkedListImplementation():
    theArray = oneSameElementHW()
    ll = LinkedList()
    head1 = Node(theArray[0])
    ll.head = head1
    prevNode = Node(0)
    for i in range(1000000):
        theNext = Node(theArray[i])
        theNext.setData(theArray[i])
        if i == 0:
            head1.next = theNext
            prevNode = theNext
        else:
            prevNode.next = theNext
            prevNode = theNext

    STOR_LL(ll)


def oneSameElementHW():
    arr = []
    arr.append(random.randint(0, 1000))
    i = 1
    for i in range(1000):
        arr.append(i)
        arr = generateOneDuplicate(arr)
    return arr


class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, num):
        self.data = num

    def getData(self):
        return self.data


# array_a = utility().generateTestArray()
# HOMEWORK
a = oneSameElementHW()
STOR(a)
# LinkedListImplementation()
DictionaryImplementation()

# STOR(x)
# print(timeit.Timer(STOR(x)).timeit(number=1))
# print(timeit.timeit('STOR(a)', setup='from __main__ import STOR, a', number=1))
# SCAN(x)
