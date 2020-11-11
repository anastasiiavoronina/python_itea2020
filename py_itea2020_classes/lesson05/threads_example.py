from threading import Thread
import time

def io_bound(id_, sec):
    print(f'{id_} fell asleep')
    time.sleep(sec)
    print(f'{id_} woke up')

# start = time.time()
# io_bound(1, 1)
# io_bound(2, 2)
# io_bound(3, 3)
# print(time.time() - start)

start = time.time()
t1 = Thread(target=io_bound, args=(1, 1), name='Thread-One', daemon=True)
t2 = Thread(target=io_bound, args=(2, 2), name='Thread-Two', daemon=True)
t3 = Thread(target=io_bound, args=(3, 3), name='Thread-Three', daemon=True)
print(t1.getName(), t2.getName(), t3.getName())
print(t1.is_alive())
t1.start()
print(t1.is_alive())
t2.start()
t3.setDaemon(False)
t3.start()

# t1.join()
# t2.join()
# t3.join()
# print(time.time() - start)
#
# for i in range(5):
#     print('Hello world')

