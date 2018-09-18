encryptedText = ['23', '45', '67', '78', '99']
tuplething = (('a','99'), ('b','67'), ('c','23'), ('d','78'), ('e','45')) 

#message:
#abe: (125)+ 10 = (modulo 5) = 11mod5=1 12mod5=2 15mod5 =0  
#+10


decrypted = []

for line in encryptedText:
    for i, (letter, code) in enumerate(tuplething):
        if line in (i, letter, code):
            print('found it in the dictionary!')
            print(i)
            #line = i #tuple is immutable so you can't overwrite it
            iModulated = chr(((i-10)%5)+96) #you can do your math operations on the index. add 96 to make it ascii
            decrypted.append(iModulated) #correct/adjusted positions in new list. now just need to convert to alphabet

for item in decrypted:
    print(item)





#for i in range(len(encryptedText))
