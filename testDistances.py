import numpy as np

x = np.random.random(10)
y = np.random.random(10)

print(type(x))
# solution1
dist1 = np.linalg.norm(x - y)

# solution2
dist2 = np.sqrt(np.sum(np.square(x - y)))

print('x', x)
print('y', y)
print('dist1', dist1)
print('dist2', dist2)