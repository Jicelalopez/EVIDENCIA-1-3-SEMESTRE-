import math
SEPARADOR=("*"*20)+"\n"
'''
Ejemploparailustrarlaimportaci√≥ndelalibrer√≠amathenPython3
Demuestraelusode:floor(x),trunc(x),ceil(x),round(x),factorial(x),pow(x,y),sqrt(x)ypi
'''

valorFlotante=float(input("Introduceunvalorconfracci√≥ndecimal:\n"))
print(f"Elsiguienteenterohaciaarribade{valorFlotante}es{math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"Elsiguienteenterohaciaabajode{valorFlotante}es{math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"Laparteenteratruncadade{valorFlotante}es{math.trunc(valorFlotante)}")
print(SEPARADOR*2)
pass