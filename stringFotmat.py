def print_formatted(number):
    max_width = len(bin(number)[2:])
    for i in range(1,number+1):
        answer = "{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(i, w=max_width)
        
        print(answer)
    print(bin(number))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


