import time
SEPARADOR=("*"*20)+"\n"

segundos=int(input("Cantidaddesegundosaesperar:\n"))
time.sleep(segundos)
print(f"Hantranscurrido,porlomenos,{segundos}segundos")
print(SEPARADOR*2)

print("Iniciaremoslamedicióndeunprocesosimulado")

horaInicial=time.time()

for termino in range(10):
    time.sleep(segundos)
    
print("procesosimuladoconcluído!")
duracion=time.time()-horaInicial
print(f"Laduracióndelprocesosimuladofuede{duracion}segundos")


