import threading
import time
def io_task():
    time.sleep(1)
    print("I/O-bound task completed.")

    threads = [threading.Thread(target=io_task) for _ in range(5)]   #list comprehension (used when loop variable name is not needed)

    for t in threads:
        t.start()
    for t in threads:
        t.join()