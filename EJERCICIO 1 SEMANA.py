from multiprocessing import Queue
import random

queue_time=Queue()
print("Almacenando en queue...")
for in range(5)
 random_time=random.randint(1,100)
 queue_time.put(random_time)
 print("%d added at queue"% random_time)
 
 print("Leyendo de queue...")
 While not queue_time.empty()
 print("%d read from queue" %time_read)