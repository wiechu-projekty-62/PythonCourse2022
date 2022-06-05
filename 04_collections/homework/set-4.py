import numpy as np
listainput = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
splits = np.array_split(listainput, 3)
for array in splits:
    x = list(array)
    x.reverse()
    print(x)


