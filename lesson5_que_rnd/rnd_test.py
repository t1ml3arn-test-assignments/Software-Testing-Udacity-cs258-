# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

from que import Queue
import random
import sys

# print(sys.maxsize)
# print(sys.maxsize < 2e30, sys.maxsize < 2e32, sys.maxsize < 2e28)

# Write a random tester for the Queue class.
def test():
    # what will be good strategy for random tester?
    # What we have:
    # 1. init(que_len)
    # 2. isFull()
    # 3. isEmpty()
    # 4. enque(item)
    # 5. deque()
    # 6. checkRep() !!!
    for i in range(100):
        qlen = random.randint(1, 500)
        q = Queue(qlen)
        q.checkRep()
        check = 0
        for i in range(9999):
            if random.random() < 0.5:
                # NOTE OverflowError: Python int too large to convert to C long
                # if a range (-2e30, 2e30) is in use
                # That's because underneath Queue uses array with 2-byte cells
                res = q.enqueue(random.randrange(-2e8, 2e8))
                if res:
                    check += 1
            else:
                res = q.dequeue()
                if not (res is None):
                    check -= 1
            q.checkRep()
        
        # number of inserted elements cannot be greater than length of the que
        assert check <= qlen
        
        # deque all items from the que
        while check > 0:
            q.dequeue()
            check -= 1
        
        assert q.empty()
        
        q.checkRep()

test()