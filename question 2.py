import time
import random
import matplotlib.pyplot as plt

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


def binarySearch(arr, low, high, target):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def find_pairs(S, sum):
    S = mergeSort(S)
    pairs = []
    for i in range(len(S)):
        complement = sum - S[i]
        if binarySearch(S, i + 1, len(S) - 1, complement):
            pairs.append((S[i], complement))
    return pairs


# Experiment
power_sizes = [10**i for i in range(7)]
running_times = []

for n in power_sizes:
    S = [random.randint(1, 100) for _ in range(n)]
    target_sum = random.randint(1, 100)
    
    start_time = time.time()
    pairs = find_pairs(S, target_sum)
    end_time = time.time()
    
    running_times.append(end_time - start_time)


plt.plot(power_sizes, running_times, marker='o')
plt.xlabel('Power Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Experimental Results of Algorithm Scalability')
plt.xscale('log')
plt.yscale('log')
plt.show()