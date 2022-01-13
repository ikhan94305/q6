def solution(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    while minimum in arr:
        arr.remove(minimum)
    return arr

arr = [4, 3, 1, 2, 1]
answer = solution(arr)
print(answer)
