import os
import sys
sys.path(os.getcwd()+sys.path)

import unittest

from board import Board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 9)

    def tearDown(self):
        pass


    def testBoardCanInit(self):
        self.assertEquals("""B B B W W
B B W W W
B B B W W
B B W W W
B B E W W
B B W W W
B B B W W
B B W W W
B B B W W
""", str(self.board))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()