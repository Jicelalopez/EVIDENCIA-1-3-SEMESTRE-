import time
SEPARADOR=("*"*20)+"\n"

segundos=int(input("Cantidaddesegundosaesperar:\n"))
time.sleep(segundos)
print(f"Hantranscurrido,porlomenos,{segundos}segundos")
print(SEPARADOR*2)

print("Iniciaremoslamedici√≥ndeunprocesosimulado")

horaInicial=time.time()

for termino in range(10):
    time.sleep(segundos)
    
print("procesosimuladoconclu√≠do!")
duracion=time.time()-horaInicial
print(f"Laduraci√≥ndelprocesosimuladofuede{duracion}segundos")


