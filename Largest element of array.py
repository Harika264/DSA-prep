arr = list(map(int, input().split()))

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest:", largest)
