from insertion_sort import insertion_sort

def insertion_sort_stable(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    data = [(2, 'A'), (1, 'B'), (2, 'C'), (1, 'D')]
    sorted_data = insertion_sort_stable(data)
    print("Before sorting:", data)
    print("After sorting: ", sorted_data)
