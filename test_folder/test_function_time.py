#! /usr/bin/python3
import time

start = time.perf_counter()
for i in range(1000):
	pass

end = time.perf_counter()
print(f"耗时{end - start}秒")
