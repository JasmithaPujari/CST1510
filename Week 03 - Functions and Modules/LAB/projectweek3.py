"""
RECORD CHECK  -  my version
===========================

Name  : Jasmitha Jhagruthi Pujari
Lane  : IT      
Date  : 11/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def print_report(label,value,limit, difference, percent, status): 
    print(f"Label:{label}")
    print(f"Value:{value}")
    print(f"Limit:{limit}")
    print(f"Difference:{difference}")
    print(f"Percent:{percent}")
    print(f"Status:{status}")

def status_of(value,limit): #creating a funtion to determine the status of whther the value is less or more than the limit 
    if value>limit:
        return"OVERLIMIT"
    else:
        return"WITHIN LIMIT"
    
def check(value,limit): #check calculates the defernce and percentage between value and limit
    difference=limit-value
    percent=(value/limit)*100
    return difference, percent

# ==================================================================== INPUT 
#2. Ask for your three values.

label = input("Enter the label:") #the user can input their values and labels
value = float(input("Enter the value:")) 
limit = float(input("Enter the limit:"))

# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
difference=limit-value  
percent = (value/limit)*100  
status = status_of(value, limit) #calling out the def of status
difference,percent=check(value, limit)#calling ou the the check

# =================================================================== OUTPUT
# 4. Print the report.
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")#this is the same code used for week2
print("=" * 34)
print(f"Value:{value:>20.2f}")#>right alighned 2 decimal places
print(f"Limit:{limit:>20.2f}") #.20 is basically the number of space at the right side of the word
print(f"Difference:{difference:>+15.2f}")
print(f"Percent:{percent:>18.2f}%")
print(f"Status:{status:>19}")
print("=" * 34)

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
