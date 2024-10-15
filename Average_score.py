"Average score"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
List_ = sorted(students, key=str.lower) # функцию взял из рунета
grades_student_1 = sum(grades[0])/len(grades[0])
grades_student_2 = sum(grades[1])/len(grades[1])
grades_student_3 = sum(grades[2])/len(grades[2])
grades_student_4 = sum(grades[3])/len(grades[3])
grades_student_5 = sum(grades[4])/len(grades[4])
average_results = {List_[0] : grades_student_1 , List_[1] : grades_student_2 , List_[2] : grades_student_3, List_[3] : grades_student_4, List_[4] : grades_student_5}
print(average_results)