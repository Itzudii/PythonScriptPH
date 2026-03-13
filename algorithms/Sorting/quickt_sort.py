
from typing import Tuple,List

def partition(arr:List[int],low:int,high:int):
    pivot = arr[high]
    swapi = low
    for k in range(low,high):
        if arr[k] <= pivot:
            arr[k],arr[swapi] = arr[swapi],arr[k]
            swapi+=1
    arr[high],arr[swapi] = arr[swapi],arr[high]
    return swapi


def quicksort(arr:List[int],low:int,high:int):
    if low < high:
        index = partition(arr,low,high)
        quicksort(arr,low,index-1)
        quicksort(arr,index,high)



if __name__ == '__main__':
    import numpy as np
    a = list(range(1,100))
    np.random.shuffle(a)
    size = len(a)
    import time as t
    t0 = t.time()
    quicksort(a,0,len(a)-1)
    t1 = t.time()
    print("Sorted array:", a)
    print("Execution time (s):", round(t1 - t0, 6))