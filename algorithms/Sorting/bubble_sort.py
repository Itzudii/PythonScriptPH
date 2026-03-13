from typing import Tuple,List

def bubblesort(a:list,size:int) -> Tuple[List[int],int]:
    step = 0
    isSwap = False
    while isSwap:
        for i in range(size-1): 
            if a[i] > a[i+1]:   
                a[i],a[i+1] = a[i+1],a[i]
                isSwap = True
            step+=1
        
    return a,step

    
if __name__ == '__main__':
    
    import numpy as np
    import time as t
    a = list(range(1,100))
    np.random.shuffle(a)
    size = len(a)
    t0 = t.time()
    sorted_array,steps = bubblesort(a,size)
    t1 = t.time()
    print("Sorted array:", sorted_array)
    print("Total comparisons:", steps)
    print("Execution time (s):", round(t1 - t0, 6))