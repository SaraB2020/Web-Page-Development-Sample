"""
#Salary Calculator
"""
yearcount = 0
sum = 0
count = 0
for count in range (6):
    count = count + 1    
    for yearcount in range (5):
        yearcount = yearcount +1   
        newsalary = input("Please enter employee " + str(count) + " salary for year " + str(yearcount) +": ")
        if (yearcount<2):
            smallest=newsalary
            largest=newsalary
            sum = newsalary
        elif(newsalary<smallest):
            smallest = newsalary
            sum = sum + newsalary
        elif(newsalary >largest):
            largest = newsalary
            sum = sum + newsalary
        else:
            sum = sum + newsalary
        avg = float(sum) / yearcount
        
    string1 = ("Employee " + str(count))
    print(string1 + " smallest salary is: $"+str(smallest))
    print(string1 + " highest salary is: $" + str(largest))
    print(string1 + " average salary is: $"+str(avg))
    print("**********")  