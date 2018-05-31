from threading import Thread, Lock
c = 0
lock = Lock()

def count_30000():
    global c
    lock.aquire()
    try:
        while c < 30000:
            c += 1
        print(c)
    finally:
        lock.release()


def count_100000():
    global c
    c = 340
    while c < 100000:
        c += 1
    print(c)


t_0 = Thread(target=count_30000, name='30000', daemon=True)

t_1 = Thread(target=count_100000, name='100000', daemon=True)

t_1.start()
t_0.start()
