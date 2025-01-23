num1 = float(input("enter the 1st no.: "))
num2 = float(input("enter the 2nd no.: "))
num3 = float(input("enter the 3rd no.: "))

if((num1>num2) & (num1>num3)):{
    print(num1,"is the largest no.")
}
elif((num2>num1) & (num2>num3)):{
    print(num2,"is the largest no.")
}
elif((num3>num1) & (num3>num2)):{
    print(num3,"is the largest no.")
}