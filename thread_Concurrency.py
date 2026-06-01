import threading
import time

def take_orders():
    for i in range(5):
        print("taking orders")
        time.sleep(2)   

def prepare_food():
    for i in range(5):
        print("preparing food")
        time.sleep(3)

#creating threads
t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=prepare_food)

#starting threads
t1.start()
t2.start()

print("Main thread is running")
t1.join()   
t2.join()
print("All threads have finished")

