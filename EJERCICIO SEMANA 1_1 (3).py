Ejercicio Random
import random

SEPARADOR=("*"*20)+"\n"
print(f"Obteniendounnumeroenteroaleatorioquepuedeirdel0al19:{random.randrange(20)}")print(SEPARADOR)
print(f"Obteniendounnumeroenteroaleatorioparquepuedeirdel2al20:{random.randrange(2,21,2)}")
print(SEPARADOR)
print(f"Obteniendounvalornuméricoentre0.0y1.0:{random.random()}")
print(SEPARADOR*2)

listaDePrueba=[10,20,30,40,15,25,35,45]
print(f"Lalistadepruebaes{listaDePrueba}")
print(f"Elvalorseleeccionadoaleatoriamentedelalistaanteriores{random.choice(listaDePrueba)}")
print(SEPARADOR)
random.shuffle(listaDePrueba)
print(f"Lalistaya'perturbada/barajada'es{listaDePrueba}")

