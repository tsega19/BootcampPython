# Solution for Complete Python Bootcamp From Zero to Hero in Python
import math 
# NUMBER
# Question 1
'''
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25'''
# Solution


# Question 2
'''Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)

What is the value of the expression 4 * 6 + 5 

What is the value of the expression 4 + 6 * 5 
 ''' 
x = 4 * (6 + 5)
y = 4 * 6 + 5 
z = 4 + 6 * 5

print("x = ", x)
print("y = ", y)
print("z = ", z)

# Question 3
'''
What is the type of the result of the expression 3 + 1.5 + 4?

'''
# Solution
r= 3 + 1.5 + 4
print("result is ",r, "and the type is ",type(r))
#Question 4
'''
What would you use to find a number’s square root, as well as its square?
'''
# Solution
# To find the squere root of the number 
 
print(math.sqrt(r)) 

# STRING
# Question 5
'''
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below
'''
# Solution
s = "Hello"
print("index of [1] is ",s[1])
# Question 6
'''
Reverse the string 'hello' using slicing:
'''
# Solution
print("The reverse is of Hello is ", s[-1::-1])
# Question 7
'''
Given the string hello, give two methods of producing the letter 'o' using indexing.
'''
# Solution
print(s[-1])
print(s[4])

# LIST
# Question 8
'''
 Build this list [0,0,0] two separate ways.
 '''
# Solution
w = [0,0,0] 
print(w)
c = [0]*3
print(c)
# Question 9
'''
Reassign 'hello' in this nested list to say 'goodbye' instead:
'''
#Solution
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

# Question 10
'''
Sort the list below:
'''
# solution
list4 = [5,3,4,6,1]
print(sorted(list4))
# TUPLE
'''What is the major difference between tuples and lists?
Answer
tuples immutable. 
How do you create a tuple?
Answer 
parantheses cruve brackets'''

# DICTIONARY
# Question 11
''' Using keys and indexing, grab the 'hello' from the following dictionaries:'''
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
m = d["k1"]
print(m["k2"])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2])
# SETS
# Question 12
'''Use a set to find the unique values of the list below:'''
list5 = [1,2,2,33,4,4,11,22,3,3,2]
# Solution
u = set(list5)
print(u)
# BOOLEAN
# Question 13
'''For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
    What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)'''
# Solution
print(2 > 3)
print(3 <= 2)
print(3 == 2.0)
print(3.0 == 3)
print(4**0.5 != 2)
# Question 14
'''Final Question: What is the boolean output of the cell block below?'''
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
print(l_one[2][0] >= l_two[2]['k1'])





