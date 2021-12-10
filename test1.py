# import the python testing framework
import unittest    

# this is what we are running our test on 
def isNum(num):
    correcto=False
    while(not correcto):
        try:
            num = int(input("Choose an Option: "))
            correcto=True
        except ValueError:
            print('Error, Enter a correct Option')
    return num

# initialized by creating a class that inherits from unittest.testCase 
class IsNum(unittest.TestCase):
    # each method in this class is a test to be run 
    def testTwo(self):
        self.assertAlmostEqual(isNum(2), 2)

if __name__ == '__main__':
    unittest.main() # this runs our tests



