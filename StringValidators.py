if __name__ == '__main__':
    s = input()
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_upper = False
for i in s:
    if i.isalnum():
        is_alnum = True
    if i.isalpha():
        is_alpha = True
    if i.isdigit():
        is_digit = True
    if i.islower():
        is_lower = True
    if i.isupper():
        is_upper = True
print(is_alnum)
print(is_alpha)
print(is_digit)
print(is_lower)
print(is_upper)
    
        
    