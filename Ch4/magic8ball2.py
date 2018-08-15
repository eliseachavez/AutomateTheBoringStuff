import random

#"childish replies" edition

messages = ['Dunno', 'No duh', 'No shit sherlock', 
'No YOU are', 'Up your butt, round the corner', 'Moo', 
'through your tube and out your boob', 
'Sure as sherbert', 'Hay is for horses', 
'I\'m telling on you', 'Ooooooooooooooo mamamamama-maaaaa!']

questionUnasked = True

while questionUnasked:
    print('Ask me your question to which yes or no can be an answer, and I will tell you your future')
    question = str(input())
    if '?' not in question:
        print ("That was not a question; do not tempt my wrath!!!")
    else:
        questionUnasked = False
        print(messages[random.randint(0, len(messages) -1)]) 



