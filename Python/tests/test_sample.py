import unittest

def add(a,b):
    return a+b

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        raise ValueError("ddddd")

    
# if __name__ == '__main__':
    # unittest.main()
