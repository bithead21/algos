#from numpy import *
import numpy as np
import threading 

"""
mul(Ad, Bd)
decomp(A)
mul(A, B)

1) 
in: quadratic matrix with size n (n is even)
декопозировать матрицу на квадратные 2x2 блоки, заполнить константой 
выполнить асинхронно
"""

C = -1

"""
TODO
max_parallel_blocks
"""

# calculating 2x2 block, like [0,0] to [1,1]
def mul_block(arr: np.ndarray, ij_from, ij_to):
    # [0, 0]
    # [0, 1]
    # [1, 0]
    # [1, 1]
    arr[ij_from] = C
    arr[ij_from + [0, 1]] = C
    arr[ij_from + [1, 0]] = C
    arr[ij_from + [1, 1]] = C


def decomp(arr: np.ndarray, debug: bool = True):
    
    """
    alg: собираем блоки 2x2 слева направо 
    """

    # check size is even
    if (len(arr) % 2 != 0 or len(arr[0]) % 2 != 0):
        print("wrong size")
        return
    
    ij = np.array([0, 0])
    ij_end = np.array([len(arr), len(arr[0])])

    # parallel threads
    parallel_blocks = []

    while(ij[0] < ij_end[0] or ij[1] < ij_end[1]):
        # calculate block diagonal indecies
        block = np.array([
            ij,
            ij+[1,1]])
        
        # здесь можем создать параллельную задачу на умножение двух блоков
        tr = threading.Thread(target=mul_block, args=(arr, block[0], block[1]))
        tr.start()
        parallel_blocks.append(tr)

        # go left
        ij += [0, 2]

        # end of line
        if (ij[1] >= ij_end[1]):
            ij = np.array([ij[0]+2, 0]) # go down on two elems

        # global end
        if (ij[0] >= ij_end[0]):
            break
    
    for t in parallel_blocks:
        t.join()

    if (debug):
        print(f"decomp() finished, num_blocks={len(parallel_blocks)}.")


arr = np.array([[1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6],
                [1, 2, 3, 4, 5, 6]])
#print(arr)
decomp(arr)

print(arr)

# [[1 2 3]
#  [4 5 6]]




