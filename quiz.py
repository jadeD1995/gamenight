print('Welcome to the quize about life')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What started  the world') 
    if answer.lower()=='aliens':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: we all have 3rd eyes  true or false  ')
    if answer.lower()=='true':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What did et say  "et phone......?')
    if answer.lower()=='home':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
print('BYE!')