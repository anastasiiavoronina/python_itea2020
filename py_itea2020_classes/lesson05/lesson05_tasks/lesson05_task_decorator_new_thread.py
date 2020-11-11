from threading import Thread
import time


def new_thread_decorator(thread_name, thread_is_daemon):

    def actual_decorator(func):

        def wrapper(sec, name):
            t1 = Thread(target=func, args=(sec, name), name=thread_name, daemon=thread_is_daemon)
            t1.start()

        return wrapper

    return actual_decorator


@new_thread_decorator('Thread A', False)
def target_function(sec, name):
    print(f'{name} is falling asleep for {sec} sec')
    time.sleep(sec)
    print(f'{name} is waking up after {sec} sec')


for i in range(1,5):
    target_function(sec=i, name=i)