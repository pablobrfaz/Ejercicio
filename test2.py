# import the python testing framework
import unittest    

# initialized by creating a class that inherits from unittest.testCase 
class IsEven(unittest.TestCase):
    def testOne(self):
        lista1=["MO10: 00-12: 00"]
        lista2=["MO10: 00-12: 00"]
        comparacion = []
        for item in lista1:
            if item in lista2:
                comparacion.append(item)

        if len(comparacion) > 0:
            print ('Ambas listas contienen estos elementos')
            for item in comparacion: print( '%s' % item)
        else:
            print ('No existe ningun elemento igual en las listas')
        self.assertEqual(lista1,lista2)

if __name__ == '__main__':
    unittest.main() # this runs our tests



