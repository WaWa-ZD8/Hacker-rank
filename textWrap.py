import textwrap
    
def wrap(string, max_width):
    wrapped_list = textwrap.fill(string, max_width)
    
    return wrapped_list
        
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

