#! /usr/bin/python
import numpy as np
a = np.asarray([10,22,33,56,67,2])
b =np.reshape(a,[1,6])
print("len",len(b[0]))
print(b[0])
similarities=""
for i in b[0]:
    print(i)
    # similarities = similarities+str(pow(b[0][i], 0.5))+"  "
print(similarities)

