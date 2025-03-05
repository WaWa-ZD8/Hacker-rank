from itertools import product
def tuple_output(li_A, li_B):
        tupels_to_string = ""
        groups = list(product(li_A, li_B))
        for i in groups:
                tupels_to_string += str(i)+ " "
          
        print(tupels_to_string)
                
        
if __name__ == '__main__':
    li_A = list(map(int, input().split()))
    li_B = list(map(int, input().split())) 
    tuple_output(li_A, li_B)