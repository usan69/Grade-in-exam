
student_score={"usan" : 95 ,
               "pritom": 80,
               "shibage": 76,
               "riad":62
               }
student_grade={}

for student in student_score:
  score=student_score[student]
  if score>90:
    student_grade[student]="outstanding"
  elif  score>80:
    student_grade[student]="exceeds expectations"
  elif score>70:
    student_grade[student]="acceptable"
  else:
    student_grade[student]="Fail"

print(student_grade)
