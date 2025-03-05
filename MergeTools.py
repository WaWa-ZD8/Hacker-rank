def merge_the_tools(string, k):
    length = len(string) // k
    for i in range(length):
        sub_s = ""
        for j in range (i*k, (i+1)*k ):
            if string[j] not in sub_s:
                sub_s += string[j]
        print(sub_s)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)