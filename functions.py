import threading
import time
''''def timemaker():
    print('Haciendo tiempo...')
    time.sleep(2) #segundos
    print('Tiempo hecho...')
to = time.time()
lista_hilos=[]
for i in range(4):
    t = threading.Thread(target = timemaker)
    lista_hilos.append( t )
    t.start()
for t in lista_hilos:
    t.join()
tf = time.time() - to
print(f'Tiempo total de ejecución: {tf}')'''
def contador(inicio,fin):
    arrayNum = []
    for i in range(inicio,fin+1, 1):
        arrayNum.append( i )
        time.sleep(0.01)
    return arrayNum
t0 = time.time()
lista_numeros = contador(1,100)
ft = time.time()-t0
#---------------------------------------------------------------------------
global_arrayNum =[]
def contador2(inicio,fin):
    for i in range(inicio,fin+1, 1):
        global_arrayNum.append( i )
        time.sleep(0.01)
    return 0

t0 = time.time()
lista_hilos =[]
t = threading.Thread(target=contador2, args=(100/4))
lista_hilos.append(t)
t.start()
for i in lista_hilos:
    t.join()
tf = time.time()-t0
global_arrayNum.sort()