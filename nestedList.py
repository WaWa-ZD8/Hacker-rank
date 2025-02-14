if __name__ == '__main__':
    students = []
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    sort_score = sorted(set(score for _, score in students))      
    second_lowest_grade = sort_score[1]  
    second_lowest_student = sorted([name for name, score in students if score == second_lowest_grade])
        
print(students)  
print( sort_score)
print (second_lowest_student)



    



    