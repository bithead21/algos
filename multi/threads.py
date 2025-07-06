import threading
from typing import Callable
from time import sleep
import queue
import urllib.request

shared_val = 0
val_lock = threading.Lock()

# LOCK

# access shared variable with lock and no lock

def work_with_lock(inc_to: int):
    global shared_val
    with val_lock:
        sleep(0.1)
        shared_val += inc_to
        print(f"val now: {shared_val}")

def work_no_lock(inc_to: int):
    global shared_val
    sleep(0.1)
    shared_val += inc_to
    print(f"val now: {shared_val}")

def test_locking(fun: Callable[[int], None]):
    global shared_val
    shared_val = 0
    ts = [threading.Thread(target=fun, args=(1,)) for i in range(0, 30)]

    for t in ts:
        t.start()

    for t in ts:
        t.join()

# SEMAPHORE

# max conn to db

class Db:
    def __init__(self, max_cons):
        self.__max_cons = max_cons
        self.__sema = threading.Semaphore(max_cons)

    def __accept_new(self, client_id):
        print(f"accept ok: {client_id}")
        sleep(2)

    def connect(self, client_id):
        with self.__sema:
            self.__accept_new(client_id)

def test_db_cons():
    db = Db(3)
    
    # run clients parallel
    ts = [threading.Thread(target=db.connect, args=(f"client-{i}-{i&2}", )) for i in range(0, 10)]

    for t in ts:
        t.start()
    for t in ts:
        t.join()

# consumer-producer

buff_size = 5
buffer = queue.Queue(maxsize=buff_size)
items_produced = 10

full = threading.Semaphore(0)
empty = threading.Semaphore(buff_size)

def prod():
    for i in range(items_produced):
        item = f"item-{i}"
        empty.acquire() # 
        buffer.put(item)
        full.release()
        sleep(1)

def cons():
    for _ in range(items_produced):
        full.acquire()
        item = buffer.get()
        print(f"got msg: {item}")
        empty.release()
        sleep(2)

def test_sema():
    s = threading.Semaphore(0)
    s.acquire()
    print("Ac")
    s.release()
    print("Rel")

# EVENT

e = threading.Event()

def patcher():
    print("patcher wait")
    e.wait()
    print("patcher got signal")

def invoker():
    sleep(2)
    print("invoker send signall")
    e.set()

# TESTS

def foo():
    sleep(5)
    print("foo...")
    

def bar():
    sleep(2)
    print("bar...")
    

# URL PATCHER

import urllib

urls = ["https://python.org", "https://example.com"]

def fetch_url(url):
    resp = urllib.request.urlopen(url)
    print(f"[{url}]: resp_len={len(resp.read())}")

def fetch_all():
    ts = [threading.Thread(target=fetch_url, args=(urls[i], )) for i in range(0, len(urls))]
    for t in ts: t.start()
    for t in ts: t.join()


# BACKGROUND LOGGING (daemon thread)
def backlog(logs: list):
    while(True):
        if (logs):
            print(logs)
            logs.clear()
            sleep(0.5)

def core():
    logs = []
    bg = threading.Thread(target=backlog, args=(logs,), daemon=True)
    bg.start()
    for  i in range(0, 10):
        sleep(0.1)
        logs.append(f"log--{i}")
    
    print("core finished.")

core()

print("gyper end")
