# arrays_search_sort.py

from typing import List

# --- 1D list basics ---
def average(nums: List[int]) -> float:
    return sum(nums) / len(nums) if nums else 0.0

# --- 2D list (matrix) example ---
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    # Assumes rectangular matrix
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

# --- Linear search (works on unsorted lists) ---
def linear_search(nums: List[int], target: int) -> int:
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1

# --- Binary search (requires sorted list) ---
def binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# --- Bubble sort (simple, O(n^2)) ---
def bubble_sort(nums: List[int]) -> List[int]:
    arr = nums[:]  # copy
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# --- Insertion sort (often faster than bubble for small arrays) ---
def insertion_sort(nums: List[int]) -> List[int]:
    arr = nums[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def demo():
    data = [7, 3, 9, 1, 4, 8]
    print("Data:", data)
    print("Average:", average(data))

    m = [[1, 2, 3],
         [4, 5, 6]]
    print("Matrix:", m)
    print("Transpose:", transpose(m))

    print("Linear search for 9:", linear_search(data, 9))
    print("Bubble sort:", bubble_sort(data))
    sorted_data = insertion_sort(data)
    print("Insertion sort:", sorted_data)
    print("Binary search for 4 in sorted_data:", binary_search(sorted_data, 4))

if __name__ == "__main__":
    demo()
