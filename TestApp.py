# Import stuff
import random
import time
import pprint

import MyFunctions as my


# Print shit
msg = "Hello World"
print(msg)
msg = 3+5
print(msg)


# Getting time
if time.gmtime().tm_sec < 30:
    print('under 30')
else:
    print('over 30')

# IF statements 
if time.gmtime().tm_sec%3 == 0:
    print('Divisable by 3!')
    print('testing')
    print('testing')
else:
    print('NOT Divisable by 3!')
    print('NOT testing')
    print('NOT testing')

# Indents matter motherfucker
print('fuck')

# For loops
for i in range(5):
    random_num = random.randint(2,7)
    print(random_num)
#    time.sleep(random_num)
    this_second = time.gmtime().tm_sec
    print('this second: %s' %this_second)
    if this_second%3 == 0:
        print('hit it')
        continue

# Data structures

# List
num_list = [1,2,3,4]

print(num_list[-2])
for i in range(4):
    print('number %s' %num_list[i])

if 6 in num_list:
    print('There is a 6')
else:
    print('There NOT a 6')

# List append
num_list.append(6)
print(num_list)

# List popped
poppedValue = num_list.pop()
print('Popped value = %s' %poppedValue)

# List insert
num_list.insert(0,0)
print(num_list)

# List append
num_list.extend([5,6,7,8])
print(num_list)

# Start stop and step / slicing / non destructive
limited_num_list = num_list[0:8:3]
print(limited_num_list)

limited_num_list = num_list[::3]
print(limited_num_list)

limited_num_list = num_list[1::3]
print(limited_num_list)

limited_num_list = num_list[1:7:3]
print(limited_num_list)

#sentance = input("Enter a sentence: ")
#print(sentance)
#print(sentance[0:7])
#print(sentance[::-1])

# Copies of lists - only chnages pointer
another_num_list = num_list
print(another_num_list)
num_list.append(9)
print(another_num_list)
print(num_list)

# Copy actual list
yet_another_num_list = num_list.copy()
num_list.append(9)
print(yet_another_num_list)
print(num_list)

# Range function
range(0,5)
print(list(range(5)))
print(list(range(0,10,2)))
print(list(range(10,0,-2)))


# Dictionary
customer1 = {'Name': 'Klara Kempf', 'Gender' : 'Female', 'Nationality': 'German', 'Car': 'Audi A4'}
print(customer1['Name'])
print(customer1['Car'])


#sentance = input("Enter a sentence: ")
sentance = 'This is a fucking slow tutorial'
vowels = {'a','e','i','o','u','y'}
vowel_count = {}
vowel_count['a'] = 0
vowel_count['e'] = 0
vowel_count['i'] = 0
vowel_count['o'] = 0
vowel_count['u'] = 0
vowel_count['y'] = 0
print(vowel_count)

for ch in list(sentance):
    if ch in vowel_count:
        vowel_count[ch] += 1
print(vowel_count)

for k, v in sorted(vowel_count.items()):
    print('Frequency of %s: %i' %(k,v))

sentance2 = 'This is a fucking slow tutorial part two because I needed another sentance'

vowel_count2 = {}
print(vowel_count2)

for ch in list(sentance2):
    if ch in vowels:
        vowel_count2.setdefault(ch,0)
        vowel_count2[ch] += 1
print(vowel_count2)

for w, x in sorted(vowel_count2.items()):
    print('Frequency of %s: %i' %(w,x))


customer2 = {}
customer2['Klara'] = {'Name': 'Klara Kempf', 'Gender' : 'Female', 'Nationality': 'German', 'Car': 'Audi A4'}
customer2['Brad'] = {'Name': 'Brad Daniels', 'Gender' : 'Male', 'Nationality': 'French', 'Car': 'BMW 3 Series'}
customer2['Jeff'] = {'Name': 'Jeff Joeman', 'Gender' : 'Male', 'Nationality': 'Polish', 'Car': 'Ford F150'}
customer2['Dan'] = {'Name': 'Dan Dingel', 'Gender' : 'Male', 'Nationality': 'Russian', 'Car': 'Toyota Camery'}

pprint.pprint(customer2)

print(customer2['Brad']['Car'])

# Sets and Tuples - sets cannot have dup values
vowels3 = set('aeiouy')
print(vowels3)

sentance3 = 'headphones'
union_set = vowels3.union(set(sentance3))
print(union_set)

differnce_set = vowels3.difference(set(sentance3))
print(differnce_set)

intersection_set = vowels3.intersection(set(sentance3))
print(intersection_set)

vowels_tuple = ('a','e','i','o','u','y')
print(vowels_tuple)
print(vowels_tuple[2])


test_sentance = 'zippy do da zippy day, my oh my what a wonderful day'
counter1 = my.dCountVowels(test_sentance)
print('Vowel Count %s' %counter1)

test_string = my.sFindCommonLetters(test_sentance, sentance3)
print('Common letters %s' %test_string)

test_string = my.sFindCommonLetters(test_sentance)
print('Common letters %s' %test_string)
