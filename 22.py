a=[2,6,3,9,5,8]
b=[]
c=[]
for x in range(len(a)):
    if(a[x]%2==0):
        b.append(a[x])
    else:
        c.append(a[x])
print("Thus the even nos are: ",b)
print("Thus the odd nos are: ",c)


 Use if-else in Lambda Functions

# check if number is even or odd
result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"

# print for numbers
print(result(12))
print(result(11))

# Lambda Function
# SYNTAX - lambda ARg : EXPRESSION

# x = lambda a,b: a+b
# # x is not a variable......   x is a function which contains same number of parameter as the lambda function 


# z= x(2,4)

# print("Addition of two number using lambda function - ", x(2,4))

# normal function

# x=0
# y=0
# print("Result = ", add(x,y))


# def add(a,b):
#     a= int(input("Enter fst number - "))
#     b= int(input("Enter secnd number - "))
#     return(a+b)



# Simple lambda function
# Find even num
