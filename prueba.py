# importar el marco de prueba de Python
import unittest    



# esto es lo que estamos ejecutando nuestra prueba en 
def isEven(n):
    lista1=["RENE","MO10: 00-12: 00","TU10: 00-12: 00", "TH01: 00-03: 00", "SA14: 00-18: 00", "SU20: 00- 21: 00"]
    lista2=["ASTRID","MO10: 00-12: 00","TH12: 00-14: 00","SU20: 00-21: 00"]
    comparacion = []
    for item in lista1:
        if item in lista2:
            comparacion.append(item)

    if len(comparacion) > 0:
        print ('Ambas listas contienen estos elementos')
        for item in comparacion: print( '%s' % item)
    else:
        print ('No existe ningun elemento igual en las listas')
# nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class IsEvenTests(unittest.TestCase):
    assertAlmostEqual()
    # cada método en esta clase es una prueba que se ejecutará 

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas



