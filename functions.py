def greet (student, country):
    print(f"{student}, welcome to {country}")

def subtract (a, b):
    answer = a - b 
    return answer
# functional argument:
    # >>> from functions import subtract
    # >>> subtract(4, 5)
    # -1

# keyword argument:
    # >>> subtract(b=4,a= 5)
    # 1
    # >>> 

def my_country(country = "Kenya") :
    print(f"Hello, I am from {country}") 
# default arguments:
#  can either take the assigned argument in the functions 
# or take the one assigned in the interpretor
    # >>> from functions import my_country
    # >>> 
    # >>> my_country()
    # Hello, I am from Kenya
    # >>> my_country("Rwanda")
    # Hello, I am from Rwanda
    # >>> 

def hello (*names):
    for name in names:
        return (f"hello, {name}")
    
# a function that accepts any number of arguments
def sum (*nums):
    ans = 0
    for num in nums:
        ans += num
    return ans

# a function that accepts any number of keyword arguments(kwargs)
def multiply(**nums):
    answer = 1
    for num in nums.values():
        answer *=num


    return answer

    
