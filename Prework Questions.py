# Question 1
# Write a function to print "hello_USERNAME!"

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(start, end):
    for i in range (start, end+1):
        if i%2==1:
            print (i)
first_odds(1,100)  

# Question 3
# Write a python function, max_num_in_list to return the max number in a given list

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print (max_num_in_list([1,3,7,23,37,76])) 

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if (a_year%400==0) and (a_year%100==0):
        print(a_year, "True")
    elif (a_year%4==0) and (a_year%100 !=0):
        print(a_year, "True")
    else:
        print(a_year, "False") 

is_leap_year(2020)  
is_leap_year(2021)
is_leap_year(1974)
is_leap_year(1776)   

# Question 5
# Write a function to check to see if all numbers in a list are consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    for x in range(1, len(a_list)):
        forward = a_list[x] - a_list[x-1]
        backward = a_list[x-1] - a_list[x-2]
    if forward == backward:
        return True
    else:
        return False

print (is_consecutive([5, 6, 7, 8, 9])) 
print (is_consecutive([2, 5, 6, 7, 12, 30]))   