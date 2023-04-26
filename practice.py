# write a range function and a for loop to return a list 
# contaning all numbers between 100 and 200 that are divisible by 7
def division ():
    # x = range (100, 200+1)
    empty =[]
    for i in range(100,200):
        if (i%7 ==0):
            empty.append(i)
    return empty
print(division())

    # METHOD 2
def division ():
    x = range (100, 200+1)
   
    empty =[i for i in x if i % 7 ==0]
    return empty
print(division())

# use for loop to calculate the average of a list in a range of (55:100)
def numbers():
    sum = 0
    x = range (55,100)
    for i in x:
        sum+=i
        avg= sum/len(x)
    return avg
print(numbers())

# using a while loop print odd numbers between 1 to 10
def prime_numbers(num):
    if num < 2:
        return False
    for i in range(2,num):
        if (num %i ==0):
            return False
    return True
num = 0
while (num <=10):
    if prime_numbers(num):
        print(num)        
    num+=1
    

