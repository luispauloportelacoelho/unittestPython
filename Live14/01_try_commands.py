import threading

'#number of active threads'
print(threading.active_count())
print(threading.enumerate()[0].name)
print(threading.enumerate()[1].is_alive())
