import time

swaps, comparisons = 0, 0


def quicksort(arr, left, right, order: bool):
    if order == 0:
        if left < right:
            partition_pos = partition_asc(arr, left, right)
            quicksort(arr, left, partition_pos - 1, False)
            quicksort(arr, partition_pos + 1, right, False)
    if order == 1:
        if left < right:
            partition_pos = partition_desc(arr, left, right)
            quicksort(arr, left, partition_pos - 1, True)
            quicksort(arr, partition_pos + 1, right, True)


def partition_asc(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    global swaps, comparisons

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            comparisons += 1
        while j > left and arr[j] >= pivot:
            j -= 1
            comparisons += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            comparisons += 1

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        swaps += 1
        comparisons += 1

    return i


def partition_desc(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    global swaps, comparisons

    while i < j:
        while i < right and arr[i] > pivot:
            i += 1
            comparisons += 1
        while j > left and arr[j] <= pivot:
            j -= 1
            comparisons += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
            comparisons += 1

    if arr[i] < pivot:
        arr[i], arr[right] = arr[right], arr[i]
        swaps += 1
        comparisons += 1

    return i


if __name__ == '__main__':
    print('Array: ')
    arr = list(map(int, input().split()))
    print('ASC/DESC: ')
    order = input()
    print('\nQuickSort')

    if order == 'ASC':
        start_time = time.perf_counter()
        quicksort(arr, 0, len(arr) - 1, False)
        end_time = time.perf_counter()
        print('Execution time:', (end_time - start_time) * 1000, "ms")
        print('Comparisons:', comparisons)
        print('Swaps:', swaps)
        print(*arr)

    if order == 'DESC':
        start_time = time.perf_counter()
        quicksort(arr, 0, len(arr) - 1, True)
        end_time = time.perf_counter()
        print('Execution time:', (end_time - start_time) * 1000, "ms")
        print('Comparisons:', comparisons)
        print('Swaps:', swaps)
        print(*arr)
