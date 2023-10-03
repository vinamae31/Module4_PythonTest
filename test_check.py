import unittest
def check(x):
    return x>=100

class mytest(unittest.TestCase):

    def test(self):
        self.assertTrue(check(3))

if __name__=='__main__':
    unittest.main()