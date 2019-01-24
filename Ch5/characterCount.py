import pprint  #prints dictionaries in a "pretty" way. keys are also sorted (symbols, then capitals alphabetically, then lowercase alphabetically.
#pprint comes in PARTICULARLY useful when there are nested dicts.
#to get as a string instead, use pprint.pformat() instead of pprint.pprint()

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message: 
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
print(pprint.pformat(count)) #does same thing as above. so i guess pformat doesn't return anything
