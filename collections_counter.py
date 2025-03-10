from collections import Counter
if __name__ == '__main__':

    num_of_shoes = int(input())
    shoe_sizes = list(map(int,input().split()))
    num_of_customers = int(input())
    total = 0
    
    counter_of_sizes = Counter(shoe_sizes)


    for i in range(num_of_customers):
        size, price = list(map(int,input().split()))
        if size in counter_of_sizes.keys() and counter_of_sizes[size] > 0:
            total += price
            counter_of_sizes[size] -= 1
        
    print(total)


    
    
    
    
    
        
    
    


    

             

