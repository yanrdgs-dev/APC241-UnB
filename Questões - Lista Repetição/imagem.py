# Questão 19
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, split_inv = merge(left, right)
    inversions = left_inv + right_inv + split_inv
    return merged, inversions

def merge(left, right):
    merged = []
    split_inversions = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, split_inversions

datagramas = list(map(int, input().strip().split()))

_, inversions = merge_sort(datagramas)
print(inversions)
