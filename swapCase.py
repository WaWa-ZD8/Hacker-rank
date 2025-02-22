

def swap_case(s):
    swaped = ""
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ./\"":
            swaped += i.lower()
        elif i in "abcdefghijklmnopqrstuvwxyz ./\"":
            swaped += i.upper()
        else:
            swaped += i
    
    return swaped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

