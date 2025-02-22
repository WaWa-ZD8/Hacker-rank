if __name__ == '__main__':
    N = int(input())
    arr =[]
    big_arr = []
    
    for _ in range(N):
        command, *numbers = input().split()
        inputs = list(map(int,numbers))
        if command == "append":
            arr.append(inputs[0])
        elif command == "insert":
            arr.insert(inputs[0],inputs[1])
        elif command == "remove":
            arr.remove(inputs[0])
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()
        if command == "print":
            big_arr.append(arr[:])
            
    for i in big_arr:
            print(i)
        
        
    

    
        
                
        
   

    


    