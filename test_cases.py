from insertion_sort import insertion_sort
import random
import time

def test_sorting():
    test_arrays = {
        "small_array": [3, 1, 4, 2],
        "large_array": random.sample(range(1000), 1000),
        "nearly_sorted": list(range(1, 1000)) + [0],
        "reversed_array": list(range(999, -1, -1))
    }

    for name, arr in test_arrays.items():
        arr_copy = arr.copy()
        start = time.time()
        sorted_arr = insertion_sort(arr_copy)
        end = time.time()
        print(f"{name} sorted correctly: {sorted_arr == sorted(arr)} in {end - start:.6f} seconds")

if __name__ == "__main__":
    test_sorting()
