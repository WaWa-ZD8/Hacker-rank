if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    res_sum = 0
    for scores in student_marks.values():
        if scores == student_marks[query_name]:
            res_sum = sum(scores)
    average = (res_sum/len(scores))
    
    print(format(average, ".2f"))



