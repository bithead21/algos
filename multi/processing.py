import multiprocessing as mt
from time import sleep
# lock, queue, pool, pipe, process

"""
Process
"""

def job(num):
    print(f"num is {num}")
    sleep(5)

if __name__ == "__main__" and False:
    procs = []
    for i in range(5):
        p = mt.Process(target=job, args=(i,))
        procs.append(p)
        p.start()
    
    for p in procs:
        p.join()

    print("end main")

"""
Pool
"""

def job_cube(i):
    print(f"[{i}] cube() {i**3}")
    sleep(3)
    return i**3

if __name__=="__main__":
    with mt.Pool(3) as p:
        res = p.map(job_cube, [1,2,3,4,5,6,7,8,9])
        print(res)

