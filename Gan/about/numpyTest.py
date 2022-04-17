import numpy as np

results_1 = np.linspace(-1, 1, 5)
# print(results_1)
# [-1.  -0.5  0.   0.5  1. ]

results_2 = [np.linspace(1, 5, 5) for _ in range(3)]
# print(results_2)
# [array([1., 2., 3., 4., 5.]), array([1., 2., 3., 4., 5.]), array([1., 2., 3., 4., 5.])]

results_3 = np.vstack(results_2)
# print(results_3)
# [[1. 2. 3. 4. 5.]
#  [1. 2. 3. 4. 5.]
#  [1. 2. 3. 4. 5.]]

results_4 = np.random.uniform(1, 2, 5)
# print(results_4)
# [1.76288464 1.57597623 1.63463408 1.92633976 1.19121049]

results_5 = results_4[:, np.newaxis]
# print(results_5)
# [[1.76288464]
#  [1.57597623]
#  [1.63463408]
#  [1.92633976]
#  [1.19121049]]

results_6 = np.power(results_1, 2)
# print(results_6)
# [1.   0.25 0.   0.25 1.  ]