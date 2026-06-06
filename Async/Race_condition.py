import threading
chai_stock = 0

def restock():
    global chai_stock
    for i in range(1000000):
        chai_stock += 1

thread = [threading.Thread(target=restock) for _ in range(10)]


