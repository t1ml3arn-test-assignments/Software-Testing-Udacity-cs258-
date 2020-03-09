# Regression Testing
# ------------------
# The goal of this problem is for you to write a regression tester
# for the Queue class.
# 
# Begin by finding and fixing all of the bugs in the Queue class. Next,
# define the function regression_test to take in a list of enqueue inputs
# and dequeue indicators (the returned list of the previous problem) and
# repeat those method calls using the fixed Queue.
# 
# That is, after fixing the Queue class, create a new Queue instance,
# and call the method corresponding to the indicator in the list
# for each item in the list:
# 
# Call the enqueue function whenever you come across an integer, using that
#     integer as the argument.
# Call the dequeue function whenever you come across the 'dq' indicator.

import array
import random
from q2_random_testing import random_test

# Fix this Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):            
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self
                    .size==0) or (self.size==self.max)


# An example list of enqueue integers and dequeue indicators
inpts = [(574, 0), ('dq', 0), (991, 0), ('dq', 0), ('dq', 1),
         (731, 0), (97, 0), ('dq', 0), (116, 0), ('dq', 0),
         (464, 0), (723, 0), (51, 0), ('dq', 0), (553, 0),
         (390, 0), ('dq', 0), (165, 0), (952, 0), ('dq', 0),
         ('dq', 0), (586, 0), (894, 0), ('dq', 0), ('dq', 0),
         (125, 0), (802, 0), (963, 0), (370, 0), ('dq', 0),
         ('dq', 0), (467, 0), (274, 0), ('dq', 0), (737, 0),
         (665, 0), (996, 0), (604, 0), (354, 0), ('dq', 0),
         (415, 0), ('dq', 0), ('dq', 0), ('dq', 0), ('dq', 0),
         ('dq', 0), (588, 0), (702, 0), ('dq', 0), ('dq', 0),
         (887, 0), ('dq', 0), (286, 0), (493, 0), (105, 0),
         ('dq', 0), (942, 0), ('dq', 0), (167, 0), (88, 0),
         ('dq', 0), (145, 0), ('dq', 0), (776, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), ('dq', 0), (67, 0), ('dq', 0),
         ('dq', 0), (367, 0), ('dq', 0), (429, 0), (996, 0),
         (508, 0), ('dq', 0), ('dq', 0), (295, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), (997, 0), ('dq', 0), (29, 0),
         (669, 0), ('dq', 0), (911, 0), ('dq', 0), ('dq', 0),
         (690, 0), (169, 0), (730, 0), (172, 0), (161, 0),
         (966, 0), ('dq', 0), (865, 0), ('dq', 0), (348, 0)]

# my inouts obtained from the Que with length of 50 item
# and 100 operations 
my_inputs = [
    ('dq', 1), (589371, 0), (-268695, 0), (541886, 0), ('dq', 0), ('dq', 0), 
    ('dq', 1), (405079, 0), ('dq', 1), (-531150, 0), ('dq', 1), ('dq', 1), ('dq', 1), 
    (513909, 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), (787863, 1), ('dq', 1), ('dq', 1),
    ('dq', 1), ('dq', 1), (-537996, 1), (360105, 1), ('dq', 1), ('dq', 1), (-428190, 1), 
    ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), (79258, 1), (-727158, 1), ('dq', 1), 
    (481463, 1), (843062, 1), ('dq', 1), (-517396, 1), (-493170, 1), ('dq', 1), ('dq', 1), 
    ('dq', 1), ('dq', 1), ('dq', 1), (-438600, 1), ('dq', 1), (-686404, 1), ('dq', 1), (-497777, 1), 
    (-652995, 1), (-125500, 1), (-957709, 1), ('dq', 1), (610185, 1), ('dq', 1), ('dq', 1), ('dq', 1), 
    ('dq', 1), (-457845, 1), ('dq', 1), ('dq', 1), ('dq', 1), (766622, 1), ('dq', 1), ('dq', 1), 
    ('dq', 1), ('dq', 1), ('dq', 1), (-373429, 1), (-981290, 1), ('dq', 1), (986708, 1), (772179, 1), 
    ('dq', 1), ('dq', 1), ('dq', 1), (797734, 1), (-157925, 1), ('dq', 1), (346080, 1), (-935440, 1), 
    ('dq', 1), (110349, 1), (953659, 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), 
    ('dq', 1), ('dq', 1), (-322941, 1), ('dq', 1), ('dq', 1), ('dq', 1), (605476, 1), (-509184, 1), 
    (477142, 1), ('dq', 1)
]

# Write a regression tester for the Queue class
def regression_test(inputlist):

    q = Queue(100)

    for data,result in inputlist:
        if data == 'dq':
            q.dequeue()
            q.checkRep()
        else:
            q.enqueue(data)
            q.checkRep()

# getting a fresh random testing results
random_results = random_test()
# print('RADNOM TESTING RESULTS:')
# print(random_results)
regression_test(random_results)
regression_test(inpts)
regression_test(my_inputs)

# Some notes about this QUIZ
# 1. It is bad. Udacity accepted WRONG answer when Que is actually not fixed properly.
#   I guess it is designed in that way. Since QUIZ 2 focused only on push/pop and checkRep() cals
#   so it is not possible to detect inverse call problem (when push(item), then pop() and pop() result != initial item)