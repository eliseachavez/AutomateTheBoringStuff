def collatz(num):
    if num == 1:
        return
    #number is even: check if it is even by seeing if it is a multiple of 2--so it mod 2 will be 0.
    elif num%2 == 0:
        print(str(num/2))
        return collatz(num/2)
    #number is odd
    elif num%2 == 1:
        print(str((3*num)+1))
        return collatz((3*num)+1)
    #number should be 0...
##############MAIN###################

print('Step right up, young lass or gent! Pick a number, any number!!')
collatz(int(input()))

#####################################
#NOTE: Did not work the first time, stuck recursively going through 4-3-2-1, 4-3-2-1. 
#Was a logic error, because I had the escape case (n = 1) as the last case
#when it should have been the first, so it was never reaching its escape case. 
#Instead, when the number reached 1 it would go down the n is odd branch and recurse.

#program is 8 lines of code long, when print statements and comments are removed.

#The collatz sequence has been checked for numbers up to 2^60
