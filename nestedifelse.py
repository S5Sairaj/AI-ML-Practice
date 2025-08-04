




exam_score = int(input("Enter exam score: "))
attendance = int(input("Enter attendance percentage: "))

if attendance < 75:
    if exam_score < 50:
        print("You Fail due to both low attendance and low exam score")
    else:
        print("You Fail due to low attendance")
else:
    if exam_score < 50:
        print("You Fail due to low exam score")
    else:
        print("You Pass the exam")
