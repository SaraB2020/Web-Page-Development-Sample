"""
#Module5Homework1
"""
#This function receives three numbers, add them up and sends back the result.
def addthreenumbers( n1, n2,n3):
    result = n1 + n2 +n3
    return result;
def calculatewages(hw,hr):
    wages = hw * hr
    return wages;

#Take three numbers.
num1= input('Enter a number')
num2= input('Enter another number')
num3 = input('Enter third number')
# send the three numbers to addthreenumbers.
total = addthreenumbers(num1,num2,num3)
#display the result sent back by the function.
print ("the sum of three numbers is ", total)

hoursworked = input("Please enter the number of hours worked: ")
hourlyrate = input("Please enter the hourlyrate")
salary = calculatewages(hoursworked,hourlyrate)
print("Your salary is:" + str(salary))
state= input("Please enter the state of residence: ")
maritalstatus = input("Please enter the marital status")