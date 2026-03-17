#A SIMPLE QUIZ PROGRAM

print('===A SIMPLE QUIZ PROGRAM BY SPECTRE===')

QUESTIONS = (
    'WHICH OF THE FOLLOWING IS A NEWTONIAN FLUID? ',
    'WHAT IS VISCOSITY?',
    'THE DIMENSIONAL ANALYSIS FOR PRESSURE IS?',
    'UNIT OF DENSITY IS?',
)

OPTIONS = (
    ('WATER','CLAY','CORN STARCH','GLUE'),
    ('RESISTANCE TO FLOW BY FLUIDS','SHEAR STRESS ON FLUIDS','FORCE PER UNIT LENGTH ON A FLUID','NONE OF THE ABOVE'),
    ('KG/M3','MLT-3','MLT','LT'),
    ('KG/M4','MLT-3','MLT','KG/M3'),
)

ANSWERS = ['a','a','b','d']

options = ['a','b','c','d']
question_index = 0
score = 0

while question_index <= (len(QUESTIONS) - 1):
    question = QUESTIONS[question_index]
    option = OPTIONS[question_index]
    print(question)
    print(option)
    answer = input('A,B,C,D: ')
    
    if answer in options:
        if answer.lower() == ANSWERS[question_index]:
            score += 1
        question_index += 1
    else:
        print('OPTIONS CAN EITHER BE A,B,C,D')
print(f'YOU GOT {score} QUESTION(S) CORRECTLY')
