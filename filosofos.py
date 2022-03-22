import threading

def left(i):
    return i

def right(i):
    return (i+1)%5

def think(i):
    print('el filosofo', i, 'esta pensando')

def eat(i):
    print('el filosofo', i, 'esta comiendo')


def get_forks(i):
    
        (forks[left(i)]).acquire()
        (forks[right(i)]).acquire()

def put_forks(i):
      (forks[left(i)]).release()
      (forks[right(i)]).release()   

def filosofo(i):
    
    while 1:
        think(i)
        get_forks(i)
        eat(i)
        put_forks(i)
        break
        

forks = list()
for i in range(5):
    fork = threading.Semaphore(1)
    forks.append(fork)

threads = list()
for i in range(5):
    p = threading.Thread(target = filosofo, args=(i,))
    p.start()

for p in threads:
    p.join()
