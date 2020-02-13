# TASK:
#
# Achieve full statement coverage on the Queue class. 
# You will need to:
# 1) Write your test code in the test function.
# 2) Press submit. The grader will tell you if you 
#    fail to cover any specific part of the code.
# 3) Update your test function until you cover the 
#    entire code base.
#
# You can also run your code through a code coverage 
# tool on your local machine if you prefer. This is 
# not necessary, however.
# If you have any questions, please don't hesitate 
# to ask in the forums!

from queue import Queue
import unittest

class TestQueueCoverage(unittest.TestCase):

    def test_coverage(self):
        ###Your code here.
        # test emptines
        q = Queue(1)
        assert q.empty()
        # enque should return true
        assert q.enqueue(2)
        assert not q.empty()
        
        q.checkRep()

        # test fullnes
        q = Queue(1)
        assert not q.full()
        q.enqueue(2)
        assert q.full()

        # test enque when q is full
        q = Queue(1)
        q.enqueue(2)
        assert not q.enqueue(3)

        # test deque
        q = Queue(1)
        q.enqueue(2)
        assert q.dequeue() == 2
        assert not q.dequeue()

        # cover checkRep 1
        q = Queue(2)
        q.enqueue(2)
        q.checkRep()

        # cover checkRep 2
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        q.checkRep()

if __name__ == '__main__':
    unittest.main()