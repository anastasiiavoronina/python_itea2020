from threading import Thread
import time

class SleepingThread(Thread):

    def __init__(self, seconds, is_daemon=True):
        super().__init__(daemon=is_daemon)
        self._seconds = seconds

    def run(self) -> None:
        print('Sleeping')
        time.sleep(self._seconds)


t1 = SleepingThread(3)
t2 = SleepingThread(3)

t1.start()
t2.start()