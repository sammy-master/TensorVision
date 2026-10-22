import time

start = time.time()
total = 0
for i in range(10_000_000):
    total += i
end = time.time()

print(f'Result: {total}')
print(f'Time taken: {end - start:.3f} seconds')