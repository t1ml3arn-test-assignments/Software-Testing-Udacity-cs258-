# TASK:
#
# This is the SplayTree code we saw earlier in the 
# unit. We didn't achieve full statement coverage 
# during the unit, but we will now!
# Your task is to achieve full statement coverage 
# on the SplayTree class. 
# 
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

import unittest
from splaytree import SplayTree, Node

class SplayTreeTest(unittest.TestCase):
    
    # Write test code in this function to achieve 
    # full statement coverage on the SplayTree class.
    def test(self):
        value = 5
        t = SplayTree()
        # test empty
        assert t.isEmpty()
        # we cannot splay if tree is empty
        assert t.splay(None) is None
        # we cannot find anything in empty tree
        assert t.find(1) is None
        assert t.findMin() is None
        assert t.findMax() is None
        # cannot remove from empty
        assert t.remove(123) is None

        # insert into empty tree
        t.insert(value)
        assert not t.isEmpty()

        # insert into non-empty tree same value
        t.insert(value)
        assert not t.isEmpty()

        # insert different values
        t = SplayTree()
        t.insert(3)
        t.insert(5)
        t.insert(1)

        assert t.findMin() == 1
        assert t.findMax() == 5
        assert t.find(3) == 3
        assert t.find(10) is None
        
        t = SplayTree()
        t.insert(5)
        t.insert(3)
        t.insert(1)
        assert t.find(3) == 3
        assert t.findMin() == 1

        # test remove
        t = SplayTree()
        t.insert(5)
        t.insert(3)
        t.insert(1)
        t.remove(5)
        t.remove(3)
        t.remove(1)
        assert t.isEmpty()

        # test Node.equals()
        n1 = Node(3)
        n2 = Node(2+1)
        n3 = Node(1)
        assert n1.equals(n2)
        assert not n1.equals(n3)

        t = SplayTree()
        t.insert(7)
        t.insert(3)
        t.insert(7)
        assert t.find(7) == 7

        # lets do som RANGE testing !
        max = 1000
        min = 100
        t = SplayTree()
        t.insert(min)
        t.insert(max)

        for i in range(101, 999, 10):
            t.insert(i)
            assert t.find(i) == i
            assert t.findMin() == min
            assert t.findMax() == max


if __name__ == '__main__':
    unittest.main()        