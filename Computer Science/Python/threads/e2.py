import logging
import threading
import time

# 100 Threads each of the summing 1 to a variable with +=
# due to that += is not an atomic operation most of the times
# values are missing, altho I found some weird results like
#
# 12:35:15: Result: 1000000
# 12:35:15: Missing: 0

# 12:41:53: Result: 990000
# 12:41:53: Missing: 10000

# 12:42:45: Result: 987286
# 12:42:45: Missing: 12714

# sometimes looks random, sometimes not so much
# maybe the GIL tries to not stop the thread if its in the
# middle of a operation like += ?
# who knows ¯\_(ツ)_/¯, but still interesting

# using Lock increases the calculation time by a LOT
# probably because of the crazy amount of context switching
# just to sum 1 XD

class Foo:
    def __init__(self):
        self.arr = [0]
        self.times = 10000
        self.lock = False
        self._lock = threading.Lock()

    def sum_one(self):
        if (self.lock):
            with self._lock:
                self.arr[0] += 1
        else:
            self.arr[0] += 1

    def sum_times(self):
        for index in range(self.times):
            self.sum_one()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    foo = Foo()

    threads = list()
    num_threads = 100

    for index in range(num_threads):
        th = threading.Thread(target=foo.sum_times)
        threads.append(th)
        th.start()

    for index, thread in enumerate(threads):
        thread.join()
        logging.info(f'Thread {index} done')

    logging.info(f'Result: {foo.arr[0]}')
    logging.info(f'Missing: {foo.times * num_threads - foo.arr[0]}')
