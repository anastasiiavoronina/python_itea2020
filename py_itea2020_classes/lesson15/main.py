from concurrent.futures import ThreadPoolExecutor
import time

def sleeper(id_):
    print(f'{id_} started')
    time.sleep(2)
    print(f'{id_} ended')

pool = ThreadPoolExecutor(max_workers=3)

futures = []
for i in range(1, 13, 1):
    futures.append(pool.submit(sleeper, i))

for f in futures:
    f.result()

