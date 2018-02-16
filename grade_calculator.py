#adds functions to grade_calculator.py

def main():
    score = float(input('Enter score:'))
    computegrade(score)


def computegrade(score):
    if score > 1 or score <0:
        print('Please enter a valid score')

    else:

        if score >= 0.9:
            grade = 'A'

        elif score >= 0.8:
            grade = 'B'


        elif score >= 0.7:
            grade = 'C'


        elif score >= 0.6:
            grade = 'D'


        else:
            grade = 'F'

        print('Grade:', grade)

main()
