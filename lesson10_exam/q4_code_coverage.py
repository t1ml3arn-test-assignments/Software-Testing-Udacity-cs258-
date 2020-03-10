# Code Coverage
# ---------------
# Achieve full statement coverage and parameter value coverage for
# strings, integers, and booleans on this enhanced Queue class.
#
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.

# This specific Queue class can enqueue not only integers,
# but strings and booleans as well. You will need to provide
# parameter value coverage for these data types by adding
# each type of data into your Queue. 
#
# Furthermore, this Queue class has the additional methods
# clear() and enqueueall(). The enqueueall method takes
# in a list or tuple and enqueues each item of the collection
# individually, returning True if all enqueues succeed, and
# False if the number of items in the collection will overfill
# the Queue.

# To run this quiz from command line, you need to:
# 1. install python coverage library
# 2. run it with command `coverage run --branch q4_code_coverage.py && coverage report && coverage html`
    # 2.1 `--branch` checks branch coverage (by default it checks only statement coverage)
    # 2.2 `report` shows report in the console output
    # 2.3 `html` generates html report, you need to locate the report file and open it with a browser


# Enhanced Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = {}

    def __str__(self):
        return str(self.data)

    def clear(self):       
        self.__init__(self.max)

    def empty(self):       
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if type(x) is not int and type(x) is not str and type(x) is not bool:
            return False
        if self.size == self.max:
            return False
        
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:           
            self.tail = 0
        return True

    def enqueueall(self, c):
        if type(c) is tuple or type(c) is list:
            if not self.size + len(c) > self.max:
                for itm in c:
                    self.enqueue(itm)
                return True
        return False

    def dequeue(self):
        if self.size == 0:           
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:           
            self.head = 0
        return x 

    def checkRep(self): # pragma: no cover
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

import random

# Provide full statement and parameter value coverage of the Queue class
def test(): # pragma: no cover
    
    # test empty que
    q = Queue(100)
    assert not q.full()
    assert q.empty()
    assert str(q) == '{}'
    q.checkRep()

    # test enque
    q = Queue(3)
    # cannot add not int or not bool or not string
    assert q.enqueue(set()) is False
    rand_int = random.randint(-1e8, 1e8)
    assert q.enqueue(rand_int) is True
    assert q.enqueue(False) is True
    assert q.enqueue('hello') is True
    # cannot enque into full que
    assert q.enqueue(123) is False
    assert q.enqueue(321) is False

    # test deque
    assert q.dequeue() == rand_int
    assert q.dequeue() is False
    assert q.dequeue() == 'hello'
    # cannot deque empty que
    assert q.dequeue() is None
    assert q.dequeue() is None

    # test empty and full
    q = Queue(1)
    q.enqueue(123)
    assert not q.empty()
    assert q.full() is True
    q.dequeue()
    q.dequeue()
    assert q.empty() is True
    assert not q.full()

    # test clear
    q = Queue(100)
    for i in range(100):
        q.enqueue(random.randrange(1e8))

    q.clear()
    assert q.empty() is True
    # refullfill que again
    for i in range(100):
        q.enqueue(random.randrange(1e8))
    assert q.full() is True

    # test string repr
    q = Queue(2)
    q.enqueue(1)
    q.enqueue('hello')
    assert str(q) != '{}'
    assert len(str(q)) > 5

    # test enque all
    listA = [1,2,1,3, True, False, 'foo', 'bar', 'foo']
    listB = tuple(listA)
    
    assert Queue(len(listA)).enqueueall(listA) is True
    assert Queue(len(listB)).enqueueall(listB) is True
    # overfilling
    assert Queue(1).enqueueall(listA) is False
    assert Queue(1).enqueueall(listB) is False
    # trying to enqueall with non-supported type
    assert Queue(2).enqueueall(set([1,2])) is False

    # trying to enqueall when list contains non-supported item
    listC = [set(), 123]
    q = Queue(10)
    assert q.enqueueall(listC) is True
    assert q.dequeue() == 123
    assert q.empty() is True

test()