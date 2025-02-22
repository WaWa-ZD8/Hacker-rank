height, legnth = map(int, input().split())
word = "WELCOME"
dot_stick = ".|."

# top
for i in range((height-1)//2):
    print ((dot_stick*i).rjust((legnth-3)//2,"-")+dot_stick+(dot_stick*i).ljust((legnth-3)//2,"-"))

# middle WELCOME
print (word.center(legnth,"-"))

# bottom
for i in range((height-1)//2):
    print((dot_stick*(((height-1)//2-i-1))).rjust((legnth-3)//2, "-")+dot_stick+(dot_stick*(((height-1)//2-i-1))).ljust((legnth-3)//2,"-"))
    

