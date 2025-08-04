
MIN_AGE = 21
MIN_INCOME = 25000  
MIN_CREDIT_SCORE = 700

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))

if age >= MIN_AGE:
    if income >= MIN_INCOME:
        if credit_score >= MIN_CREDIT_SCORE:
            print("Loan approved.")
        else:
            print("Rejected: Low credit score.")
    else:
        if credit_score >= MIN_CREDIT_SCORE:
            print("Rejected: Low income.")
        else:
            print("Rejected: Low income and credit score.")
else:
    if income >= MIN_INCOME:
        if credit_score >= MIN_CREDIT_SCORE:
            print("Rejected: Age below minimum.")
        else:
            print("Rejected: Age and credit score too low.")
    else:
        if credit_score >= MIN_CREDIT_SCORE:
            print("Rejected: Age and income too low.")
        else:
            print("Rejected: Age, income, and credit score too low.")
