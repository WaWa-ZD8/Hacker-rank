# def minion_game(string):
#     Stuart = []
#     Kevin = []
#     count_kev = 0
#     count_stu = 0
#     for i in range(len(string)):
#         for j in range(i + 1, len(string) + 1):
#             if string[i:j] not in Stuart and string[i:j][0] not in "AEIOU":
#                 Stuart.append(string[i:j].upper())

#         for j in range(i + 1, len(string) + 1):
#             if string[i:j] not in Kevin and string[i:j][0] in "AEIOU":
#                 Kevin.append(string[i:j].upper())

#     for i in Kevin:
#         for j in range(len(string)):
#             if string[j : j+len(i)]==i:
#                 count_kev+=1
#     for i in Stuart:
#         for j in range(len(string)):
#             if string[j : j+len(i)]==i:
#                 count_stu+=1
    
#     if count_stu > count_kev:
#         print("Stuart "+str(count_stu))
#     elif count_stu < count_kev:
#         print("Kevin "+str(count_kev))
#     else:
#         print("Draw")
def minion_game(string):
    vowels = "AEIOU"
    n = len(string)
    stuart_score = 0
    kevin_score = 0

    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)  
        else:
            stuart_score += (n - i)  

    if stuart_score > kevin_score:
        print(f"Stuart "+str(stuart_score))
    elif kevin_score > stuart_score:
        print(f"Kevin "+str(kevin_score))
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)