import time
import numpy as np

N = 1_000_000


start = time.time()
python_list = [i ** 2 for i in range(N)]
py_time = time.time() - start


start = time.time()
numpy_arr = np.arange(N) ** 2
np_time = time.time() - start

print(f"Python loop time: {py_time:.5f} s")
print(f"NumPy vectorization time: {np_time:.5f} s")
print(f"Speedup ratio: {py_time / np_time:.2f}x")