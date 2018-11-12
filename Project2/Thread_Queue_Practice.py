import thread
import Queue

def Square(num, Q):
    Q.put(int(num)*int(num))

my_queue = Queue.Queue()

num = 5#int(raw_input())
thread.start_new_thread(
    Square, (num, my_queue))
res = my_queue.get()

print("{} squared is {}".format(num, res))