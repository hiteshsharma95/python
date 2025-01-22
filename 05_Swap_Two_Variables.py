#METHOD 1 (USING TEMOERARY VARIABLE)--- >>
x = 12
y = 15

temp = x #stored/copy value of x in another variable
x = y
y = temp 
print("the value of x is :",x)
print("the value of y is :",y)

#METHOD 2 (WITHOUT USE TEMP. VARIABLE)

x = 10
y = 20 

x,y = y,x 

print("the vlaue of x is : ", x)
print("the value of y is : ", y)