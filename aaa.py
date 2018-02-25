import time

# 为线程定义一个函数
# from concurrent.futures import thread
import _thread

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

# 创建两个线程
try:
    thread.start_new_thread(print_time, ())
    _thread.start_new_thread(print_time, ())
except:
    print("Error: unable to start thread")
