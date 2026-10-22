import numpy as np
import time

SIZE = 10_000_000  # 10 million numbers

# ── Method 1: Pure Python loop ──────────────────────────
data_list = list(range(SIZE))

start = time.time()
result = [x * 2 for x in data_list]
python_time = time.time() - start

print(f"Python loop  : {python_time:.4f} seconds")

# ── Method 2: NumPy vectorized ──────────────────────────
data_array = np.arange(SIZE)

start = time.time()
result = data_array * 2
numpy_time = time.time() - start

print(f"NumPy        : {numpy_time:.4f} seconds")

# ── Speedup ─────────────────────────────────────────────
print(f"\nNumPy is {python_time / numpy_time:.1f}x faster than Python loop")