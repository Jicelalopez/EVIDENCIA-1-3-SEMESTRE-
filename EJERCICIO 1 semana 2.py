import math
SEPARADOR=("*"* 20)+"\n"
'''
Ejemplo para ilustrar la importación de la librería math en Python 3 Demuestra el uso de: floor(x),trunc(x),ceil(x),round(x),factorial(x),pow(x,y),sqrt(x)y pi
'''

valorFlotante= float(input("Introduceunvalorconfraccióndecimal:\n"))
print(f"Elsiguienteenterohaciaarribade{valorFlotante}es{math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"Elsiguienteenterohaciaabajode{valorFlotante}es{math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"Laparteenteratruncadade{valorFlotante}es{math.trunc(valorFlotante)}")
print(SEPARADOR*2)
pass