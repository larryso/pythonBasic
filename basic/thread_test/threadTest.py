import threading
import time

thread_lock = threading.RLock()

def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


class MyThread(threading.Thread):
    __threadName = ""
    __threadId = 0
    __counter = 0

    def __init__(self, threadId, threadName, counter):
        threading.Thread.__init__(self)
        self.__threadId = threadId
        self.__threadName = threadName
        self.__counter = counter

    def run(self):
        print(f"Starting thread - {self.__threadName}")
        thread_lock.acquire()
        print_time(self.__threadName, 10, self.__counter)
        thread_lock.release()
