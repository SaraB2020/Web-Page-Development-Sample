"""
#Module5Homework1
"""

def calculatewages(hw,hr):
    wages = hw * hr
    return wages;
def CalculateFederalTax(sal,marstat):
    if(marstat == 'Single')or(marstat == "single")or(marstat == "SINGLE"):
        fedtax = sal*25/100
    elif(marstat == 'married')or(marstat =='Married'):
        fedtax = sal*20/100
    else:
        fedtax = sal*22/100
    return fedtax;
def calculatestatetax(sal,state):
    if(state == "CA" or state =='NV' or state == 'SD' or state == 'WA' or state == 'AZ'):
        statax = sal*8/100
        return statax;
    elif(state == "TX"  or state == 'IL' or state == 'MO' or state == 'OH'or state=='VA'):
        statax = sal*7/100
        return statax;
    elif(state == "NM"  or state == 'OR' or state == 'IN' ):
        statax = sal*6/100
        return statax;
    else:
        statax = sal*5/100
        return statax;
def calculatenetsalary(sal,statax,fedtax):
    netsal = sal - statax - fedtax
    return netsal;

hoursworked = input("Please enter your work hours: ")
hourlyrate = input("Please enter your hourly rate: ")
stateofresidence= input("Please enter your state of resident: ")
maritalstatus = input("Please enter your marital status: ")

salary = calculatewages(hoursworked,hourlyrate)
federaltax = CalculateFederalTax(salary,maritalstatus)
statetax = calculatestatetax(salary,stateofresidence)
netsalary = calculatenetsalary(salary, federaltax, statetax)
print('**********')
print("Your wage is: $" + str(salary))
print("Your federal tax is: $" + str(federaltax))
print("Your state tax is: $" +str(statetax))
print("Your net wage is: $" +str(netsalary))
print('**********')