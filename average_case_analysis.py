from insertion_sort import insertion_sort
import random
import time

def average_case_analysis():
    for size in [100, 200, 400, 800]:
        times = []
        for _ in range(5):
            arr = random.sample(range(size), size)
            start = time.time()
            insertion_sort(arr)
            end = time.time()
            times.append(end - start)
        avg_time = sum(times) / len(times)
        print(f"Average time for size {size}: {avg_time:.6f} seconds")

if __name__ == "__main__":
    average_case_analysis()
