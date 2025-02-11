# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     arr.sort()
    
#     for i in range(n):
#         if arr[i] < arr[n-1]:
#             runner_up = arr[i]
#     print(runner_up)
        
        
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))

    arr.sort()

    print(arr[len(arr)-2])