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
