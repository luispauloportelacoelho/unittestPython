import threading
from time import sleep

'''
#Situation 1
def wait():
    count = 0
    while True:
        print(count)
        count += 1
        sleep(0.1)
        t = threading.Thread(target=wait, name="Wait", daemon=True)
        t.start()
        print(threading.enumerate()[1].is_alive())
        sleep(1)
        print(t.is_alive())
        '''

'''
#Situation 2
def wait():
    sleep(2)


t1 = threading.Thread(target=wait, name="Wait", daemon=True)
t1.start()
print(t1.is_alive())
print(t1.name)

t2 = threading.Thread(target=wait, name="Wait")
t2.start()
print(t2.is_alive())
print(t2.name)
'''


def wait():
    sleep(2)


class myThread(threading.Thread):
    def __init__(self, target, name='mythread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = myThread(wait)

t.start()
print(t.name)
